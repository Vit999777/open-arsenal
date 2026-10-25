"""Validate the active 30-day editorial plan without external requests."""
import datetime as dt
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
def validate(plan, candidates, directions):
    errors = []
    try:
        start = dt.date.fromisoformat(plan["start_date"])
        end = dt.date.fromisoformat(plan["end_date"])
        days = (end - start).days + 1
        if days != 30 or plan.get("horizon_days") != 30:
            errors.append("Expected a 30-day horizon")
    except (KeyError, ValueError, TypeError):
        return ["Invalid start/end date"]
    slots = plan.get("slots")
    if not isinstance(slots, list):
        return ["slots must be a list"]
    expected = {(str(start + dt.timedelta(days=d)), time) for d in range(days) for time in ("10:00", "18:00")}
    observed, urls, ids = set(), set(), set()
    published = {c["url"].lower().rstrip("/").removesuffix(".git") for c in candidates if c.get("publication", {}).get("status") == "published"}
    for i, slot in enumerate(slots):
        if not isinstance(slot, dict):
            errors.append(f"slot[{i}] must be an object")
            continue
        prefix = slot.get("id", f"slot[{i}]")
        identity = (slot.get("date"), slot.get("time"))
        if identity in observed or identity not in expected:
            errors.append(f"{prefix}: duplicate or out-of-range time slot")
        observed.add(identity)
        if prefix in ids:
            errors.append(f"{prefix}: duplicate id")
        ids.add(prefix)
        url = str(slot.get("url", "")).lower().rstrip("/").removesuffix(".git")
        if not re.fullmatch(r"https://github.com/[a-z0-9_.-]+/[a-z0-9_.-]+", url) or url in urls:
            errors.append(f"{prefix}: invalid or duplicate repository URL")
        urls.add(url)
        if url in published and slot.get("status") != "published":
            errors.append(f"{prefix}: already published; choose another candidate")
        if slot.get("direction") not in directions:
            errors.append(f"{prefix}: unknown direction")
        if slot.get("timezone") != "Europe/Moscow":
            errors.append(f"{prefix}: wrong timezone")
        if slot.get("status") not in ("planned_research", "researching", "draft", "ready", "published", "blocked", "skipped"):
            errors.append(f"{prefix}: unknown status")
        for key in ("topic", "repository", "vittora_benefit", "post_angle", "pilot", "illustration_brief"):
            if not isinstance(slot.get(key), str) or not slot[key].strip():
                errors.append(f"{prefix}: missing {key}")
        check = slot.get("metadata_check", {})
        if check.get("exists") is not True or check.get("archived") is not False:
            errors.append(f"{prefix}: repository metadata not confirmed")
        if slot.get("status") == "published" and not slot.get("publication", {}).get("url"):
            errors.append(f"{prefix}: published requires receipt URL")
    if observed != expected:
        errors.append("Plan must cover both slots on every date")
    return errors

if __name__ == "__main__":
    plan = json.loads((ROOT / "content-plan/current.json").read_text())
    candidates = json.loads((ROOT / "data/candidates.json").read_text())
    policy = json.loads((ROOT / "config/research.json").read_text())
    errors = validate(plan, candidates, policy["directions"])
    print("\n".join(errors) if errors else "Plan valid: 30 days, 60 unique repository slots; editorial review still required")
    sys.exit(bool(errors))
