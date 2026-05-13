# Glosario — Lenguaje ubicuo

| | |
|---|---|
| **Documento** | Glosario del dominio (Ubiquitous Language) |
| **Versión** | 1.0 |
| **Última revisión** | 2026-04-27 |
| **Responsable** | Tech Lead + PO |
| **Marco** | Domain-Driven Design (Eric Evans, 2003) |

---

## 1. Propósito

Establecer un **lenguaje único y compartido** entre PO, equipo de desarrollo, QA y usuarios. El mismo término debe significar exactamente lo mismo en:

- Las conversaciones entre el equipo
- La documentación (este sitio)
- El código (clases, métodos, variables, tablas)
- La interfaz de usuario

Si en una entrevista alguien dice "tarjeta", en el código aparece `Card` y en la UI aparece "Tarea", el sistema sufre. **Aquí se define el término canónico** y los sinónimos prohibidos.

> *"Use the model as the backbone of a language. Commit the team to exercising that language relentlessly in all communication within the team and in the code."*  
> — Eric Evans, *Domain-Driven Design*

---

## 2. Cómo leer este glosario

Cada término sigue este formato:

> **Término** *(en inglés en código)* — Definición concisa.  
> **Sinónimos prohibidos**: lista de palabras que no se deben usar.  
> **Notas**: aclaraciones, restricciones, ejemplos.

Términos marcados con 🔑 son entidades del modelo de dominio.

---

## 3. Términos del dominio

### Workspace 🔑

**Workspace** *(`Workspace`)* — Contenedor de máximo nivel que agrupa todos los proyectos, usuarios y datos de **una** organización. v1 soporta un único workspace ("Lumen Studio").  
**Sinónimos prohibidos**: tenant, organización, empresa.  
**Notas**: en v2 podría haber multi-workspace; el modelo ya incluye la columna `workspace_id` por previsión.

### Proyecto 🔑

**Proyecto** *(`Project`)* — Engagement con un cliente externo. Tiene fechas de inicio y fin, un equipo asignado, un *owner* y un estado (`active`, `paused`, `archived`).  
**Sinónimos prohibidos**: cuenta, account, engagement, cliente.  
**Notas**: un proyecto pertenece a un único *workspace*. Contiene tareas. No se puede eliminar; solo archivar.

### Tarea 🔑

**Tarea** *(`Task`)* — Unidad atómica de trabajo. Tiene un único asignado, una fecha de vencimiento y un estado.  
**Sinónimos prohibidos**: tarjeta, card, ticket, issue, ítem, actividad, to-do.  
**Notas**: el reportante (`reporter`) es quien la creó; puede o no ser el mismo asignado.

### Subtarea 🔑

**Subtarea** *(`Subtask`)* — Tarea hija de otra tarea. Tiene los mismos campos que una tarea, **excepto** que no puede tener subtareas propias (no hay anidamiento de segundo nivel).  
**Sinónimos prohibidos**: subitem, hijo, child task, sub-actividad.  
**Notas**: una tarea padre no puede marcarse `done` mientras tenga subtareas pendientes.

### Comentario 🔑

**Comentario** *(`Comment`)* — Mensaje en formato Markdown asociado a una tarea o subtarea. Tiene autor y timestamp.  
**Sinónimos prohibidos**: nota, mensaje, observación.  
**Notas**: editable por el autor durante 5 minutos después de crearlo; luego es inmutable.

### Estado

**Estado** *(`Status`)* — Etapa del ciclo de vida de una tarea. Valores permitidos: `todo`, `in_progress`, `in_review`, `done`, `blocked`, `cancelled`.  
**Sinónimos prohibidos**: status, fase, paso, etapa, columna.  
**Notas**: las transiciones permitidas se rigen por la máquina de estados documentada en [state-machines](../05-design/state-machines.md). Una transición inválida produce HTTP 422.

### Asignado

