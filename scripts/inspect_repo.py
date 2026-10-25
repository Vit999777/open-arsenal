"""Read GitHub metadata; never execute repository contents. Python standard library only."""
import argparse
import datetime as dt
import json
import os
import re
import urllib.request
import urllib.error


def inspect(full_name):
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", full_name):
        raise ValueError("Expected owner/repository")
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "open-arsenal-research/1"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    evidence = {}
    def get(suffix):
        url = "https://api.github.com/repos/" + full_name + suffix
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=25) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                evidence[suffix or "repository"] = "not_found_or_inaccessible"
                return None
            raise RuntimeError("GitHub HTTP %s; retry later or check access/rate limit" % e.code) from None
    repo = get("")
    if repo is None:
        raise ValueError("Repository not found or inaccessible")
    readme, license_data, release = get("/readme"), get("/license"), get("/releases/latest")
    return {"repository": repo["full_name"], "url": repo["html_url"],
            "checked_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            "verification_level": "metadata_only", "archived": repo["archived"],
            "pushed_at": repo["pushed_at"], "stars": repo["stargazers_count"],
            "readme_url": readme.get("html_url") if readme else None,
            "license": license_data.get("license") if license_data else None,
            "license_url": license_data.get("html_url") if license_data else None,
            "latest_release_url": release.get("html_url") if release else None,
            "gaps": evidence, "editorial_status": "reviewing",
            "note": "Read the linked sources. Metadata is not a license, security, cost or runtime review."}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository")
    args = parser.parse_args()
    try:
        print(json.dumps(inspect(args.repository), ensure_ascii=False, indent=2))
    except (ValueError, RuntimeError, urllib.error.URLError) as e:
        parser.exit(1, str(e) + "\n")
