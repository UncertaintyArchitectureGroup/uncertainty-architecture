#!/usr/bin/env python3
"""Mechanically evaluate the preregistered Repository Intelligence A/B study."""

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from _ri_ab_base import *  # noqa: F401,F403,E402
from _ri_ab_prereg import *  # noqa: F401,F403,E402
from _ri_ab_corpus import *  # noqa: F401,F403,E402
from _ri_ab_events import *  # noqa: F401,F403,E402
from _ri_ab_scoring import *  # noqa: F401,F403,E402


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preregistration", type=Path, required=True)
    parser.add_argument("--run-record", type=Path, required=True)
    parser.add_argument("--ecological-frame", type=Path, required=True)
    parser.add_argument("--ecological-pool", type=Path, required=True)
    parser.add_argument("--ecological-selection-seed", required=True)
    parser.add_argument("--pilot-arm-seed", required=True)
    parser.add_argument("--confirmatory-arm-seed", required=True)
    parser.add_argument("--pilot-prompts", type=Path, required=True)
    parser.add_argument("--pilot-key", type=Path, required=True)
    parser.add_argument("--confirmatory-prompts", type=Path, required=True)
    parser.add_argument("--confirmatory-key", type=Path, required=True)
    parser.add_argument("--blind-scores", type=Path, required=True)
    parser.add_argument("--treatment-surface", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        prereg = load(args.preregistration, "preregistration")
        record = load(args.run_record, "run record")
        validate_prereg(prereg)
        treatment_evidence = validate_treatment_surface(args.treatment_surface, prereg)
        evidence = verify_evidence(
            prereg,
            {
                "ecological_frame": args.ecological_frame,
                "ecological_pool": args.ecological_pool,
                "pilot_prompts": args.pilot_prompts,
                "pilot_key": args.pilot_key,
                "confirmatory_prompts": args.confirmatory_prompts,
                "confirmatory_key": args.confirmatory_key,
            },
            {
                "ecological_selection": args.ecological_selection_seed,
                "pilot_arm": args.pilot_arm_seed,
                "confirmatory_arm": args.confirmatory_arm_seed,
            },
        )
        evidence["treatment_surface"] = treatment_evidence
        score_map = validate_blind_scores(args.blind_scores, record, prereg, evidence)
        output = evaluate(prereg, record, evidence, score_map)
        treatment_report = dict(treatment_evidence)
        treatment_report.pop("payload", None)
        output["evidence_verification"]["treatment_surface"] = treatment_report
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(
            json.dumps(output, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print("Repository Intelligence A/B evaluation: " + output["final_conclusion"]["final_status"])
        return 0
    except (OSError, ValueError) as exc:
        print(f"Repository Intelligence A/B evaluation error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
