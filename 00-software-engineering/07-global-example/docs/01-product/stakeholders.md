# Stakeholders

| | |
|---|---|
| **Documento** | Análisis de stakeholders |
| **Versión** | 1.0 |
| **Última revisión** | 2026-04-27 |
| **Responsable** | Mariana Restrepo (PO) |
| **Marco** | Mendelow Power-Interest Matrix (1991) + RACI |

---

## 1. Propósito

Identificar a todas las partes interesadas en TaskFlow, clasificarlas por nivel de poder e interés, y definir cómo involucrar a cada una. Las decisiones documentadas aquí dirigen el plan de comunicación y el de gestión del cambio.

---

## 2. Inventario de stakeholders

Identificados durante las entrevistas de descubrimiento (2026-02-18 al 2026-02-26).

### 2.1 Internos al cliente (Lumen Studio)

| ID | Nombre | Rol | Equipo |
|----|--------|-----|--------|
| S01 | Carlos Velandia | CEO | Dirección |
| S02 | Mariana Restrepo | COO / Product Owner | Dirección |
| S03 | Andrea Pulido | Head of Design | Diseño |
| S04 | Diego Restrepo | Head of Engineering interno | Ingeniería |
| S05 | Laura Méndez | Lead Project Manager | Operaciones |
| S06 | Equipo de Project Managers (×8) | Project Managers | Operaciones |
| S07 | Team Leads (×6) | Líderes de equipo | Diseño / Eng / Copy / Motion |
| S08 | Contributors (~60) | Diseñadores, devs, copywriters | Todos los equipos |
| S09 | Felipe Rojas | IT Admin | TI |
| S10 | Ana Quintero | CFO | Finanzas |

### 2.2 Externos al cliente

| ID | Nombre | Rol |
|----|--------|-----|
| S11 | Consultora (nuestro equipo) | Proveedor de implementación |
| S12 | Clientes finales de Lumen | Reciben reportes generados (no usan el sistema) |
| S13 | AWS | Proveedor de infraestructura |

---

## 3. Matriz de Mendelow (Power × Interest)

Clasificación de los 13 stakeholders en los cuatro cuadrantes del modelo.

```
                      INTERÉS →
                  Bajo            Alto
              ┌───────────────┬──────────────────────────┐
              │  MONITOREAR   │     MANTENER INFORMADO   │
         Bajo │               │                          │
              │  S13 AWS      │  S06 Project Managers   │
              │               │  S07 Team Leads          │
   PODER      │               │  S08 Contributors        │
     ↑        │               │  S09 IT Admin            │
              ├───────────────┼──────────────────────────┤
              │   MANTENER    │      ACTORES CLAVE       │
              │   SATISFECHO  │      (gestión cercana)   │
         Alto │               │                          │
              │  S01 CEO      │  S02 PO (COO)            │
              │  S10 CFO      │  S03 Head Design         │
              │  S12 Clientes │  S04 Head Eng            │
              │               │  S05 Lead PM             │
              │               │  S11 Consultora          │
              └───────────────┴──────────────────────────┘
```

### 3.1 Estrategia por cuadrante

| Cuadrante | Estrategia | Cadencia |
|-----------|------------|----------|
| **Actores clave** (alto poder + alto interés) | Gestión cercana, co-decisión, feedback continuo | Semanal o mayor |
| **Mantener satisfecho** (alto poder + bajo interés) | Comunicación ejecutiva, sin saturar con detalle | Quincenal / mensual |
| **Mantener informado** (bajo poder + alto interés) | Información clara y oportuna, canales de feedback | Por sprint |
| **Monitorear** (bajo poder + bajo interés) | Comunicación mínima, monitoreo de cambios | Bajo demanda |

---

## 4. Mapa detallado de stakeholders

### S02 — Mariana Restrepo (Product Owner)