**Asignado** *(`assignee`)* — Único usuario responsable de completar una tarea.  
**Sinónimos prohibidos**: responsable, owner, encargado, dueño.  
**Notas**: una tarea **siempre** tiene exactamente un asignado. Reasignar es una acción que queda en bitácora.

### Reportante

**Reportante** *(`reporter`)* — Usuario que creó la tarea.  
**Sinónimos prohibidos**: creador, autor, solicitante.  
**Notas**: puede coincidir con el asignado.

### Observador

**Observador** *(`watcher`)* — Usuario que recibe notificaciones de los cambios en una tarea sin ser su asignado.  
**Sinónimos prohibidos**: seguidor, follower, suscriptor, espectador.  
**Notas**: una tarea puede tener múltiples observadores.

### Prioridad

**Prioridad** *(`priority`)* — Nivel de urgencia. Valores: `low`, `medium`, `high`, `urgent`.  
**Sinónimos prohibidos**: importancia, criticidad, severidad.  
**Notas**: la prioridad la fija el asignador (manager o reportante).

### Bitácora de auditoría

**Bitácora de auditoría** *(`AuditLog`)* — Registro inmutable de toda acción de creación, edición o eliminación sobre proyectos, tareas y comentarios.  
**Sinónimos prohibidos**: log, historial, audit trail (en español, sí "bitácora de auditoría").  
**Notas**: cada entrada incluye actor, timestamp, tipo de entidad, ID, diff *antes / después*. Retención mínima: 2 años.

---

## 4. Términos de personas y roles

### Usuario 🔑

**Usuario** *(`User`)* — Persona con cuenta en TaskFlow. Tiene email, nombre completo, foto opcional, un rol y pertenece a uno o más equipos.  
**Sinónimos prohibidos**: cuenta, account, miembro.

### Rol

**Rol** *(`Role`)* — Nivel de permisos del usuario. Valores: `admin`, `manager`, `contributor`, `viewer`.  
**Notas**: matriz completa de permisos en [requirements/functional § FR-002](../02-requirements/functional.md).

### Admin

**Admin** — Usuario con permisos máximos. Gestiona usuarios, equipos, configuración del workspace.  
**Notas**: solo IT Admin (S09) y posiblemente PO tienen este rol.

### Manager

**Manager** — Usuario que crea proyectos y administra tareas dentro de los proyectos donde es *owner*.

### Contributor

**Contributor** — Usuario que ejecuta tareas asignadas. Puede crear y editar **solo sus propias tareas**.

### Viewer

**Viewer** — Usuario de solo lectura. Útil para perfiles ejecutivos que no operan el sistema.

### Equipo 🔑

**Equipo** *(`Team`)* — Agrupación de usuarios (ej. "Diseño", "Engineering"). Un usuario puede pertenecer a múltiples equipos.  
**Sinónimos prohibidos**: grupo, área, departamento.

### Champion

**Champion** — Usuario *early adopter* designado dentro de un equipo para apoyar la adopción de TaskFlow durante el rollout.  
**Notas**: rol social, no técnico. No es un permiso del sistema.

---

## 5. Términos del proceso (Scrum)

### Sprint

**Sprint** — Iteración de **2 semanas** durante la cual el equipo se compromete a un conjunto definido de historias de usuario.  
**Sinónimos prohibidos**: iteración, ciclo.

### Backlog

**Backlog** *(`Backlog`)* — Conjunto de historias de usuario priorizadas, propiedad del PO.  
**Notas**: se distingue *Product Backlog* (todas las historias) de *Sprint Backlog* (las del sprint actual).

### Historia de usuario

**Historia de usuario** *(`UserStory`)* — Descripción corta de una necesidad expresada en formato "Como [rol] quiero [acción] para [valor]".  
**Sinónimos prohibidos**: requerimiento, requisito, feature (los tres existen pero son cosas distintas; ver § 6).

### Definition of Ready (DoR)

**DoR** — Lista de chequeo que debe cumplir una historia para entrar a un sprint. Detalle en [process/definition-of-ready.md](../03-process/definition-of-ready.md).

