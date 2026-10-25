"""Send one reviewed PNG post through the owner-private VITTORA connector.
Obtain the current service token with Sites get_site; pass {"token": "..."} on
stdin only. Never save credentials or pass them as command-line arguments.
"""
import argparse
import base64
import json
from pathlib import Path
import sys
import urllib.error
import urllib.request

ORIGIN = "https://vittora-vk.q999666999p.chatgpt.site"

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repository")
    p.add_argument("--caption-file")
    p.add_argument("--image")
    p.add_argument("--confirmed", action="store_true")
    p.add_argument("--illustration-reviewed", action="store_true")
    p.add_argument("--status", action="store_true")
    args = p.parse_args()
    if sys.stdin.isatty():
        import termios
        settings = termios.tcgetattr(sys.stdin)
        settings[3] &= ~termios.ECHO
        termios.tcsetattr(sys.stdin, termios.TCSANOW, settings)
        print("Ready for credential JSON on stdin (hidden).", flush=True)
    credential = json.loads(sys.stdin.readline())
    token = credential.get("token")
    if not isinstance(token, str) or not token:
        p.error("Missing service token")
    headers = {"OAI-Sites-Authorization": "Bearer " + token}
    body = None
    path = "/api/arsenal-status" if args.status else "/api/arsenal-publish"
    if not args.status:
        if not all((args.repository, args.caption_file, args.image,
                    args.confirmed, args.illustration_reviewed)):
            p.error("Require repository, caption-file, image and both review flags")
        image = Path(args.image).read_bytes()
        if len(image) > 1048576 or not image.startswith(b"\x89PNG\r\n\x1a\n"):
            p.error("Use a reviewed PNG under 1 MiB")
        caption = Path(args.caption_file).read_text(encoding="utf-8").strip()
        body = json.dumps({"repository": args.repository, "caption": caption,
                          "image_base64": base64.b64encode(image).decode(),
                          "confirmed": True, "illustration_reviewed": True}).encode()
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(ORIGIN + path, headers=headers, data=body)
    try:
        with urllib.request.urlopen(request, timeout=40) as response:
            result = json.load(response)
    except urllib.error.HTTPError as error:
        # The route returns no secrets. Never repeat an uncertain POST.
        detail = error.read(2000).decode(errors="replace")
        p.exit(1, "HTTP %s: %s\nInspect delivery history before any retry.\n" %
               (error.code, detail))
    except (urllib.error.URLError, TimeoutError):
        p.exit(1, "Request uncertain. Inspect GET /api/arsenal-publish; do not retry automatically.\n")
    if args.status:
        result = result.get("structuredContent", {})
        result = {"can_publish": result.get("can_publish"),
                  "channel": result.get("channel", {}).get("username")}
    print(json.dumps(result, ensure_ascii=False))

if __name__ == "__main__":
    main()
