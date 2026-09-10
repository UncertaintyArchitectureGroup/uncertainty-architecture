#!/usr/bin/env python3
"""Source/arm boundaries and measurements from recorded connector interactions."""

from pathlib import PurePosixPath

from _ri_ab_base import COMPACT, CONTROL, digest, exact, measurement, nonempty, planned_runs, require, text_digest


def event_metrics(events, arm, study):
    require(isinstance(events, list), "events must be a chronological list")
    reasons, sizes, attempts, verified = [], [], 0, 0
    if not events:
        reasons.append("no repository interactions recorded")
    for event in events:
        required = {"tool", "operation", "repository", "resource", "ref", "response_bytes"}
        optional = {"observed_ref_sha", "kind", "delivery", "content_sha256"}
        require(isinstance(event, dict) and required <= set(event) <= required | optional, "event: incorrect fields")
        for name in ("tool", "operation", "repository", "resource"):
            require(nonempty(event[name]), f"event.{name} required")
        measurement(event["response_bytes"], "response_bytes")
        sizes.append(event["response_bytes"])
        if event["tool"] != "GitHub" or event["operation"] not in {"fetch", "search", "code_search", "inspect"}:
            reasons.append("unsupported transport or operation")
        require(event["repository"] == study["repository"], "event repository differs from study")
        resource = event["resource"]
        if event["operation"] == "fetch":
            path = PurePosixPath(resource)
            require(bool(path.parts) and not path.is_absolute() and ".." not in path.parts and "\\" not in resource and str(path) == resource, "fetch resource must be a canonical repository-relative path")
        compact = resource == COMPACT or event.get("content_sha256") == study["ri_surface_sha256"]
        known_ri = compact or resource.startswith("assets/repository-intelligence/") or resource.rstrip("/") == "control-map"
        kind = event.get("kind", "ri_compact" if compact else "ri_other" if known_ri else "source")
        require(kind in {"source", "ri_compact", "ri_other"}, "unknown resource kind")
        require(not compact or kind == "ri_compact", "compact identity contradicts resource kind")
        require(not known_ri or kind != "source", "RI resource cannot be classified as ordinary source")
        require("delivery" not in event or kind == "ri_compact", "delivery metadata belongs to compact RI")
        observed, ref = event.get("observed_ref_sha"), event["ref"]
        sha, branch = study["repository_ref"], study["default_branch"]
        require(observed is None or observed == sha, "read source evidence contradicts study SHA")
        if event["operation"] in {"search", "code_search"} and kind == "source":
            require(ref in (None, branch, sha), "search ref is outside the study window")
        else:
            require(ref == sha or ref in (None, branch) and observed == sha, "read must prove the study SHA")
        if kind != "source":
            attempts += 1
            if arm == CONTROL:
                reasons.append("Control accessed RI")
            if kind == "ri_other" or event["operation"] != "fetch":
                reasons.append("RI aid outside the connector compact route")
        if kind == "ri_compact":
            require(event.get("delivery") in {"verified", "unverified", "unavailable"}, "record compact delivery outcome")
            if event["delivery"] == "verified":
                require(event.get("content_sha256") == study["ri_surface_sha256"], "verified RI content does not match frozen complete surface")
                require(event["response_bytes"] is None or event["response_bytes"] > 0, "verified RI delivery cannot have zero response bytes")
                verified += 1
    return {
        "reasons": reasons, "calls": len(events),
        "bytes": None if any(n is None for n in sizes) else sum(sizes),
        "ri_attempts": attempts, "ri_verified": verified,
    }


def validate_runs(study, records):
    exact(records, {"study_sha256", "conditions_confirmed", "source_window", "runs"}, "run bundle")
    require(records["study_sha256"] == digest(study), "study changed after run preparation")
    require(type(records["conditions_confirmed"]) is bool, "conditions_confirmed must be boolean")
    exact(records["source_window"], {"before", "after"}, "source window")
    window_ok = True
    for observation in records["source_window"].values():
        if observation is None:
            window_ok = False
            continue
        exact(observation, {"tool", "repository", "branch", "sha", "evidence"}, "branch observation")
        window_ok &= (
            observation["tool"] == "GitHub" and observation["repository"] == study["repository"]
            and observation["branch"] == study["default_branch"] and observation["sha"] == study["repository_ref"]
            and nonempty(observation["evidence"])
        )
    require(isinstance(records["runs"], list), "runs must be a list")
    plan = {(task["task_id"], arm): message for task, arm, message in planned_runs(study)}
    run_map, sessions, actual_order = {}, set(), []
    for run in records["runs"]:
        exact(run, {"task_id", "arm", "session_id", "submitted_message", "response", "evidence", "events", "deviations", "input_tokens"}, "run")
        require(nonempty(run["task_id"]) and nonempty(run["arm"]), "run task/arm required")
        key = (run["task_id"], run["arm"])
        require(key in plan and key not in run_map, "unknown or duplicate task/arm run")
        require(isinstance(run["response"], str), "response must be exact visible text")
        require(nonempty(run["session_id"]) and run["session_id"] not in sessions, "unique fresh session ID required")
        sessions.add(run["session_id"])
        measurement(run["input_tokens"], "input_tokens")
        require(isinstance(run["deviations"], list) and all(nonempty(v) for v in run["deviations"]), "deviations must be a list of explanations")
        metrics = event_metrics(run["events"], run["arm"], study)
        reasons = metrics["reasons"] + run["deviations"]
        for ok, reason in (
            (records["conditions_confirmed"], "session/configuration conditions unconfirmed"),
            (window_ok, "source window not proven"),
            (run["submitted_message"] == plan[key], "submitted message differs from frozen task"),
            (nonempty(run["response"]), "no final response"),
            (nonempty(run["evidence"]), "raw capture reference missing"),
        ):
            if not ok:
                reasons.append(reason)
        run_map[key] = {**metrics, "reasons": reasons, "input_tokens": run["input_tokens"], "response_id": text_digest(run["session_id"])}
        actual_order.append(key)
    require(actual_order == [key for key in plan if key in run_map], "execution order differs from frozen counterbalanced plan")
    return run_map
