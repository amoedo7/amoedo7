# Portafolio MVP · DesarrollAMO

Revisión operativa del ecosistema GitHub. La regla es simple: **un repo no es “MVP” por existir; es MVP cuando resuelve un flujo mínimo de punta a punta y tiene una forma verificable de probarlo.**

## Estados usados

- **OPERABLE** — el flujo mínimo existe y puede probarse.
- **CANDIDATE** — funciona, pero todavía necesita evidencia/release/verificación adicional.
- **EN CONSTRUCCIÓN** — tiene implementación sustancial, pero el circuito mínimo aún no está cerrado.
- **INFRAESTRUCTURA** — no es un producto final; habilita otros MVP.
- **HISTÓRICO** — se conserva como referencia y no debe reactivarse automáticamente.
- **PLACEHOLDER** — no contiene todavía una implementación suficiente.

---

## Núcleo del ecosistema

| Repo | Rol MVP | Estado objetivo |
|---|---|---|
| EscritoriAMO | DesarrollAMO OS: mapa, herramientas, MVP y coordinación local | EN CONSTRUCCIÓN → 1.0 |
| PlataformAMO | Fuente operativa de tareas, personal, clientes, productos, pagos/evidencias | EN CONSTRUCCIÓN |
| IAMO | Agente raíz con memoria, objetivos, IAMOX y sinergias verificables | CANDIDATE |
| RaizAMO | Constitución, ownership y formato universal .amo | INFRAESTRUCTURA |
| CircuitAMO | Control plane para procesos repetibles y gates deterministas | CANDIDATE |
| PasoaPasAMO | Recetas/procedimientos reutilizables | INFRAESTRUCTURA |
| CerebrAMO | Recursos/proveedores + router multi-IA sin inventar métricas | CANDIDATE |
| MesaIAMO | Mesa multi-IA con tareas, mensajes, recibos y capacidades | CANDIDATE |
| SegurAMO | Inventario, sentinel y escaneo defensivo del ecosistema | CANDIDATE |
| DepositAMO | Depósito/refinería local de material con interpretación conservadora | CANDIDATE |
| RankingIAMO | Competencia con ingresos sólo cuando están realmente verificados | CANDIDATE |
| IdeAMO | Incubadora de ideas/prototipos antes de convertirse en producto | INFRAESTRUCTURA |
| DesarrollAMO-Labs | Demos reproducibles y capacidades pequeñas | OPERABLE |

## StoreAMO y distribución

| Repo | Rol MVP | Estado |
|---|---|---|
| StoreAMO | Tienda Android y actualización desde semilla | CANDIDATE |
| StoreAMO-Web | Descubrimiento multiplataforma del catálogo | CANDIDATE |
| StoreAMO-Catalog | Descubrimiento + catálogo machine-readable | OPERABLE |
| StoreAMO-Verify | Evidencia de integridad/identidad antes de “Verified” | OPERABLE |
| StoreAMO-Install | Entrada/recuperación desde cero | OPERABLE |
| desarrollamo/storeamo | Superficie pública de releases verificables | OPERABLE |

## Comercial y operación

| Repo | Rol MVP | Estado |
|---|---|---|
| CobrAMO | Puerta de cobro y referencias trazables | BLOQUEADO: source de producción no reconciliado |
| PagoKitAMO | Recomendar/auditar integraciones de pago | OPERABLE |
| CAMO | Cliente Android de la economía CAMO | EN CONSTRUCCIÓN |
| PidAmo | Pedidos QR para gastronomía | HISTÓRICO funcional |
| PidAmoFrontend | Placeholder histórico | PLACEHOLDER |
| PidAmoBackend | Placeholder histórico | PLACEHOLDER |

## Suite de diagnóstico

