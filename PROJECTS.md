# Inventario GitHub · DesarrollAMO

Revisión realizada el **18 de agosto de 2026** sobre los repositorios existentes en la cuenta operativa `amoedo7`.

Este inventario evita confundir repos históricos, placeholders y fuentes canónicas. Cada uno de los 19 repos revisados contiene además un `amo.project.json` con clasificación legible por máquina.

| Repo | Tipo | Estado | Fuente de verdad |
|---|---|---|---|
| `landings` | infraestructura web | activo/reutilizable | parcial |
| `AutoDesarrollAMO` | automatización | prototipo histórico | no; no es DAMO actual |
| `PorduccionEmpresa` | starter operativo privado | funcional con hardening pendiente | snapshot histórico |
| `DesarrollAmo` | sitio web | referencia histórica | no |
| `CobrAMO` | referencia de cobro | placeholder | no; source de producción aún no localizado aquí |
| `Eros` | web | stub histórico | no |
| `CriptAmo` | criptografía | experimento histórico | snapshot histórico |
| `termuxschool` | educación/Termux | archivo de aprendizaje | no |
| `PidAmoFrontend` | frontend | placeholder | `PidAmo` |
| `PidAmoBackend` | backend | placeholder | `PidAmo` |
| `PidAmo` | producto vertical | prototipo funcional histórico | canónico para esa etapa |
| `ApostAmo` | social/puntos virtuales | prototipo funcional histórico | snapshot histórico |
| `IAMO` | interfaz humano ↔ IA | prototipo conceptual histórico | no; concepto sigue vigente |
| `INRED` | reservado | placeholder sin propósito documentado | no |
| `Frases` | experimento BIP39 | histórico/incompleto | no |
| `nada` | scratch | histórico | no |
| `Truco` | web | prototipo mínimo histórico | no |
| `Armacabeza` | orquestación modular | antecedente conceptual | no |
| `HolaMundo.bat` | aprendizaje Batch | archivo histórico | no |

## Relaciones importantes

```text
landings
└── branding/                 identidad web compartida provisional

PidAmo                       implementación histórica principal
├── PidAmoFrontend           placeholder
└── PidAmoBackend            placeholder

CriptAmo
├── Frases                    experimento relacionado
└── nada                      scratch relacionado

Armacabeza                    antecedente de orquestación modular
├── AutoDesarrollAMO          prototipo posterior de automatización
└── IAMO                      exploración humano ↔ IA

CobrAMO
└── repo placeholder; producción y source todavía deben reconciliarse
```

## Convención `amo.project.json`

Schema inicial:

```text
desarrollamo.project.v1
```

Campos base usados:

- `repository`
- `name`
- `ecosystem`
- `type`
- `lifecycle`
- `visibility`
- `source_of_truth`
- `production_url`
- `related`
- `reviewed_at`
- `notes`

El objetivo es que DAMO, PlataformAMO u otra herramienta de inventario puedan descubrir qué es cada repo sin inferirlo por el nombre.

## Regla de preservación

La limpieza de 2026 **no borra historia ni convierte artificialmente prototipos en productos actuales**. Primero se documenta el estado real; cualquier reactivación futura debe partir de requisitos actuales y validar qué código sigue siendo útil.

## Seguridad pendiente conocida

`PorduccionEmpresa` conserva deuda técnica de credenciales/seed históricos en su código. Está registrada explícitamente en su Issue #1 y no debe tratarse como producción endurecida hasta resolverla.

---

**DesarrollAMO** · una sola visión del ecosistema, aunque los proyectos hayan nacido en momentos y contextos distintos.
