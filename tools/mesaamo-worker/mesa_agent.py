#!/usr/bin/env python3
"""MesaAMO / MapaAMO worker helper v0.5.1. No credentials are embedded."""
import argparse, json, os, sys, urllib.request, urllib.error

VERSION = "0.5.1"
DEFAULT_ENDPOINT = "https://ydmnavyadpztydontaqh.supabase.co/functions/v1/mesa-api"
DEFAULT_MEDIA_ENDPOINT = "https://ydmnavyadpztydontaqh.supabase.co/functions/v1/mesa-media"
DEFAULT_ANALYSIS_ENDPOINT = "https://ydmnavyadpztydontaqh.supabase.co/functions/v1/mesa-analysis"

def token():
    t=os.environ.get("MESAAMO_AGENT_TOKEN","").strip()
    if not t: raise SystemExit("FALTA: MESAAMO_AGENT_TOKEN")
    return t

def call(action,payload=None):
    body={"action":action}; body.update(payload or {})
    req=urllib.request.Request(os.environ.get("MESAAMO_ENDPOINT",DEFAULT_ENDPOINT),data=json.dumps(body).encode(),method="POST",headers={"Authorization":f"Bearer {token()}","Content-Type":"application/json","User-Agent":f"MesaAMO-AgentTool/{VERSION}"})
    try:
        with urllib.request.urlopen(req,timeout=25) as r:
            out=r.read().decode(); print(out); return json.loads(out or "{}")
    except urllib.error.HTTPError as e:
        out=e.read().decode() or str(e); print(out,file=sys.stderr); raise SystemExit(e.code)

