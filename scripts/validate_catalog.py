"""Validate the catalog and prevent incomplete/stale cards from being marked ready."""
import datetime as dt
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]


def validate(cards, policy, today=None):
    today = today or dt.datetime.now(dt.timezone.utc).date()
    errors, seen = [], set()
    if not isinstance(cards, list):
        return ["Catalog must be a list"]
    for i, c in enumerate(cards):
        prefix = "card[%d]" % i
        if not isinstance(c, dict):
            errors.append(prefix + ": expected object")
            continue
        url = c.get("url", "")
        match = re.fullmatch(r"https://github.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)/?", str(url))
        key = ("/".join(match.groups()).removesuffix(".git").lower()) if match else None
        if not key or key in seen:
            errors.append(prefix + ": invalid or duplicate repository URL")
        if key:
            seen.add(key)
        if c.get("status") not in policy["statuses"]:
            errors.append(prefix + ": invalid status")
        if c.get("direction") not in policy["directions"]:
            errors.append(prefix + ": invalid direction")
        if c.get("status") not in ("ready", "pilot", "adopted"):
            continue
        for field in ("concrete_problem", "application_example", "first_pilot", "success_metric", "requirements_and_costs", "limitations", "license_review", "comparison"):
            if not isinstance(c.get(field), str) or not c[field].strip():
                errors.append(prefix + ": missing " + field)
        if c.get("verification_level") not in ("documentation", "installed", "pilot_passed"):
            errors.append(prefix + ": invalid verification level")
        if c.get("status") == "adopted" and c.get("verification_level") != "pilot_passed":
            errors.append(prefix + ": adopted requires pilot_passed")
        for field in ("readme_source", "license_source"):
            source = urlparse(str(c.get(field, "")))
            if source.scheme != "https" or not source.netloc:
                errors.append(prefix + ": missing HTTPS " + field)
        try:
            age = (today - dt.date.fromisoformat(c.get("verification_date", ""))).days
            if age < 0 or age > policy["max_evidence_age_days"]:
                raise ValueError()
        except (ValueError, TypeError):
            errors.append(prefix + ": stale/invalid verification date")
        scores = c.get("scores", {})
        if not isinstance(scores, dict) or any(type(scores.get(k)) not in (int, float) or not 0 <= scores[k] <= 5 for k in policy["dimensions"]):
            errors.append(prefix + ": each score must be numeric 0..5")
        elif sum(scores[k] * w / 5 for k, w in policy["dimensions"].items()) < policy["ready_score"]:
            errors.append(prefix + ": score below readiness threshold")
    return errors

if __name__ == "__main__":
    errors = validate(json.loads((ROOT / "data/candidates.json").read_text()), json.loads((ROOT / "config/research.json").read_text()))
    print("\n".join(errors) if errors else "Catalog valid (readiness is not publication approval)")
    sys.exit(bool(errors))
