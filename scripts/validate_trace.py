#!/usr/bin/env python3
"""
Trace Validation Script for Spec-Driven Development

Validates that human-interaction plans carry a usable trace from:
DOMAIN.md / USE_CASES.md / REQUIREMENTS.md -> PLAN.md domain_trace.

This is intentionally conservative. It catches missing or inconsistent IDs and
empty trace fields; it does not try to prove product correctness.
"""

import ast
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple


STATUS_OK = 0
STATUS_WARNINGS = 0
STATUS_ERRORS = 1


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def extract_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---", 4)
    if end == -1:
        return ""
    return text[4:end]


def parse_scalar(value: str):
    value = value.strip()
    if value in ("[]", ""):
        return []
    if value.startswith("[") and value.endswith("]"):
        try:
            parsed = ast.literal_eval(value)
            return parsed if isinstance(parsed, list) else value
        except Exception:
            return [item.strip().strip('"').strip("'") for item in value[1:-1].split(",") if item.strip()]
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    if value in ("true", "false"):
        return value == "true"
    return value


def parse_frontmatter(text: str) -> Dict:
    """Parse the small YAML subset used by PLAN.md frontmatter."""
    fm = extract_frontmatter(text)
    data: Dict = {}
    current_map = None
    current_list_key = None

    for raw_line in fm.splitlines():
        if not raw_line.strip() or raw_line.strip().startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        line = raw_line.split("#", 1)[0].rstrip()

        if indent == 0 and ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            if value.strip():
                data[key] = parse_scalar(value)
                current_map = None
                current_list_key = None
            else:
                data[key] = {}
                current_map = key
                current_list_key = None
            continue

        if current_map and indent == 2 and ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value:
                data[current_map][key] = parse_scalar(value)
                current_list_key = None
            else:
                data[current_map][key] = []
                current_list_key = key
            continue

        if current_map and current_list_key and indent >= 4 and line.strip().startswith("- "):
            data[current_map][current_list_key].append(parse_scalar(line.strip()[2:]))

    return data


def extract_ids(pattern: str, text: str) -> Set[str]:
    return set(re.findall(pattern, text))


def extract_domain_concepts(domain_text: str) -> Set[str]:
    concepts: Set[str] = set()
    for line in domain_text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        first = cells[0]
        if first and first not in {"Concept", "---------", "Level", "-------"} and not first.startswith("["):
            concepts.add(first)
    return concepts


def extract_actors(use_cases_text: str) -> Set[str]:
    actors: Set[str] = set()
    in_actor_table = False
    for line in use_cases_text.splitlines():
        if line.startswith("## Actors and Roles"):
            in_actor_table = True
            continue
        if in_actor_table and line.startswith("## "):
            break
        if not in_actor_table or not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        actor = cells[0]
        if actor and actor not in {"Actor / Role", "--------------"} and not actor.startswith("["):
            actors.add(actor)
    return actors


def as_list(value) -> List[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str):
        if not value or value in {"N/A", "n/a"}:
            return []
        return [value]
    return [str(value)]


def find_plan_files(planning_dir: Path) -> List[Path]:
    return sorted((planning_dir / "phases").glob("**/*-PLAN.md"))


