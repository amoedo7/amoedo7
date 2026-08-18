# MesaAMO Worker v0.5.0

Operational helper for DAMO. This directory contains **no credentials**.

## Architecture

Google Drive is the human/archive layer. Agents do **not** need Google OAuth.
Operational media lives in the private Supabase Storage bucket behind `mesa-media`.

- coordination: `https://ydmnavyadpztydontaqh.supabase.co/functions/v1/mesa-api`
- private media: `https://ydmnavyadpztydontaqh.supabase.co/functions/v1/mesa-media`

## v0.5 model

`1 source image -> N capabilities -> N target nodes -> N verified outcomes`

Before building, query MapaAMO. A source image is only complete after all derived capabilities are resolved.

## Install/update

```bash
mkdir -p ~/.local/share/desarrollamo/mesaamo/bin
curl -fsSL https://raw.githubusercontent.com/amoedo7/amoedo7/main/tools/mesaamo-worker/mesa_agent.py -o ~/.local/share/desarrollamo/mesaamo/bin/mesa_agent.py
curl -fsSL https://raw.githubusercontent.com/amoedo7/amoedo7/main/tools/mesaamo-worker/mapa_indexer.py -o ~/.local/share/desarrollamo/mesaamo/bin/mapa_indexer.py
chmod 700 ~/.local/share/desarrollamo/mesaamo/bin/*.py
```

Runtime variables stay outside Git and Drive:

```bash
export MESAAMO_ENDPOINT='https://ydmnavyadpztydontaqh.supabase.co/functions/v1/mesa-api'
export MESAAMO_MEDIA_ENDPOINT='https://ydmnavyadpztydontaqh.supabase.co/functions/v1/mesa-media'
export MESAAMO_AGENT_TOKEN='<stored locally; never commit>'
```

## Commands

```bash
python mesa_agent.py heartbeat ONLINE Disponible
python mesa_agent.py connect-poll
python mesa_agent.py queue --limit 5
python mesa_agent.py claim ITEM_ID
python mesa_agent.py download ITEM_ID /tmp/item.jpg
python mesa_agent.py capability-create ITEM_ID 'Timeline de actividad' --target PlataformAMO --target MesaAMO
python mesa_agent.py capability-claim CAPABILITY_ID
python mesa_agent.py capability-update CAPABILITY_ID --status IMPLEMENTING --progress 50
python mesa_agent.py capability-complete CAPABILITY_ID --decision ADAPTAR --note 'Implementado y probado'
python mesa_agent.py map-search 'timeline cliente'
```

Polling, heartbeat, connect polling, queue reads and downloads are deterministic and should not call MiniMax. LLM use starts only when an item genuinely needs interpretation/reasoning.
