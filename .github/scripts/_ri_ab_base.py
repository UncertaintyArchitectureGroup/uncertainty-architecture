#!/usr/bin/env python3
"""Frozen study inputs and shared primitives for the bounded RI comparison."""

import hashlib
import json
import re
from pathlib import Path

PROTOCOL_VERSION = 11
CONTROL = "RI-AB-CONTROL"
TREATMENT = "RI-AB-TREATMENT"
COMPACT = "assets/repository-intelligence/agent-context.json"
CONTEXT_METRICS = {"repository_response_utf8_bytes", "input_tokens", "unavailable"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def exact(value, fields, label):
    require(isinstance(value, dict) and set(value) == set(fields), f"{label}: incorrect fields")


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def hex_digest(value, size):
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{%d}" % size, value) is not None


def measurement(value, label):
    require(value is None or type(value) is int and value >= 0, f"{label}: non-negative integer or null required")


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def text_digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, value):
    # Evidence is frozen between stages; refuse to overwrite an existing file.
    with Path(path).open("x", encoding="utf-8") as output:
        output.write(json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n")


def validate_study(study):
    exact(study, {
        "protocol_version", "study_id", "repository", "repository_ref", "default_branch",
        "configuration", "assessor", "selection_note", "frozen_before_execution",
        "smoke_evidence", "ri_surface_sha256", "context_metric", "follow_up_rule", "tasks",
    }, "study")
    require(study["protocol_version"] == PROTOCOL_VERSION, "use protocol v11; v10 evidence is not compatible")
    for name in ("study_id", "repository", "default_branch", "assessor", "selection_note", "smoke_evidence", "follow_up_rule"):
        require(nonempty(study[name]), f"study.{name} required")
    require(hex_digest(study["repository_ref"], 40), "study ref must be a full commit SHA")
    require(hex_digest(study["ri_surface_sha256"], 64), "complete RI surface SHA-256 required")
    require(study["frozen_before_execution"] is True, "freeze the study before execution")
    require(study["context_metric"] in CONTEXT_METRICS, "unknown context metric")
    exact(study["configuration"], {"model", "thinking", "client", "connector"}, "configuration")
    require(all(nonempty(v) for v in study["configuration"].values()), "complete configuration required")
    require(study["configuration"]["connector"] == "GitHub", "study requires the GitHub connector")
    tasks = study["tasks"]
    require(isinstance(tasks, list) and len(tasks) == 12, "initial comparison needs exactly 12 tasks")
    ids, prompts = set(), set()
    for task in tasks:
        exact(task, {"task_id", "prompt", "source_reference", "expected", "serious_errors"}, "task")
        for name in ("task_id", "prompt", "source_reference"):
            require(nonempty(task[name]), f"task.{name} required")
        normalized = " ".join(task["prompt"].split()).casefold()
        require(task["task_id"] not in ids and normalized not in prompts, "duplicate task ID or prompt")
        ids.add(task["task_id"])
        prompts.add(normalized)
        for name in ("expected", "serious_errors"):
            require(isinstance(task[name], list) and task[name] and all(nonempty(v) for v in task[name]), f"task.{name}: concrete scoring expectations required")


def planned_runs(study):
    for index, task in enumerate(study["tasks"]):
        for arm in ((CONTROL, TREATMENT) if index % 2 == 0 else (TREATMENT, CONTROL)):
            message = (
                f"Experiment arm: {arm}\nStudy repository: {study['repository']}\n"
                f"Study ref: {study['repository_ref']}\nTask ID: {task['task_id']}\n"
                f"Task:\n{task['prompt']}"
            )
            yield task, arm, message