def validate(project_path: Path) -> int:
    planning_dir = project_path / ".planning"
    errors: List[str] = []
    warnings: List[str] = []

    if not planning_dir.exists():
        print(f"ERROR: .planning directory not found at {planning_dir}")
        return STATUS_ERRORS

    domain_text = read_text(planning_dir / "DOMAIN.md")
    use_cases_text = read_text(planning_dir / "USE_CASES.md")
    requirements_text = read_text(planning_dir / "REQUIREMENTS.md")

    requirement_ids = extract_ids(r"\b[A-Z][A-Z0-9]{2,}-\d{2,}\b", requirements_text)
    use_case_ids = extract_ids(r"\bUC-\d{3,}\b", use_cases_text)
    actors = extract_actors(use_cases_text)
    concepts = extract_domain_concepts(domain_text)

    if not domain_text:
        warnings.append("DOMAIN.md missing; trace validation is limited.")
    if not use_cases_text:
        warnings.append("USE_CASES.md missing; trace validation is limited.")

    plan_files = find_plan_files(planning_dir)
    if not plan_files:
        warnings.append("No PLAN.md files found.")

    for plan_path in plan_files:
        rel = plan_path.relative_to(project_path)
        text = read_text(plan_path)
        frontmatter = parse_frontmatter(text)
        requirements = as_list(frontmatter.get("requirements"))
        domain_trace = frontmatter.get("domain_trace", {})
        if not isinstance(domain_trace, dict):
            errors.append(f"{rel}: domain_trace must be an object with interaction_gate/use_cases/actors/concepts/derived_access_rules.")
            domain_trace = {}

        interaction_gate = domain_trace.get("interaction_gate", "not_required")
        if interaction_gate not in {"required", "not_required"}:
            errors.append(f"{rel}: domain_trace.interaction_gate must be 'required' or 'not_required'.")

        for req_id in requirements:
            if requirement_ids and req_id not in requirement_ids:
                errors.append(f"{rel}: requirement '{req_id}' not found in REQUIREMENTS.md.")

        traced_use_cases = as_list(domain_trace.get("use_cases"))
        traced_actors = as_list(domain_trace.get("actors"))
        traced_concepts = as_list(domain_trace.get("concepts"))
        traced_access = as_list(domain_trace.get("derived_access_rules"))

        if interaction_gate == "required":
            if not requirements:
                errors.append(f"{rel}: human-interaction plan must list requirements.")
            if not traced_use_cases:
                errors.append(f"{rel}: domain_trace.use_cases must not be empty when interaction_gate is required.")
            if not traced_actors:
                errors.append(f"{rel}: domain_trace.actors must not be empty when interaction_gate is required.")
            if not traced_concepts:
                errors.append(f"{rel}: domain_trace.concepts must not be empty when interaction_gate is required.")
            if not traced_access:
                warnings.append(f"{rel}: domain_trace.derived_access_rules is empty; confirm roles do not differ for touched concepts.")

        for uc_id in traced_use_cases:
            if use_case_ids and uc_id not in use_case_ids:
                errors.append(f"{rel}: use case '{uc_id}' not found in USE_CASES.md.")
        for actor in traced_actors:
            if actors and actor not in actors:
                errors.append(f"{rel}: actor '{actor}' not found in USE_CASES.md Actors and Roles.")
        for concept in traced_concepts:
            if concepts and concept not in concepts:
                warnings.append(f"{rel}: concept '{concept}' not found in DOMAIN.md Core Concepts table.")

        for rule in traced_access:
            if not re.match(r"^(allowed|denied|unconfirmed):\s+\S", rule):
                errors.append(
                    f"{rel}: derived access rule '{rule}' must start with "
                    "'allowed:', 'denied:', or 'unconfirmed:'."
                )

        task_traces = re.findall(r"<domain_trace>(.*?)</domain_trace>", text, flags=re.DOTALL)
        if interaction_gate == "required" and not task_traces:
            errors.append(f"{rel}: human-interaction plan must include task-level <domain_trace> blocks.")
        for index, task_trace in enumerate(task_traces, start=1):
            for tag in ("actors", "use_cases", "concepts"):
                match = re.search(rf"<{tag}>(.*?)</{tag}>", task_trace, flags=re.DOTALL)
                value = match.group(1).strip() if match else ""
                if interaction_gate == "required" and (not value or value in {"N/A", "n/a", "[]"}):
                    errors.append(f"{rel}: task domain_trace #{index} has empty <{tag}>.")

    print("Trace Validation Results")
    print("=" * 50)
    print(f"Plans checked: {len(plan_files)}")
    print(f"Requirements found: {len(requirement_ids)}")
    print(f"Use cases found: {len(use_case_ids)}")
    print(f"Actors found: {len(actors)}")
    print(f"Concepts found: {len(concepts)}")

    if warnings:
        print(f"\nWARNINGS ({len(warnings)}):")
        for warning in warnings:
            print(f"  - {warning}")

    if errors:
        print(f"\nERRORS ({len(errors)}):")
        for error in errors:
            print(f"  - {error}")
        return STATUS_ERRORS

    print("\nTrace validation passed.")
    return STATUS_WARNINGS if warnings else STATUS_OK


def main() -> None:
    project_path = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    sys.exit(validate(project_path))


if __name__ == "__main__":
    main()