| | |
|---|---|
| **Rol** | COO de Lumen Studio. Product Owner del proyecto. |
| **Cuadrante** | Actor clave |
| **Interés principal** | Visibilidad operativa y reducción del tiempo de reporte. |
| **Influencia** | Decide alcance, prioridades y aceptación de entregables. |
| **Riesgo si se ignora** | Crítico. Sin su validación no hay producto. |
| **Compromiso** | Sync semanal de 60 min, demo cada sprint, decisiones de backlog. |

### S01 — Carlos Velandia (CEO)

| | |
|---|---|
| **Rol** | Sponsor ejecutivo. Aprueba presupuesto y dirección estratégica. |
| **Cuadrante** | Mantener satisfecho |
| **Interés principal** | ROI, alineación estratégica, riesgo financiero. |
| **Influencia** | Veto sobre presupuesto y compromisos contractuales. |
| **Riesgo si se ignora** | Alto. Puede pausar o cancelar el proyecto. |
| **Compromiso** | Steering committee bi-semanal (30 min), reporte ejecutivo mensual. |

### S03 — Andrea Pulido (Head of Design)

| | |
|---|---|
| **Rol** | Lidera el área más numerosa de la agencia. |
| **Cuadrante** | Actor clave |
| **Interés principal** | Que el equipo de diseño adopte la herramienta sin fricción. |
| **Influencia** | Determina la adopción real en su área (≈ 30 personas). |
| **Riesgo si se ignora** | Alto. Si su equipo no adopta, el proyecto fracasa en métricas. |
| **Compromiso** | Demo dedicada cada 2 sprints, participación en pruebas de usabilidad. |

### S04 — Diego Restrepo (Head of Engineering)

| | |
|---|---|
| **Rol** | Lidera ingeniería interna. Será el dueño del sistema post-launch. |
| **Cuadrante** | Actor clave |
| **Interés principal** | Mantenibilidad, calidad técnica, transferencia de conocimiento. |
| **Influencia** | Decisiones técnicas, aprobación de stack y arquitectura. |
| **Riesgo si se ignora** | Crítico para la sostenibilidad post-launch. |
| **Compromiso** | Revisión de ADRs, sesiones de transferencia, acceso al repo desde día 1. |

### S05 — Laura Méndez (Lead PM)

| | |
|---|---|
| **Rol** | Coordina al equipo de Project Managers. Usuario *power*. |
| **Cuadrante** | Actor clave |
| **Interés principal** | Que la herramienta soporte el flujo real de proyectos en curso. |
| **Influencia** | Define el flujo operativo que el sistema debe modelar. |
| **Riesgo si se ignora** | Alto. Es la voz operativa del cliente. |
| **Compromiso** | Refinamiento de backlog quincenal, validación de flujos. |

### S06 — Project Managers (×8)

| | |
|---|---|
| **Rol** | Crean proyectos, asignan, monitorean, reportan. |
| **Cuadrante** | Mantener informado |
| **Interés principal** | Reducir trabajo manual de coordinación. |
| **Compromiso** | Sesión por sprint review, canal Slack dedicado, encuestas mensuales. |

### S07 — Team Leads (×6)

| | |
|---|---|
| **Rol** | Líderes de equipo. Aprueban entregas. |
| **Cuadrante** | Mantener informado |
| **Compromiso** | Demo por sprint, *champions* de adopción dentro de su equipo. |

### S08 — Contributors (~60)

| | |
|---|---|
| **Rol** | Usuarios diarios. Crean y completan tareas. |
| **Cuadrante** | Mantener informado |
| **Compromiso** | Beta interna, encuesta de usabilidad post-onboarding. |

### S09 — IT Admin (Felipe Rojas)

| | |
|---|---|
| **Rol** | Operación de la cuenta AWS de Lumen. |
| **Cuadrante** | Mantener informado |
| **Compromiso** | Acceso a infra desde día 1, walkthrough de runbook. |

### S10 — CFO (Ana Quintero)

| | |
|---|---|
| **Rol** | Aprueba pagos y revisiones presupuestales. |
| **Cuadrante** | Mantener satisfecho |
| **Compromiso** | Reporte de avance presupuestal mensual. |