| Repo | Pregunta mínima | Estado |
|---|---|---|
| MiDispositivo | ¿Qué dispositivo tengo? | OPERABLE |
| MiRed | ¿Cómo está conectado? | OPERABLE |
| MiSistema | ¿Qué puede ejecutar? | OPERABLE |
| MiWeb | ¿Cómo está una web? | OPERABLE |
| MiArchivos | ¿Qué ocupa y cómo está organizado? | OPERABLE |
| MiAPI | ¿Cómo responde un endpoint? | OPERABLE |
| DiagnosticoAMO | ¿Qué significa todo junto? | OPERABLE |

## Utilidades Android

| Repo | MVP mínimo | Estado |
|---|---|---|
| AlarmAMO | hora + repetición + confirmación/gestión en reloj del sistema | CANDIDATE · construido 2026-09-13 |
| LinternAMO | flash on/off + intermitente + apagado seguro al salir | CANDIDATE · construido 2026-09-13 |
| CalendAMO | calendario mensual + eventos locales persistentes | CANDIDATE · construido 2026-09-13 |
| RelojAMO | reloj digital/analógico offline | CANDIDATE |
| CalculAMO | calculadora + historial local | CANDIDATE |
| CronAMO | cronómetro + vueltas | CANDIDATE |
| GastAMO | ingresos/gastos locales | CANDIDATE |
| HabitAMO | hábitos + rachas locales | CANDIDATE |
| NivelAMO | nivel/inclinómetro + calibración | CANDIDATE |
| PorcentAMO | porcentajes/descuentos/aumentos/propinas | CANDIDATE |
| ContAMO | contadores persistentes | CANDIDATE |
| TemporizAMO | cuenta regresiva con pausa/reinicio/aviso | CANDIDATE |
| DadosAMO | dados múltiples + historial | CANDIDATE |
| SorteAMO | sorteos locales | CANDIDATE |
| ContrasenAMO | generador local de contraseñas | CANDIDATE |
| TareasAMO | tareas locales | CANDIDATE |
| NotasAMO | notas locales | CANDIDATE |
| ConversAMO | conversación/utilidad Android del ecosistema | EN CONSTRUCCIÓN |
| BrujulAMO | brújula local | CANDIDATE |
| GeneralAMO | Generala local-first y compartida | CANDIDATE |

## Infraestructura / identidad pública

- `desarrollamo/branding` — identidad canónica pública.
- `desarrollamo/design-system` — primitivas UI reutilizables.
- `desarrollamo/web` — fuente pública de desarrollamo.com.ar.
- `desarrollamo/desarrollamo` — perfil público corporativo.
- `desarrollamo/.github` — configuración/perfil de cuenta.
- `landings` — infraestructura web y material reutilizable.
- `amoedo7/amoedo7` — mapa público operativo de la cuenta.

Estas piezas no necesitan inventar un “MVP de negocio”: su aceptación es **consistencia, build/check reproducible y fuente de verdad clara**.

## Históricos / experimentales

No deben recibir inversión de MVP hasta que exista una decisión explícita de reactivación:

- AutoDesarrollAMO
- DesarrollAmo
- CriptAmo
- ApostAmo
- Armacabeza
- Eros
- Truco
- Frases
- termuxschool
- HolaMundo.bat
- nada
- INRED
- PorduccionEmpresa

## Regla de cierre

Un MVP pasa a **OPERABLE** sólo si:

1. existe un flujo mínimo completo;
2. no depende de datos ficticios;
3. tiene estado/error visible;
4. persiste lo que deba persistir;
5. puede probarse de forma reproducible;
6. tiene límites y permisos claros;
7. cuando distribuye binarios, conserva hash/evidencia;
8. si maneja dinero, “pagado/verificado” sólo proviene de evidencia real;
9. si usa IA, distingue propuesta de acción ejecutada;
10. su README/MVP.md dice qué está terminado y qué no.

---

**Prioridad actual:** cerrar primero DesarrollAMO OS ↔ PlataformAMO ↔ IAMO/DAMO ↔ móvil; después promover candidatos de StoreAMO según evidencia real.
