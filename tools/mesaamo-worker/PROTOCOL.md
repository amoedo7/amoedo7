# MesaAMO Image Intelligence v1

Ninguna imagen se implementa directamente.

Pipeline obligatorio:

1. OBSERVE — describir objetivamente qué muestra.
2. EXTRACT — extraer 0..N capacidades útiles.
3. MAP — consultar MapaAMO por cada capacidad.
4. CLASSIFY — YA_EXISTE / PARCIAL / NUEVA / NO_APORTA / INVESTIGAR.
5. IMPACT — asignar cada capacidad a 0..N destinos del ecosistema.
6. PLAN — adaptar a la arquitectura propia, sin copiar producto/código propietario.
7. ASSIGN — un OWNER por capacidad; REVIEWER/COLLABORATOR permitidos.
8. BUILD — implementar sólo donde aporta valor.
9. VERIFY — tests, evidencia, commit/deploy.
10. LEARN — actualizar MapaAMO con capacidad, relaciones y evidencia.
11. CLOSE — la imagen fuente sólo queda FINAL cuando todas sus capacidades derivadas están resueltas.

Decisiones terminales: ADAPTAR, YA_EXISTE, NO_APORTA, REJECTED.

Modelo: `1 imagen -> N capacidades -> N destinos -> N trabajos`.
