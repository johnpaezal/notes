# Alcance del proyecto

| | |
|---|---|
| **Documento** | Project Scope Statement |
| **Versión** | 1.0 |
| **Última revisión** | 2026-04-27 |
| **Responsable** | Mariana Restrepo (PO) |
| **Aprobado por** | Carlos Velandia (CEO), Mariana Restrepo (COO) |
| **Marcos** | PMBOK 7 (Scope Management) + MoSCoW |
| **Estado** | Aprobado |

---

## 1. Justificación del proyecto

El crecimiento de Lumen Studio (12 → 80 empleados en 3 años) ha hecho que la coordinación basada en hojas de cálculo, Slack y correo deje de escalar, generando pérdida de visibilidad, trabajo duplicado y un costo operativo significativo del equipo ejecutivo. Ver [visión § 4](vision.md#4-problema) para diagnóstico completo.

---

## 2. Objetivos del proyecto

| ID | Objetivo | Métrica |
|----|----------|---------|
| O1 | Centralizar la gestión de tareas en una única plataforma | 100 % de proyectos activos en TaskFlow a 60 días post-launch |
| O2 | Reducir el tiempo de reporte ejecutivo | ≤ 30 min/semana (desde ~6 h actuales) |
| O3 | Garantizar trazabilidad de decisiones | 100 % de cambios con autor y timestamp; retención ≥ 2 años |
| O4 | Lograr adopción interna sostenida | ≥ 70 % de empleados con uso diario activo a 90 días |

---

## 3. Entregables del proyecto

### 3.1 Entregables de producto (software)

| # | Entregable | Criterio de aceptación |
|---|------------|------------------------|
| D01 | Aplicación web TaskFlow v1 desplegada en producción | Pasa pruebas de aceptación + checklist NFR |
| D02 | Importador CSV desde hojas de cálculo Lumen | Migración de ≥ 5 proyectos activos sin pérdida de datos |
| D03 | Reportería ejecutiva (PDF) | Reporte generado en ≤ 10 s, branding aprobado |
| D04 | Integración con Slack (notificaciones salientes) | Mensajes recibidos en canales correctos en ≤ 5 s |

### 3.2 Entregables de documentación

| # | Entregable | Ubicación |
|---|------------|-----------|
| D05 | Documentación técnica completa (este sitio) | `/docs` |
| D06 | Guías de usuario por rol | `/docs/11-user-guides/` |
| D07 | Runbook operativo | `/docs/08-operations/runbook.md` |
| D08 | Architecture Decision Records | `/docs/09-decisions/` |

### 3.3 Entregables de transferencia

| # | Entregable | Criterio de aceptación |
|---|------------|------------------------|
| D09 | Sesiones de capacitación a usuarios (3 sesiones por rol) | Asistencia ≥ 80 %, encuesta ≥ 4/5 |
| D10 | Sesión de transferencia técnica al equipo interno | Equipo S04 puede desplegar y operar sin acompañamiento |
| D11 | Repositorio Git transferido al cliente | Acceso completo otorgado al equipo de S04 |

---

## 4. In-scope (con priorización MoSCoW)

Lo que **sí** se entrega en v1, clasificado por prioridad.

### 4.1 Must have (M) — sin esto no hay v1

| ID | Feature | Justificación |
|----|---------|---------------|
| M01 | Autenticación con email + password | Bloqueador de cualquier acceso |
| M02 | Roles: admin, manager, contributor, viewer | Requisito de seguridad y de adopción organizacional |
| M03 | CRUD de proyectos | Núcleo del producto |
| M04 | CRUD de tareas con asignado, fecha, prioridad, estado | Núcleo del producto |
| M05 | Estados de tarea con máquina de estados | Auditoría y consistencia |
| M06 | Comentarios sobre tareas con menciones | Necesidad confirmada en entrevistas |
| M07 | Notificaciones in-app | Cumplimiento de J1, J2 |
| M08 | Notificaciones por email (digest) | Cumplimiento de J1 fuera de la app |
| M09 | Búsqueda y filtros sobre tareas | Cumplimiento de J2 |
| M10 | Dashboard "Mis tareas" | Cumplimiento de J1 |
| M11 | Dashboard de proyecto | Cumplimiento de J2 |
| M12 | Reporte PDF por proyecto | Cumplimiento de J4 |
| M13 | Bitácora de auditoría | Cumplimiento de J5 + requisito legal |
| M14 | UI en español (es-CO) | Restricción C4 |
| M15 | Importador CSV desde hojas de cálculo Lumen | Cumplimiento de J7 |
| M16 | WCAG 2.1 AA en pantallas críticas | Restricción C5 |
| M17 | Despliegue en AWS São Paulo | Restricción C3 |

### 4.2 Should have (S) — importante pero no bloqueador

| ID | Feature | Justificación |
|----|---------|---------------|
| S01 | Subtareas (hasta 20 por tarea) | Solicitada por 5/8 PMs, pero el flujo funciona sin ella en v0 |
| S02 | Adjuntos en tareas (≤ 25 MB c/u) | Solicitada por equipo de diseño |
| S03 | Vista de carga por persona | Cumplimiento de J3 |
| S04 | Integración saliente con Slack | Reduce fricción pero no es esencial |
| S05 | Plantillas de proyecto | Acelera creación; puede esperar |
| S06 | Exportar reportes a Excel (además de PDF) | Solicitada por finanzas |

### 4.3 Could have (C) — agradables si hay tiempo

| ID | Feature | Justificación |
|----|---------|---------------|
| C01 | Toggle de UI en inglés (en-US) | Útil para staff bilingüe; no urgente |
| C02 | Modo oscuro | Preferencia de usuarios |
| C03 | Atajos de teclado avanzados | Para *power users* |
| C04 | Bulk edit en lista de tareas | Productividad |

### 4.4 Won't have (W) — explícitamente fuera de v1

Ver § 5.

---

## 5. Out-of-scope

Lo que **no** se entrega en v1. Documentar esto evita expectativas mal alineadas.

| # | Funcionalidad | Razón |
|---|---------------|-------|
| W01 | Time tracking y facturación | Manejado por Harvest; ADR-pending para integración futura |
| W02 | Gantt charts y *resource leveling* | Complejidad alta vs. valor incremental para v1 |
| W03 | Cuentas para clientes externos | Riesgo de seguridad y datos; clientes reciben PDFs |
| W04 | App móvil nativa (iOS / Android) | Web responsiva cubre 95 % de los casos en mobile |
| W05 | Edición colaborativa en tiempo real | Complejidad técnica desproporcionada |
| W06 | Integración con Harvest (entrante) | Posible v2; depende de aprendizajes |
| W07 | SSO con Google Workspace | Posible v1.1; no bloqueador para launch |
| W08 | Reportes personalizables por el usuario | Posible v2 |
| W09 | Workflows automáticos (if-then) | Posible v2 |

---

## 6. Suposiciones

Condiciones que asumimos verdaderas. Si alguna no se cumple, el plan debe revisarse.

| # | Suposición | Validador |
|---|------------|-----------|
| A01 | Lumen mantendrá disponible al PO durante toda la duración del proyecto | PO |
| A02 | Los ~80 empleados tienen acceso a navegador moderno (Chrome / Firefox / Edge / Safari ≥ 16) | IT (S09) |
| A03 | Existe cuenta AWS de Lumen con presupuesto operativo aprobado | CFO + IT |
| A04 | Datos a migrar viven en hojas de cálculo accesibles vía exportación CSV | Lead PM |
| A05 | Habrá ≥ 1 *champion* por equipo identificado antes del launch | Heads de área |
| A06 | El equipo interno de S04 aceptará la transferencia técnica al cierre | Head Eng + CEO |

---

## 7. Restricciones

Condiciones límite que el proyecto debe respetar. Trazadas desde [visión § 8](vision.md#8-restricciones).

| # | Restricción | Origen |
|---|-------------|--------|
| C1 | Presupuesto v1: USD 18,000 | CFO |
| C2 | Beta antes del 2026-09-15 | CEO |
| C3 | Datos en AWS sa-east-1 | Política de residencia |
| C4 | UI en español (es-CO) por defecto | UX |
| C5 | Cumplimiento WCAG 2.1 AA | Política inclusión |
| C6 | El stack debe ser mantenible por un equipo interno de 2 devs | Head Eng |

---

## 8. Criterios de aceptación del proyecto

El proyecto se da por **terminado y aceptado** cuando:

1. ✅ Todos los entregables Must (§ 4.1) están en producción y pasan pruebas de aceptación
2. ✅ La documentación (§ 3.2) está completa y publicada
3. ✅ Se completaron las sesiones de capacitación (D09)
4. ✅ Se completó la transferencia técnica al equipo interno (D10)
5. ✅ El repositorio fue transferido al cliente (D11)
6. ✅ El sistema funcionó en producción durante 30 días con uptime ≥ 99.5 %
7. ✅ El PO firmó el documento de aceptación final

---

## 9. Gestión de cambios de alcance

Toda modificación al alcance documentado aquí sigue el proceso de **change request**:

```
Solicitud → Análisis impacto → Aprobación PO → Aprobación CEO (si > USD 1,000) → Actualización de doc
```

| Tipo de cambio | Aprobador |
|----------------|-----------|
| Mover ítem entre Must/Should/Could (sin agregar trabajo) | PO |
| Agregar feature nueva con esfuerzo ≤ 5 días-persona | PO |
| Agregar feature con esfuerzo > 5 días-persona o > USD 1,000 | PO + CEO |
| Cambiar restricción (presupuesto, fecha, región) | CEO |

Las solicitudes de cambio se registran en `docs/12-project-management/change-log.md` (sección agregada cuando aplique).

---

## 10. Resumen ejecutivo (one-pager)

| | |
|---|---|
| **Proyecto** | TaskFlow v1 |
| **Cliente** | Lumen Studio |
| **Sponsor** | Carlos Velandia (CEO) |
| **PO** | Mariana Restrepo (COO) |
| **Inicio** | 2026-02-15 |
| **Beta** | 2026-09-15 |
| **Launch** | 2026-09-30 |
| **Cierre proyecto** | 2026-10-31 |
| **Presupuesto** | USD 18,000 |
| **Equipo** | 1 Tech Lead + 1 Backend + 1 Frontend + 1 QA/SRE part-time |
| **Entregables clave** | App web + docs + capacitación + transferencia |

---

## Aprobación

Las firmas siguientes constituyen aprobación formal del alcance descrito.

| Rol | Nombre | Firma | Fecha |
|-----|--------|-------|-------|
| CEO | Carlos Velandia | ___________ | ___________ |
| COO / PO | Mariana Restrepo | ___________ | ___________ |
| Tech Lead (consultora) | John Páez | ___________ | ___________ |

---

## Referencias

- PMI. *PMBOK Guide* — 7ª edición, dominio Scope
- DSDM Consortium — *MoSCoW Prioritization*
- Documentos relacionados: [Visión](vision.md) · [Stakeholders](stakeholders.md) · [Personas](personas.md) · [Glosario](glossary.md)
