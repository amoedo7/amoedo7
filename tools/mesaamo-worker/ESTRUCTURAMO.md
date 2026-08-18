# EstructurAMO v1

EstructurAMO es la estructura organizacional y el circuito de evolución continua de DesarrollAMO.

No es otra IA ni otra app. MesaAMO es su tablero visible; MapaAMO es su índice; DAMO y otros participantes son trabajadores.

## Ciclo

`BUSCAR → ENTENDER → UBICAR → HACER → VERIFICAR → APRENDER → CERRAR → VOLVER ↻`

- BUSCAR: detectar cola, ideas, imágenes, tareas y cambios.
- ENTENDER: observar la fuente y convertirla en información estructurada.
- UBICAR: consultar MapaAMO y decidir qué oficinas/sistemas impacta.
- HACER: asignar ownership e implementar.
- VERIFICAR: tests, seguridad, regresiones y evidencia.
- APRENDER: actualizar MapaAMO y relaciones.
- CERRAR: resolver fuente/capacidades con evidencia.
- VOLVER: regresar a BUSCAR.

Cuando no existe trabajo el circuito queda dormido: polling/heartbeat deterministas, 0 llamadas LLM.

## Organización inicial

- EstructurAMO — control plane.
- DesarrolloAMO — arquitectura, implementación, tests e integración.
- SecurityAMO — seguridad, secretos, hardening y auditoría.
- InfraAMO — infraestructura, red, deploy y resiliencia.
- OperAMO — supervisión, colas, recovery y continuidad.
- WebAMO — web, UX/UI y accesibilidad.
- DatabaseAMO — PostgreSQL, Supabase, migraciones y datos.
- MarketingAMO, ContaduríaAMO e InvestigAMO — oficinas ya existentes del ecosistema.

Los agentes tienen una oficina primaria, capacidades y límites de concurrencia. Una unidad de trabajo tiene un solo OWNER y puede tener revisores/colaboradores.

## Principio

El objetivo no es tener más agentes, sino aumentar capacidad sin aumentar colisiones ni gasto en estado ocioso.
