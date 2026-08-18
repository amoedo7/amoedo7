# MesaAMO Worker v0.3.0

Bootstrap helper for DAMO. This directory contains no credentials.

Endpoint:

`https://ydmnavyadpztydontaqh.supabase.co/functions/v1/mesa-api`

Install:

```bash
mkdir -p ~/.local/share/desarrollamo/mesaamo/bin
curl -fsSL https://raw.githubusercontent.com/amoedo7/amoedo7/main/tools/mesaamo-worker/mesa_agent.py \
  -o ~/.local/share/desarrollamo/mesaamo/bin/mesa_agent.py
chmod 700 ~/.local/share/desarrollamo/mesaamo/bin/mesa_agent.py
```

Runtime variables must stay outside Git and Drive:

```bash
export MESAAMO_ENDPOINT='https://ydmnavyadpztydontaqh.supabase.co/functions/v1/mesa-api'
export MESAAMO_AGENT_TOKEN='<provided separately>'
```

Smoke test:

```bash
python ~/.local/share/desarrollamo/mesaamo/bin/mesa_agent.py heartbeat ONLINE 'Bootstrap MesaAMO'
python ~/.local/share/desarrollamo/mesaamo/bin/mesa_agent.py queue --limit 5
```

Scopes expected for DAMO: `heartbeat`, `queue`, `register_item`, `claim`, `update`, `complete`, `release`.

Google Drive access is independent from Mesa API authentication. Configure it once via official Google OAuth in rclone; do not store Google passwords or tokens in Git.
