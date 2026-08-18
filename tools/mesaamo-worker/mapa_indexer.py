#!/usr/bin/env python3
"""Indexa amo.project.json en MapaAMO usando mesa_agent.py/map_register_node."""
import argparse, json, os, pathlib, subprocess, sys

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("root",nargs="?",default=os.path.expanduser("~/.openclaw/workspace")); ap.add_argument("--dry-run",action="store_true"); a=ap.parse_args()
    root=pathlib.Path(a.root).expanduser().resolve(); found=0; ok=0
    helper=pathlib.Path(__file__).with_name("mesa_agent.py")
    for p in root.rglob("amo.project.json"):
        found+=1
        try: data=json.loads(p.read_text(encoding="utf-8"))
        except Exception as e: print(json.dumps({"file":str(p),"ok":False,"error":str(e)})); continue
        name=str(data.get("name") or data.get("project") or p.parent.name)
        pid=str(data.get("id") or name)
        lifecycle=str(data.get("lifecycle") or data.get("status") or "ACTIVE").upper()
        kind=str(data.get("type") or data.get("kind") or "PROJECT").upper()
        repo=str(data.get("repository") or data.get("repo") or "")
        desc=str(data.get("description") or "")
        cmd=[sys.executable,str(helper),"map-register-node",name,"--id",pid,"--type",kind,"--lifecycle",lifecycle,"--manifest",str(p.relative_to(root))]
        if repo: cmd += ["--repository",repo]
        if desc: cmd += ["--description",desc]
        if a.dry_run: print(json.dumps({"file":str(p),"command":cmd})); ok+=1; continue
        r=subprocess.run(cmd,text=True,capture_output=True)
        print(r.stdout.strip() or r.stderr.strip()); ok += int(r.returncode==0)
    print(json.dumps({"root":str(root),"found":found,"indexed":ok,"dry_run":a.dry_run}))
if __name__=="__main__": main()
