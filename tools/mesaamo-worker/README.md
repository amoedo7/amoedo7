# MesaAMO Worker v0.4.0

Operational helper for DAMO. This directory contains **no credentials**.

## Architecture

Google Drive is the human/archive layer. Agents do **not** need Google OAuth.

Operational media lives in the private Supabase Storage bucket behind `mesa-media`:

- coordination: `https://ydmnavyadpztydontaqh.supabase.co/functions/v1/mesa-api`
- private media gateway: `https://ydmnavyadpztydontaqh.supabase.co/functions/v1/mesa-media`

MesaAMO Android ingests working copies into the private factory. DAMO obtains a short-lived signed media URL using its existing agent credential.

## Install / update

```bash
mkdir -p ~/.local/share/desarrollamo/mesaamo/bin
curl -fsSL https://raw.githubusercontent.com/amoedo7/amoedo7/main/tools/mesaamo-worker/mesa_agent.py \
  -o ~/.local/share/desarrollamo/mesaamo/bin/mesa_agent.py
chmod 700 ~/.local/share/desarrollamo/mesaamo/bin/mesa_agent.py
```

Runtime variables stay outside Git and Drive:

```bash
export MESAAMO_ENDPOINT='https://ydmnavyadpztydontaqh.supabase.co/functions/v1/mesa-api'
export MESAAMO_MEDIA_ENDPOINT='https://ydmnavyadpztydontaqh.supabase.co/functions/v1/mesa-media'
export MESAAMO_AGENT_TOKEN='<stored locally; never commit>'
```

## Commands

```bash
python mesa_agent.py heartbeat ONLINE 'Disponible'
python mesa_agent.py queue --limit 5
python mesa_agent.py claim <ITEM_ID>
python mesa_agent.py download <ITEM_ID> /tmp/mesa-item.jpg
python mesa_agent.py update <ITEM_ID> --status ANALYZING --progress 10 --note 'Analizando capacidad'
python mesa_agent.py complete <ITEM_ID> --note 'Adaptación finalizada y verificada'
python mesa_agent.py release <ITEM_ID>
```

`download` asks `mesa-media` for a time-limited signed URL. The bucket remains private and the Supabase server secret is never exposed to DAMO.

Scopes expected for DAMO: `heartbeat`, `queue`, `register_item`, `claim`, `update`, `complete`, `release`.

Polling, heartbeat, queue reads and downloads are deterministic. They do not require MiniMax/LLM calls.