### Definition of Done (DoD)

**DoD** — Lista de chequeo que debe cumplir una historia para considerarse *terminada*. Detalle en [process/definition-of-done.md](../03-process/definition-of-done.md).

---

## 6. Términos técnicos compartidos

### Requerimiento funcional (FR)

**FR** — Descripción de **qué** debe hacer el sistema. Numerados FR-001, FR-002… en [02-requirements/functional.md](../02-requirements/functional.md).

### Requerimiento no funcional (NFR)

**NFR** — Descripción de **cómo** debe comportarse el sistema (rendimiento, seguridad, etc.). Numerados NFR-001, NFR-002… en [02-requirements/non-functional.md](../02-requirements/non-functional.md).

### Caso de uso

**Caso de uso** *(`UseCase`)* — Flujo paso a paso que describe la interacción entre un actor y el sistema. Numerados UC-001, UC-002…  
**Diferencia con historia de usuario**: la historia es corta y orientada a valor; el caso de uso es detallado y paso a paso.

### ADR

**ADR** — *Architecture Decision Record*. Documento que captura **una** decisión arquitectónica con su contexto, opciones evaluadas y consecuencias. Formato MADR. Ver [09-decisions/](../09-decisions/index.md).

### SLO / SLA / SLI

**SLI** — *Service Level Indicator*. Métrica medible (ej. latencia p95).  
**SLO** — *Service Level Objective*. Meta interna que el equipo se compromete a cumplir (ej. p95 ≤ 300 ms).  
**SLA** — *Service Level Agreement*. Compromiso contractual con el cliente, generalmente más laxo que el SLO.

### PII

**PII** — *Personally Identifiable Information*. Datos que pueden identificar a una persona (nombre completo, email). Su tratamiento sigue lo definido en [seguridad](../08-operations/security-policies.md) (sección agregada en bloque 8).

### RPO / RTO

**RPO** — *Recovery Point Objective*. Máxima pérdida de datos aceptable, medida en tiempo (ej. 1 hora).  
**RTO** — *Recovery Time Objective*. Máximo tiempo aceptable para restaurar el servicio (ej. 4 horas).

---

## 7. Modismos a evitar

Términos coloquiales que circulan en las entrevistas pero **no** deben aparecer en docs ni código:

| Coloquial | Reemplazar por |
|-----------|----------------|
| "tarjeta" | tarea |
| "ticket" | tarea |
| "issue" | tarea (o bug, según contexto) |
| "el board" | dashboard / vista de tareas |
| "el sheet" | hoja de cálculo (legacy) |
| "responsable" | asignado |
| "creador" | reportante |
| "estatus" | estado |
| "dueline" | fecha de vencimiento |

---

## 8. Conformidad

Esta lista es vinculante. Las revisiones de PR deben rechazar identificadores que contradigan el lenguaje ubicuo. La UI debe traducir consistentemente cada término al español de Colombia.

| Inglés (código) | Español (UI) |
|-----------------|--------------|
| `Project` | Proyecto |
| `Task` | Tarea |
| `Subtask` | Subtarea |
| `Comment` | Comentario |
| `Status` | Estado |
| `assignee` | Asignado |
| `reporter` | Reportante |
| `watcher` | Observador |
| `priority` | Prioridad |
| `dueDate` | Fecha de vencimiento |
| `Team` | Equipo |
| `Workspace` | Workspace (no se traduce) |
| `AuditLog` | Bitácora de auditoría |

---

## Referencias

- Evans, E. *Domain-Driven Design: Tackling Complexity in the Heart of Software*, 2003 — capítulo 2 (Ubiquitous Language)
- Fowler, M. [Ubiquitous Language](https://martinfowler.com/bliki/UbiquitousLanguage.html)
- [DDD Reference](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf) — Eric Evans
- Documentos relacionados: [Visión](vision.md) · [Modelo de dominio](../05-design/domain-model.md) (bloque 5)