### S11 — Consultora (nuestro equipo)

| | |
|---|---|
| **Rol** | Implementadores. |
| **Cuadrante** | Actor clave |
| **Compromiso** | Toda la documentación, sprints, retros internas. |

### S12 — Clientes finales de Lumen

| | |
|---|---|
| **Rol** | Reciben reportes PDF generados por el sistema. |
| **Cuadrante** | Mantener satisfecho |
| **Compromiso** | No interactúan con el sistema. La calidad del reporte les afecta indirectamente. |

### S13 — AWS

| | |
|---|---|
| **Rol** | Proveedor de infraestructura. |
| **Cuadrante** | Monitorear |
| **Compromiso** | Suscripción a alertas de servicios usados (RDS, ECS, S3). |

---

## 5. Matriz RACI por entregable mayor

R = Responsable (ejecuta) · A = *Accountable* (rinde cuentas) · C = Consultado · I = Informado

| Entregable | PO (S02) | CEO (S01) | Head Design (S03) | Head Eng (S04) | Lead PM (S05) | Consultora (S11) |
|------------|:---:|:---:|:---:|:---:|:---:|:---:|
| Visión y alcance v1 | A | C | C | C | C | R |
| Backlog priorizado | A | I | C | C | C | R |
| Arquitectura y ADRs | C | I | I | A | I | R |
| Diseño UX | C | I | A | C | C | R |
| Implementación | I | I | I | A | I | R |
| Pruebas de aceptación | A | I | C | C | R | C |
| Despliegue a producción | C | I | I | A | I | R |
| Capacitación a usuarios | A | I | R | C | R | C |
| Operación post-launch | I | I | I | A | C | C |

---

## 6. Plan de comunicación

| Foro | Audiencia | Cadencia | Duración | Objetivo |
|------|-----------|----------|----------|----------|
| **Sync semanal de PO** | S02 + Tech Lead | Viernes 10:00 | 60 min | Decisiones de backlog y bloqueos |
| **Sprint review (demo)** | S02, S03, S04, S05, S07, equipo | Cada 2 semanas, viernes | 60 min | Mostrar incremento; recoger feedback |
| **Sprint planning** | Equipo + S02 | Cada 2 semanas, lunes | 90 min | Compromiso del próximo sprint |
| **Daily** | Equipo de desarrollo | Diario 9:30 | 15 min | Sincronización |
| **Steering committee** | S01, S02, S04, S10, Tech Lead | Cada 2 semanas, jueves | 30 min | Alineación ejecutiva |
| **Demo a contributors** | S06, S07, S08 | Una vez por mes | 45 min | Adopción y feedback amplio |
| **Reporte ejecutivo** | S01, S10 | Mensual (último día hábil) | (escrito) | Avance, presupuesto, riesgos |
| **Canal `#taskflow-feedback`** | Todo Lumen | Continuo | — | Recoger feedback abierto |

---

## 7. Gestión del cambio

Acciones específicas para mitigar el riesgo R1 (baja adopción) identificado en la [visión](vision.md#9-riesgos-estratégicos).

1. **Champions por equipo.** Identificar 1 persona por área que sea early adopter y pueda apoyar a sus pares.
2. **Rollout gradual.** Beta con 2 equipos piloto antes del rollout general.
3. **Capacitación corta.** Sesiones de 30 min por rol (manager, contributor, viewer).
4. **Documentación al alcance.** Guías de usuario disponibles desde el primer login.
5. **Encuesta a 30 días.** Medir satisfacción y ajustar antes del rollout completo.

---

## Referencias

- Mendelow, A. *Stakeholder Mapping* (1991)
- PMBOK 7 — Stakeholder Performance Domain
- [NN/g — Stakeholder Analysis for UX](https://www.nngroup.com/articles/stakeholder-analysis/)
- Documentos relacionados: [Visión](vision.md) · [Personas](personas.md)
