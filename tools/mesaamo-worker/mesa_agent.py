#!/usr/bin/env python3
import argparse
import json
import os
import sys
import urllib.request
import urllib.error

DEFAULT_ENDPOINT = "https://ydmnavyadpztydontaqh.supabase.co/functions/v1/mesa-api"


def call(action, payload=None):
    token = os.environ.get("MESAAMO_AGENT_TOKEN", "").strip()
    if not token:
        raise SystemExit("FALTA: export MESAAMO_AGENT_TOKEN='...'")
    endpoint = os.environ.get("MESAAMO_ENDPOINT", DEFAULT_ENDPOINT)
    body = {"action": action}
    if payload:
        body.update(payload)
    data = json.dumps(body).encode()
    req = urllib.request.Request(
        endpoint,
        data=data,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "MesaAMO-AgentTool/0.3.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as res:
            print(res.read().decode())
    except urllib.error.HTTPError as e:
        print(e.read().decode() or str(e), file=sys.stderr)
        raise SystemExit(e.code)


def main():
    p = argparse.ArgumentParser(description="MesaAMO agent helper")
    sub = p.add_subparsers(dest="cmd", required=True)

    h = sub.add_parser("heartbeat")
    h.add_argument("status", nargs="?", default="ONLINE")
    h.add_argument("task", nargs="?", default="Disponible")

    q = sub.add_parser("queue")
    q.add_argument("--limit", type=int, default=20)

    r = sub.add_parser("register")
    r.add_argument("file_name")
    r.add_argument("--drive-id")
    r.add_argument("--media-type", default="image/jpeg")
    r.add_argument("--sha256")

    c = sub.add_parser("claim")
    c.add_argument("item_id")

    u = sub.add_parser("update")
    u.add_argument("item_id")
    u.add_argument("--progress", type=int)
    u.add_argument("--status")
    u.add_argument("--capability")
    u.add_argument("--target")
    u.add_argument("--route")
    u.add_argument("--note")
    u.add_argument("--error-code")
    u.add_argument("--error-message")

    f = sub.add_parser("complete")
    f.add_argument("item_id")
    f.add_argument("--note", default="Adaptación finalizada")

    rel = sub.add_parser("release")
    rel.add_argument("item_id")

    a = p.parse_args()
    if a.cmd == "heartbeat":
        call("heartbeat", {"status": a.status, "current_task": a.task})
    elif a.cmd == "queue":
        call("queue", {"limit": a.limit})
    elif a.cmd == "register":
        call("register_item", {
            "file_name": a.file_name,
            "drive_file_id": a.drive_id,
            "media_type": a.media_type,
            "sha256": a.sha256,
        })
    elif a.cmd == "claim":
        call("claim", {"item_id": a.item_id})
    elif a.cmd == "update":
        payload = {"item_id": a.item_id}
        mapping = {
            "progress": a.progress,
            "status": a.status,
            "identified_capability": a.capability,
            "target_project": a.target,
            "route_summary": a.route,
            "latest_note": a.note,
            "error_code": a.error_code,
            "error_message": a.error_message,
        }
        payload.update({k: v for k, v in mapping.items() if v is not None})
        call("update", payload)
    elif a.cmd == "complete":
        call("complete", {"item_id": a.item_id, "latest_note": a.note})
    elif a.cmd == "release":
        call("release", {"item_id": a.item_id})


if __name__ == "__main__":
    main()
