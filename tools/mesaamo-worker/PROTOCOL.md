# MesaAMO Image Intelligence v1.1 · EstructurAMO

Ninguna imagen se implementa ni se finaliza directamente.

Circuito obligatorio:

`BUSCAR → ENTENDER → UBICAR → HACER → VERIFICAR → APRENDER → CERRAR → VOLVER ↻`

Pipeline por fuente:

1. CLAIM — tomar ownership exclusivo de la fuente.
2. DOWNLOAD — obtener media privada.
3. OBSERVE — usar visión/LLM real y describir objetivamente qué muestra.
4. SOURCE_ANALYZED — registrar el resumen mediante `source-analyzed`; descargar no cuenta como analizar.
5. EXTRACT — extraer 0..N capacidades útiles.
6. MAP — consultar MapaAMO por cada capacidad.
7. CLASSIFY — ADAPTAR / YA_EXISTE / NO_APORTA / INVESTIGAR.
8. IMPACT — asignar cada capacidad a 0..N destinos del ecosistema.
9. PLAN — adaptar a arquitectura propia, sin copiar producto/código propietario.
10. ASSIGN — un OWNER por capacidad; REVIEWER/COLLABORATOR permitidos.
11. BUILD — implementar sólo donde aporta valor.
12. VERIFY — tests, evidencia, commit/deploy y comprobación de regresiones.
13. LEARN — actualizar MapaAMO con capacidad, relaciones y evidencia.
14. CLOSE — la fuente sólo queda FINAL cuando existe análisis real y todas sus capacidades derivadas están resueltas, o cuando la disposición terminal demuestra que no hay nada que adaptar.
15. RETURN — volver a BUSCAR. Si no hay trabajo, dormir con 0 llamadas LLM.

Reglas fuertes:

- `download != analysis != done`.
- Una imagen puede producir muchas capacidades y afectar muchos sectores.
- Antes de construir, consultar MapaAMO para evitar duplicados.
- No completar una fuente con notas como “análisis pendiente”.
- No usar LLM para heartbeat, polling, queue, download, hashing o ownership.
- Máximo inicial de 2 trabajos concurrentes por DAMO.

Modelo: `1 imagen -> N capacidades -> N destinos -> N trabajos -> verificación -> aprendizaje`.
