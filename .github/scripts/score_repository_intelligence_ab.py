#!/usr/bin/env python3
"""Prepare and score the 12-pair preliminary RI workflow comparison."""

import argparse
from pathlib import Path
import sys

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from _ri_ab_base import (  # noqa: E402
    CONTROL, TREATMENT, PROTOCOL_VERSION, digest, exact, nonempty, planned_runs,
    read_json, require, text_digest, validate_study, write_json,
)
from _ri_ab_events import validate_runs  # noqa: E402


def initial_records(study):
    return {
        "study_sha256": digest(study), "conditions_confirmed": False,
        "source_window": {"before": None, "after": None},
        "runs": [
            {"task_id": task["task_id"], "arm": arm, "session_id": "",
             "submitted_message": message, "response": "", "evidence": "",
             "events": [], "deviations": [], "input_tokens": None}
            for task, arm, message in planned_runs(study)
        ],
    }


def blind_packet(study, records, run_map):
    tasks = {task["task_id"]: task for task in study["tasks"]}
    entries = []
    for run in records["runs"]:
        task = tasks[run["task_id"]]
        entries.append({
            "response_id": run_map[(run["task_id"], run["arm"])]["response_id"],
            "task_id": task["task_id"], "prompt": task["prompt"],
            "expected": task["expected"], "serious_errors": task["serious_errors"],
            "response": run["response"], "response_sha256": text_digest(run["response"]),
            "quality": None, "serious_error": None,
        })
    return {
        "protocol_version": PROTOCOL_VERSION, "study_sha256": digest(study),
        "runs_sha256": digest(records), "scorer": "", "scored_before_reveal": False,
        "responses": sorted(entries, key=lambda entry: entry["response_id"]),
    }


def blind_scores(study, records, run_map, packet):
    expected = blind_packet(study, records, run_map)
    exact(packet, expected, "blind scoring packet")
    for field in ("protocol_version", "study_sha256", "runs_sha256"):
        require(packet[field] == expected[field], "blind packet does not match frozen evidence")
    require(nonempty(packet["scorer"]) and packet["scored_before_reveal"] is True, "independent blind scoring must finish before arm reveal")
    require(isinstance(packet["responses"], list), "blind responses must be a list")
    frozen = {entry["response_id"]: entry for entry in expected["responses"]}
    scores = {}
    for entry in packet["responses"]:
        fields = {"response_id", "task_id", "prompt", "expected", "serious_errors", "response", "response_sha256", "quality", "serious_error"}
        exact(entry, fields, "blind response")
        rid = entry["response_id"]
        require(isinstance(rid, str) and rid in frozen and rid not in scores, "unknown/duplicate blind response")
        for field in fields - {"quality", "serious_error"}:
            require(entry[field] == frozen[rid][field], "blind response or scoring expectations changed")
        require(type(entry["quality"]) is int and 0 <= entry["quality"] <= 2, "quality must be 0, 1 or 2")
        require(type(entry["serious_error"]) is bool, "serious_error must be boolean")
        require(not entry["serious_error"] or entry["quality"] == 0, "a serious error must score 0")
        scores[rid] = entry
    require(set(scores) == set(frozen), "blind scores must cover exactly the recorded responses")
    return scores


def ratio(b, a):
    # Null represents missing or unbounded comparison, never a favorable zero.
    if a is None or b is None or a == 0 and b > 0:
        return None
    return b / a if a else 1.0


def total(valid, arm, field):
    values = [case[arm][field] for case in valid]
    return sum(values) if values and all(value is not None for value in values) else None


def evaluate(study, records, packet):
    validate_study(study)
    run_map = validate_runs(study, records)
    scores = blind_scores(study, records, run_map, packet)
    cases = []
    for task in study["tasks"]:
        case = {"task_id": task["task_id"], "valid": True, "invalid_reasons": {}}
        for arm, label in ((CONTROL, "A"), (TREATMENT, "B")):
            run = run_map.get((task["task_id"], arm))
            reasons = run["reasons"] if run else ["run missing"]
            if reasons:
                case["valid"] = False
                case["invalid_reasons"][label] = reasons
            if run:
                score = scores[run["response_id"]]
                case[label] = {**{key: run[key] for key in ("calls", "bytes", "input_tokens", "ri_attempts", "ri_verified")}, "quality": score["quality"], "serious_error": score["serious_error"]}
        cases.append(case)
    valid = [case for case in cases if case["valid"]]
    wins = sum(case["B"]["quality"] > case["A"]["quality"] for case in valid)
    usable_wins = sum(case["B"]["quality"] == 2 and case["A"]["quality"] < 2 for case in valid)
    losses = sum(case["B"]["quality"] < case["A"]["quality"] for case in valid)
    new_serious = sum(case["B"]["serious_error"] and not case["A"]["serious_error"] for case in valid)
    removed_serious = sum(case["A"]["serious_error"] and not case["B"]["serious_error"] for case in valid)
    totals = {arm: {field: total(valid, arm, field) for field in ("calls", "bytes", "input_tokens", "ri_attempts", "ri_verified")} for arm in ("A", "B")}
    calls = ratio(totals["B"]["calls"], totals["A"]["calls"])
    metric = {"repository_response_utf8_bytes": "bytes", "input_tokens": "input_tokens"}.get(study["context_metric"])
    volume = ratio(totals["B"][metric], totals["A"][metric]) if metric else None
    complete = len(valid) == 12
    quality_gain = usable_wins >= 2 and calls is not None and calls <= 1.5
    # Faster incorrect answers cannot establish useful orientation efficiency.
    efficiency = all(case["B"]["quality"] == 2 for case in valid) and calls is not None and calls <= 0.8 and volume is not None and volume <= 1.0
    if not complete:
        status = "INCONCLUSIVE"
    elif losses or new_serious:
        status = "REGRESSION"
    elif totals["B"]["ri_verified"] and (quality_gain or efficiency):
        status = "BENEFIT SHOWN"
    else:
        status = "NO BENEFIT SHOWN"
    return {
        "protocol_version": PROTOCOL_VERSION, "study_id": study["study_id"],
        "repository_ref": study["repository_ref"], "study_sha256": digest(study),
        "runs_sha256": digest(records), "scores_sha256": digest(packet),
        "claim_scope": "Preliminary comparison on these 12 tasks; full RI-EVAL acceptance remains open",
        "final_status": status, "valid_pairs": len(valid), "quality_wins": wins,
        "usable_quality_wins": usable_wins, "quality_losses": losses, "quality_ties": len(valid) - wins - losses,
        "new_serious_errors": new_serious, "removed_serious_errors": removed_serious,
        "totals_over_valid_pairs": totals, "connector_ratio_b_over_a": calls,
        "context_metric": study["context_metric"], "context_ratio_b_over_a": volume,
        "cases": cases,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("init", "prepare", "score"))
    parser.add_argument("--study", type=Path, required=True)
    parser.add_argument("--runs", type=Path)
    parser.add_argument("--scores", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        study = read_json(args.study)
        validate_study(study)
        if args.command == "init":
            output = initial_records(study)
        else:
            require(args.runs is not None, "--runs required for prepare/score")
            records = read_json(args.runs)
            if args.command == "prepare":
                output = blind_packet(study, records, validate_runs(study, records))
            else:
                require(args.scores is not None, "--scores required for score")
                output = evaluate(study, records, read_json(args.scores))
        write_json(args.output, output)
        print(output.get("final_status", f"Prepared {args.output.name}"))
        return 0
    except (OSError, ValueError, TypeError) as exc:
        print(f"RI comparison error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
