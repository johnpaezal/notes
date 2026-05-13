# Requisitos funcionales

| | |
|---|---|
| **Documento** | Software Requirements Specification (SRS) — Sección Funcional |
| **Versión** | 1.0 |
| **Última revisión** | 2026-04-27 |
| **Responsable** | Mariana Restrepo (PO) + Tech Lead |
| **Estándar** | ISO/IEC/IEEE 29148:2018 (sucesor de IEEE 830) |
| **Estado** | Aprobado |

---

## 1. Introducción

Este documento especifica los **requisitos funcionales** (FR) de TaskFlow v1, en conformidad con [ISO/IEC/IEEE 29148:2018 — Requirements Engineering](https://www.iso.org/standard/72089.html). Cada requisito describe **qué debe hacer** el sistema, no cómo hacerlo. Los requisitos no funcionales (rendimiento, seguridad, etc.) están en [non-functional.md](non-functional.md).

### 1.1 Convenciones

Cada requisito tiene la siguiente estructura, derivada de IEEE 29148:

| Campo | Descripción |
|-------|-------------|
| **ID** | Identificador único `FR-NNN` |
| **Nombre** | Frase corta |
| **Descripción** | Lo que el sistema debe hacer (en presente, voz activa) |
| **Prioridad** | MUST · SHOULD · COULD (MoSCoW; ver [scope](../01-product/scope.md#4-in-scope-con-priorización-moscow)) |
| **Origen** | Stakeholder o evidencia que lo motivó |
| **Criterio de aceptación** | Condición verificable de cumplimiento |
| **Verificación** | Método (test unitario, integración, E2E, manual, inspección) |
| **Dependencias** | Otros FR/NFR de los que depende |
| **Historia(s) relacionada(s)** | Enlace a `US-NNN` en [user-stories](user-stories.md) |

Las palabras **deberá**, **debe**, **no debe** se usan según RFC 2119 / IEEE 29148: indican obligación normativa.

### 1.2 Alcance

Cubre los 18 requisitos funcionales aprobados para v1. Cualquier requisito adicional debe pasar por el [proceso de control de cambios](../01-product/scope.md#9-gestión-de-cambios-de-alcance).

### 1.3 Trazabilidad

Cada FR está enlazado a su(s) historia(s) de usuario, su(s) caso(s) de uso y su(s) prueba(s). La matriz consolidada está en [traceability.md](traceability.md).

---

## 2. Categorías de requisitos

Los FR se agrupan en módulos del dominio:

| Módulo | Rango |
|--------|-------|
| Autenticación y autorización | FR-001 a FR-003 |
| Proyectos | FR-004 a FR-005 |
| Tareas y subtareas | FR-006 a FR-010 |
| Comentarios | FR-011 |
| Notificaciones | FR-012 |
| Búsqueda y vistas | FR-013 a FR-014 |
| Reportes | FR-015 |
| Auditoría e importación | FR-016 a FR-017 |
| Internacionalización | FR-018 |

---

## 3. Requisitos funcionales detallados

### Módulo: Autenticación y autorización

#### FR-001 — Autenticación con email y contraseña

| | |
|---|---|
| **Prioridad** | MUST |
| **Origen** | Política de seguridad Lumen Studio (S04, S09) |
| **Descripción** | El sistema **deberá** autenticar a los usuarios mediante correo corporativo (`@lumen.studio`) y contraseña, emitiendo un token de sesión válido por 8 horas de inactividad. |
| **Criterios de aceptación** | (1) Credenciales válidas → token JWT con `exp = 8 h`. (2) Tres intentos fallidos en 5 min → bloqueo de 15 min. (3) Sesiones inactivas > 8 h se invalidan. (4) Logout revoca el refresh token. |
| **Verificación** | Integración + manual |
| **Dependencias** | — |
| **Historia(s)** | US-001 |

#### FR-002 — Control de acceso basado en roles (RBAC)

| | |
|---|---|
| **Prioridad** | MUST |
| **Origen** | Lead PM (S05), Head Eng (S04) |
| **Descripción** | El sistema **deberá** aplicar cuatro roles: `admin`, `manager`, `contributor`, `viewer`, con permisos jerárquicos. |
| **Criterios de aceptación** | Matriz rol × acción cumplida (ver § 4 de este documento). Toda acción denegada **deberá** retornar HTTP 403 sin filtrar información. |
| **Verificación** | Integración (test por rol × endpoint) |
| **Dependencias** | FR-001 |
| **Historia(s)** | US-002 |

#### FR-003 — Gestión de cuenta de usuario

| | |
|---|---|
| **Prioridad** | MUST |
| **Origen** | UX (S03), IT Admin (S09) |
| **Descripción** | Un `admin` **deberá** crear, editar, desactivar y reactivar cuentas. Cualquier usuario autenticado **deberá** modificar su propio perfil (nombre, foto, contraseña). |
| **Criterios de aceptación** | (1) Desactivar mantiene el historial pero impide login. (2) El email es único e inmutable tras la creación. (3) Cambio de contraseña requiere contraseña actual. |
| **Verificación** | Integración + manual |
| **Dependencias** | FR-001, FR-002 |
| **Historia(s)** | US-003 |

---

### Módulo: Proyectos

#### FR-004 — Gestión de proyectos

| | |
|---|---|
| **Prioridad** | MUST |
| **Origen** | Lead PM (S05) |
| **Descripción** | Usuarios con rol `manager` o `admin` **deberán** crear, editar, archivar y desarchivar proyectos. |
| **Criterios de aceptación** | Un proyecto tiene: nombre (obligatorio, ≤ 80 chars), nombre del cliente, fecha inicio, fecha fin (≥ inicio), *owner* (manager o admin), estado (`active`/`paused`/`archived`). No se elimina, solo se archiva. |
| **Verificación** | E2E |
| **Dependencias** | FR-002 |
| **Historia(s)** | US-004 |

#### FR-005 — Membresía de proyecto

| | |
|---|---|
| **Prioridad** | MUST |
| **Origen** | Lead PM (S05), Head Design (S03) |
| **Descripción** | El *owner* del proyecto **deberá** agregar y remover miembros. Solo los miembros **deberán** ver el proyecto y sus tareas. |
| **Criterios de aceptación** | (1) Agregar requiere rol mínimo `contributor`. (2) Al remover a un usuario con tareas asignadas, el sistema solicita reasignación obligatoria. (3) Los `admin` siempre tienen acceso a todos los proyectos. |
| **Verificación** | Integración + E2E |
| **Dependencias** | FR-002, FR-004 |
| **Historia(s)** | US-005 |

---

### Módulo: Tareas y subtareas

#### FR-006 — Creación de tareas

| | |
|---|---|
| **Prioridad** | MUST |
| **Origen** | Todas las personas (Laura, Andrés, Sofía) |
| **Descripción** | Cualquier miembro del proyecto con rol mínimo `contributor` **deberá** crear tareas. |
| **Criterios de aceptación** | Una tarea tiene: título (obligatorio, ≤ 200 chars), descripción Markdown (opcional, ≤ 10,000 chars), asignado (obligatorio), fecha de vencimiento (obligatoria), prioridad (`low`/`medium`/`high`/`urgent`), estado inicial `todo`. El `reporter` se registra automáticamente. |
| **Verificación** | E2E |
| **Dependencias** | FR-005 |
| **Historia(s)** | US-006 |

#### FR-007 — Edición y reasignación de tareas

| | |
|---|---|
| **Prioridad** | MUST |
| **Origen** | Lead PM (S05), Andrés (Team Lead) |
| **Descripción** | Un `contributor` **deberá** editar únicamente las tareas que él haya creado o que tenga asignadas. Un `manager` **deberá** editar cualquier tarea de proyectos donde sea *owner*. |
| **Criterios de aceptación** | (1) Cambio de asignado se registra en bitácora con autor + timestamp. (2) Reasignar dispara notificación al nuevo asignado y al anterior. |
| **Verificación** | Integración |
| **Dependencias** | FR-002, FR-006 |
| **Historia(s)** | US-007 |

#### FR-008 — Transiciones de estado

| | |
|---|---|
| **Prioridad** | MUST |
| **Origen** | Lead PM (S05) |
| **Descripción** | El sistema **deberá** validar las transiciones de estado de una tarea según la máquina de estados definida (ver [state-machines](../05-design/state-machines.md), bloque 5). |
| **Criterios de aceptación** | Transiciones inválidas → HTTP 422 con código `INVALID_TRANSITION`. Cada transición produce entrada en bitácora (FR-016). |
| **Verificación** | Unitario (state machine) + integración |
| **Dependencias** | FR-006, FR-016 |
| **Historia(s)** | US-008 |

#### FR-009 — Subtareas

| | |
|---|---|
| **Prioridad** | SHOULD |
| **Origen** | 5 de 8 PMs en entrevistas |
| **Descripción** | Una tarea **podrá** contener hasta 20 subtareas. Las subtareas tienen los mismos campos que las tareas pero **no** pueden tener subtareas propias. |
| **Criterios de aceptación** | (1) Crear subtarea #21 → HTTP 422. (2) La tarea padre no se marca `done` mientras existan subtareas en estado distinto a `done` o `cancelled`. (3) Eliminar (archivar) la tarea padre archiva todas sus subtareas. |
| **Verificación** | Integración |
| **Dependencias** | FR-006 |
| **Historia(s)** | US-009 |

#### FR-010 — Adjuntos en tareas

| | |
|---|---|
| **Prioridad** | SHOULD |
| **Origen** | Equipo de diseño (S03) |
| **Descripción** | Un usuario **podrá** adjuntar archivos a una tarea, máximo 25 MB por archivo y 10 archivos por tarea. |
| **Criterios de aceptación** | (1) Tipos permitidos: imágenes (PNG, JPG, WEBP), documentos (PDF, DOCX, XLSX), texto. Otros → HTTP 415. (2) Almacenamiento en S3 cifrado en reposo. (3) URL firmada con expiración de 15 min. |
| **Verificación** | Integración + seguridad |
| **Dependencias** | FR-006, NFR-005 |
| **Historia(s)** | US-010 |

---

### Módulo: Comentarios

#### FR-011 — Comentarios en tareas

| | |
|---|---|
| **Prioridad** | MUST |
| **Origen** | Andrés (Team Lead), Lead PM (S05) |
| **Descripción** | Cualquier miembro del proyecto **deberá** comentar tareas usando Markdown, con menciones `@usuario`. |
| **Criterios de aceptación** | (1) Comentario editable por su autor durante 5 min; luego inmutable. (2) Mención dispara notificación al usuario mencionado (FR-012). (3) Markdown soportado: negrita, cursiva, listas, links, código inline. (4) Sanitización contra XSS. |
| **Verificación** | Integración + seguridad |
| **Dependencias** | FR-005, FR-012 |
| **Historia(s)** | US-011 |

---

### Módulo: Notificaciones

#### FR-012 — Sistema de notificaciones

| | |
|---|---|
| **Prioridad** | MUST |
| **Origen** | Sofía (Contributor), Laura (PM) |
| **Descripción** | El sistema **deberá** notificar a los usuarios sobre: asignación, mención, cambio de estado en tarea propia, comentario en tarea propia, fecha de vencimiento en ≤ 24 h. |
| **Criterios de aceptación** | (1) Notificación in-app aparece en ≤ 5 s. (2) Email enviado en ≤ 5 min para eventos críticos (asignación, mención). (3) *Digest* diario de eventos no críticos a las 17:00 hora local. (4) Cada usuario configura preferencias por canal. |
| **Verificación** | Integración + observabilidad |
| **Dependencias** | FR-006, FR-011 |
| **Historia(s)** | US-012 |

---

### Módulo: Búsqueda y vistas

#### FR-013 — Búsqueda de tareas

| | |
|---|---|
| **Prioridad** | MUST |
| **Origen** | Laura (PM), Mariana (Exec) |
| **Descripción** | El usuario **deberá** buscar tareas por título, descripción, asignado, proyecto, estado, prioridad y rango de fechas. |
| **Criterios de aceptación** | (1) Búsqueda *full-text* sobre título y descripción. (2) Filtros combinables (AND lógico). (3) Resultados paginados (50 por página). (4) Latencia ≤ 500 ms p95 para 50,000 tareas (NFR-002). |
| **Verificación** | Integración + performance |
| **Dependencias** | FR-006, NFR-002 |
| **Historia(s)** | US-013 |

#### FR-014 — Vistas predefinidas (dashboards)

| | |
|---|---|
| **Prioridad** | MUST |
| **Origen** | Sofía (J1), Laura (J2), Mariana (visión ejecutiva) |
| **Descripción** | El sistema **deberá** ofrecer las siguientes vistas: (a) "Mis tareas" — tareas asignadas al usuario activo agrupadas por estado y orden por fecha. (b) "Proyecto" — tareas del proyecto agrupadas por estado (vista kanban). (c) "Ejecutiva" — solo `admin`/`manager`: portafolio con KPIs por proyecto. |
| **Criterios de aceptación** | Cada vista carga en ≤ 2.5 s (NFR-002). Filtros básicos sin recargar página. |
| **Verificación** | E2E |
| **Dependencias** | FR-013 |
| **Historia(s)** | US-014 |

---

### Módulo: Reportes

#### FR-015 — Reporte PDF de proyecto

| | |
|---|---|
| **Prioridad** | MUST |
| **Origen** | Mariana (COO), Lead PM |
| **Descripción** | Un usuario con rol `manager` o `admin` **deberá** generar un reporte PDF para cualquier proyecto activo. |
| **Criterios de aceptación** | (1) Generación en ≤ 10 s para proyectos con ≤ 500 tareas. (2) Branding Lumen Studio (logo, colores). (3) Contenido: tasa de completitud, bloqueos, próximos vencimientos (≤ 14 días), distribución por asignado. (4) Idioma según preferencia del usuario. |
| **Verificación** | E2E + manual QA |
| **Dependencias** | FR-014, NFR-007 |
| **Historia(s)** | US-015 |

---

### Módulo: Auditoría e importación

#### FR-016 — Bitácora de auditoría

| | |
|---|---|
| **Prioridad** | MUST |
| **Origen** | CEO (S01), legal Lumen, J5 (reconstruir historial) |
| **Descripción** | El sistema **deberá** registrar toda creación, edición y eliminación sobre proyectos, tareas y comentarios. |
| **Criterios de aceptación** | Cada entrada incluye: actor, timestamp UTC, tipo de entidad, ID, *diff* antes/después en JSON. Solo `admin` consulta. Retención ≥ 2 años (NFR-005). |
| **Verificación** | Integración |
| **Dependencias** | — |
| **Historia(s)** | US-016 |

#### FR-017 — Importación masiva desde CSV

| | |
|---|---|
| **Prioridad** | SHOULD |
| **Origen** | Lead PM (S05), J7 |
| **Descripción** | Un `admin` **deberá** importar tareas desde un archivo CSV con esquema documentado. |
| **Criterios de aceptación** | (1) 5,000 filas en ≤ 60 s. (2) Errores de validación reportados por fila sin abortar. (3) Reporte final con conteo de éxitos/errores y archivo de errores descargable. (4) Importaciones quedan en bitácora. |
| **Verificación** | Integración |
| **Dependencias** | FR-006, FR-016 |
| **Historia(s)** | US-017 |

---

### Módulo: Internacionalización

#### FR-018 — Interfaz en español de Colombia

| | |
|---|---|
| **Prioridad** | MUST |
| **Origen** | Restricción C4 |
| **Descripción** | La interfaz de usuario **deberá** estar disponible en español (`es-CO`). |
| **Criterios de aceptación** | (1) 100 % de cadenas externalizadas en archivos de traducción. (2) Sin páginas con idioma mezclado. (3) Formatos de fecha y número siguen `es-CO`. (4) Mensajes de error del backend traducidos. |
| **Verificación** | Manual QA + linter i18n |
| **Dependencias** | — |
| **Historia(s)** | US-018 |

---

## 4. Matriz de permisos rol × acción

Implementación operativa de FR-002. Las celdas marcan acciones **permitidas**.

| Acción | viewer | contributor | manager | admin |
|--------|:---:|:---:|:---:|:---:|
| Ver proyectos donde es miembro | ✓ | ✓ | ✓ | ✓ |
| Ver todos los proyectos del workspace | — | — | — | ✓ |
| Crear proyecto | — | — | ✓ | ✓ |
| Editar proyecto del que es *owner* | — | — | ✓ | ✓ |
| Archivar proyecto | — | — | ✓ (solo owner) | ✓ |
| Crear tarea en proyecto donde es miembro | — | ✓ | ✓ | ✓ |
| Editar tarea propia (creada o asignada) | — | ✓ | ✓ | ✓ |
| Editar cualquier tarea del proyecto | — | — | ✓ (solo owner) | ✓ |
| Comentar tarea visible | ✓ | ✓ | ✓ | ✓ |
| Editar comentario propio (≤ 5 min) | ✓ | ✓ | ✓ | ✓ |
| Generar reporte PDF | — | — | ✓ | ✓ |
| Importar CSV | — | — | — | ✓ |
| Ver bitácora de auditoría | — | — | — | ✓ |
| Gestionar usuarios y roles | — | — | — | ✓ |

---

## 5. Reglas de negocio

Reglas transversales que aplican a múltiples requisitos.

| ID | Regla |
|----|-------|
| BR-01 | Una tarea siempre tiene exactamente un asignado (no se permite *unassigned*). |
| BR-02 | Las fechas se almacenan en UTC y se muestran en la zona del usuario (default `America/Bogota`). |
| BR-03 | Un email solo puede asociarse a una cuenta activa a la vez. |
| BR-04 | Una contraseña debe tener ≥ 12 caracteres, con al menos una mayúscula, un dígito y un símbolo. |
| BR-05 | Un proyecto no se elimina, solo se archiva. Las tareas archivadas son consultables pero no editables. |
| BR-06 | El idioma efectivo de un usuario es: `user.locale` > `workspace.default_locale` > `es-CO`. |

---

## 6. Conformidad con ISO/IEC/IEEE 29148:2018

Cada FR cumple los atributos exigidos por el estándar:

| Atributo | Cumplimiento |
|----------|--------------|
| **Necesario** | Cada FR está trazado a un origen (stakeholder o evidencia) |
| **Apropiado** | Granularidad uniforme (entre US y reglas) |
| **Inequívoco** | Lenguaje normativo (RFC 2119) y términos del [glosario](../01-product/glossary.md) |
| **Completo** | Estructura uniforme para todos los FR |
| **Singular** | Un FR = una funcionalidad (sin "y/o" abusivos) |
| **Verificable** | Criterios de aceptación medibles y método de verificación explícito |
| **Correcto** | Validado con PO el 2026-04-25 |
| **Conforme** | Identificadores únicos (`FR-NNN`) y referencias cruzadas |

---

## Referencias

- ISO/IEC/IEEE 29148:2018 — *Systems and software engineering — Life cycle processes — Requirements engineering*
- IEEE 830-1998 — *Recommended Practice for Software Requirements Specifications* (precedente)
- RFC 2119 — *Key words for use in RFCs to Indicate Requirement Levels*
- DSDM Consortium — MoSCoW Prioritization
- Documentos relacionados: [Alcance](../01-product/scope.md) · [Historias de usuario](user-stories.md) · [Casos de uso](use-cases.md) · [No funcionales](non-functional.md) · [Trazabilidad](traceability.md)