def main():
    p=argparse.ArgumentParser(description=f"MesaAMO agent helper v{VERSION}")
    s=p.add_subparsers(dest="cmd",required=True)
    h=s.add_parser("heartbeat"); h.add_argument("status",nargs="?",default="ONLINE"); h.add_argument("task",nargs="?",default="Disponible")
    q=s.add_parser("queue"); q.add_argument("--limit",type=int,default=20)
    s.add_parser("connect-poll")
    ca=s.add_parser("connect-ack"); ca.add_argument("request_id"); ca.add_argument("--result",default="CONNECTED")
    d=s.add_parser("download"); d.add_argument("item_id"); d.add_argument("output")
    c=s.add_parser("claim"); c.add_argument("item_id")
    u=s.add_parser("update"); u.add_argument("item_id"); u.add_argument("--progress",type=int); u.add_argument("--status"); u.add_argument("--capability"); u.add_argument("--target"); u.add_argument("--route"); u.add_argument("--note"); u.add_argument("--error-code"); u.add_argument("--error-message")
    sa=s.add_parser("source-analyzed"); sa.add_argument("item_id"); sa.add_argument("summary"); sa.add_argument("--disposition",default="INVESTIGAR")
    cc=s.add_parser("capability-create"); cc.add_argument("source_item_id"); cc.add_argument("title"); cc.add_argument("--description"); cc.add_argument("--slug"); cc.add_argument("--decision",default="INVESTIGAR"); cc.add_argument("--target",action="append",default=[]); cc.add_argument("--route")
    cl=s.add_parser("capability-list"); cl.add_argument("--source")
    cq=s.add_parser("capability-claim"); cq.add_argument("capability_id")
    cu=s.add_parser("capability-update"); cu.add_argument("capability_id"); cu.add_argument("--progress",type=int); cu.add_argument("--status"); cu.add_argument("--decision"); cu.add_argument("--route"); cu.add_argument("--note")
    cf=s.add_parser("capability-complete"); cf.add_argument("capability_id"); cf.add_argument("--decision",default="ADAPTAR"); cf.add_argument("--note",default="Capacidad resuelta y verificada")
    f=s.add_parser("complete"); f.add_argument("item_id"); f.add_argument("--note",default="Fuente resuelta")
    rel=s.add_parser("release"); rel.add_argument("item_id")
    ms=s.add_parser("map-search"); ms.add_argument("query")
    mr=s.add_parser("map-register-node"); mr.add_argument("display_name"); mr.add_argument("--id"); mr.add_argument("--type",default="SYSTEM"); mr.add_argument("--lifecycle",default="ACTIVE"); mr.add_argument("--description"); mr.add_argument("--repository"); mr.add_argument("--manifest")
    a=p.parse_args()
    if a.cmd=="heartbeat": call("heartbeat",{"status":a.status,"current_task":a.task})
    elif a.cmd=="queue": call("queue",{"limit":a.limit})
    elif a.cmd=="connect-poll": call("connect_poll")
    elif a.cmd=="connect-ack": call("connect_ack",{"request_id":a.request_id,"result":a.result})
    elif a.cmd=="download":
        media=os.environ.get("MESAAMO_MEDIA_ENDPOINT",DEFAULT_MEDIA_ENDPOINT)
        req=urllib.request.Request(f"{media}?action=media_url&item_id={a.item_id}",headers={"Authorization":f"Bearer {token()}","User-Agent":f"MesaAMO-AgentTool/{VERSION}"})
        with urllib.request.urlopen(req,timeout=25) as r: info=json.loads(r.read().decode())
        if not info.get("ok"): raise SystemExit(json.dumps(info))
        with urllib.request.urlopen(info["signed_url"],timeout=60) as r, open(a.output,"wb") as out:
            while True:
                b=r.read(1024*1024)
                if not b: break
                out.write(b)
        print(json.dumps({"ok":True,"item_id":a.item_id,"output":a.output}))
    elif a.cmd=="claim": call("claim",{"item_id":a.item_id})
    elif a.cmd=="update":
        m={"progress":a.progress,"status":a.status,"identified_capability":a.capability,"target_project":a.target,"route_summary":a.route,"latest_note":a.note,"error_code":a.error_code,"error_message":a.error_message}; call("update",{"item_id":a.item_id,**{k:v for k,v in m.items() if v is not None}})
    elif a.cmd=="source-analyzed":
        endpoint=os.environ.get("MESAAMO_ANALYSIS_ENDPOINT",DEFAULT_ANALYSIS_ENDPOINT)
        payload={"action":"source_analyzed","item_id":a.item_id,"observed_summary":a.summary,"source_disposition":a.disposition}
        req=urllib.request.Request(endpoint,data=json.dumps(payload).encode(),method="POST",headers={"Authorization":f"Bearer {token()}","Content-Type":"application/json","User-Agent":f"MesaAMO-AgentTool/{VERSION}"})
        try:
            with urllib.request.urlopen(req,timeout=25) as r: print(r.read().decode())
        except urllib.error.HTTPError as e:
            print(e.read().decode() or str(e),file=sys.stderr); raise SystemExit(e.code)
    elif a.cmd=="capability-create": call("capability_create",{"source_item_id":a.source_item_id,"title":a.title,"description":a.description,"capability_slug":a.slug,"decision":a.decision,"targets":a.target,"route_summary":a.route})
    elif a.cmd=="capability-list": call("capability_list",{"source_item_id":a.source} if a.source else {})
    elif a.cmd=="capability-claim": call("capability_claim",{"capability_id":a.capability_id})
    elif a.cmd=="capability-update":
        m={"progress":a.progress,"status":a.status,"decision":a.decision,"route_summary":a.route,"latest_note":a.note}; call("capability_update",{"capability_id":a.capability_id,**{k:v for k,v in m.items() if v is not None}})
    elif a.cmd=="capability-complete": call("capability_complete",{"capability_id":a.capability_id,"decision":a.decision,"latest_note":a.note})
    elif a.cmd=="complete": call("complete",{"item_id":a.item_id,"latest_note":a.note})
    elif a.cmd=="release": call("release",{"item_id":a.item_id})
    elif a.cmd=="map-search": call("map_search",{"query":a.query})
    elif a.cmd=="map-register-node": call("map_register_node",{"id":a.id,"display_name":a.display_name,"node_type":a.type,"lifecycle":a.lifecycle,"description":a.description,"repository":a.repository,"manifest_path":a.manifest})

if __name__=="__main__": main()
