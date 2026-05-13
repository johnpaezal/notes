# Visión del producto

| | |
|---|---|
| **Documento** | Visión de producto |
| **Versión** | 1.0 |
| **Última revisión** | 2026-04-27 |
| **Responsable** | Mariana Restrepo (Product Owner) |
| **Aprobado por** | Carlos Velandia (CEO, Lumen Studio) |
| **Estado** | Aprobado |

---

## 1. Visión

> **Que cualquier persona en Lumen Studio pueda saber qué le toca hoy, en qué va su equipo y cómo avanzan los proyectos activos — sin tener que preguntarle a nadie.**

Esta es la afirmación central del producto. Todo lo que se construya debe poder justificarse contra ella.

---

## 2. Posicionamiento (Geoffrey Moore)

Plantilla *elevator pitch* tomada de *Crossing the Chasm*.

> **Para** los equipos creativos, de cuenta y de operaciones de Lumen Studio  
> **que** necesitan coordinar el trabajo de decenas de proyectos simultáneos sin perder visibilidad ni duplicar esfuerzos,  
> **TaskFlow** es **una plataforma interna de gestión de tareas**  
> **que** centraliza la asignación, el seguimiento y el reporte del trabajo en un único sistema operado por la propia agencia,  
> **a diferencia** de hojas de cálculo compartidas, hilos de Slack y herramientas SaaS genéricas que no se ajustan al flujo creativo de la agencia,  
> **nuestro producto** ofrece un modelo de datos hecho a medida, reportes ejecutivos automáticos y reside en infraestructura propia con datos en Brasil (cumplimiento de residencia de datos).

---

## 3. Vision Board (Roman Pichler)

Modelo visual usado para alinear visión, audiencia, necesidades, producto y objetivos de negocio.

### 3.1 Visión

Eliminar la fricción operativa entre los equipos de Lumen Studio para que el tiempo del personal se invierta en trabajo creativo, no en coordinación.

### 3.2 Audiencia objetivo

| Segmento | Volumen | Descripción |
|----------|---------|-------------|
| Project Managers | 8 | Coordinan portafolio de proyectos, asignan trabajo, reportan al cliente |
| Team Leads | 6 | Lideran equipos creativos (diseño, copy, dev, motion) |
| Contributors | ~60 | Diseñadores, copywriters, desarrolladores y especialistas |
| Executives | 2 | CEO y COO con necesidad de visibilidad consolidada |

### 3.3 Necesidades

Lo que la audiencia necesita y hoy no obtiene:

- **Visibilidad inmediata** del estado de cualquier tarea sin tener que preguntar
- **Asignación inequívoca** — una tarea, un responsable, una fecha
- **Historial auditable** de cambios de estado, decisiones y comentarios
- **Reportes ejecutivos** generados en segundos, no en horas
- **Carga de trabajo balanceada** visible por equipo y persona

### 3.4 Producto

Aplicación web responsiva (no app nativa en v1) construida sobre stack moderno, alojada en AWS São Paulo, con UI en español. Características clave de v1:

- Gestión de proyectos, tareas y subtareas
- Asignación con reglas claras (1 tarea = 1 asignado = 1 fecha)
- Comentarios con menciones, notificaciones in-app y email
- Dashboard ejecutivo y reportes PDF
- Bitácora de auditoría completa
- Búsqueda y filtros

### 3.5 Objetivos de negocio

Lo que la organización gana al construir este producto.

| Objetivo de negocio | Beneficio cuantificado |
|--------------------|------------------------|
| Reducir el tiempo de reporte semanal del COO | de 6 h/semana a ≤ 30 min/semana |
| Eliminar trabajo duplicado entre equipos | ≥ 90 % de incidentes de duplicación evitados |
| Aumentar la confianza del cliente con reportes consistentes | NPS de cliente +10 puntos en 6 meses |
| Reducir el ruido en Slack `#projects` por preguntas operativas | −50 % de mensajes "¿dónde va X?" |

---

## 4. Problema

### 4.1 Contexto

Lumen Studio creció de 12 a 80 empleados en tres años. La coordinación operativa que funcionó cuando eran 12 personas no escaló:

- Cada equipo lleva su propio Google Sheet, sin formato común
- Los cambios de estado se anuncian en Slack y se pierden en el ruido
- Los reportes a clientes se arman manualmente cada semana
- No hay rastro auditable de quién aprobó qué, cuándo

### 4.2 Síntomas observados

Datos recogidos durante el descubrimiento (2026-02-15 a 2026-02-26):

| Síntoma | Evidencia |
|---------|-----------|
| Pérdida de visibilidad | 6 de 8 PMs reportan tener que preguntar por Slack para conocer el estado de tareas críticas |
| Duplicación de trabajo | 4 incidentes documentados en el último trimestre |
| Costo de reporting | El COO dedica 5–7 horas semanales a consolidar reportes |
| Falta de auditoría | Cliente Q1 escaló reclamo sin que se pudiera reconstruir el historial de aprobaciones |

### 4.3 Por qué ahora

- **Riesgo operativo creciente**: el costo de no actuar aumenta con cada cliente nuevo
- **Ventana de presupuesto**: el CFO aprobó la inversión para el ciclo fiscal actual
- **Disponibilidad de equipo interno**: hay capacidad para acompañar el rollout en Q3

---

## 5. Métricas de éxito

El proyecto se considera exitoso a 90 días post-lanzamiento si se cumplen estas condiciones, todas medibles.

| # | Métrica | Línea base (mar 2026) | Meta (90 días post-launch) | Medición |
|---|---------|----------------------|---------------------------|----------|
| M1 | Adopción diaria | 0 % | ≥ 70 % de empleados con ≥ 1 sesión por día hábil | Analytics |
| M2 | Tiempo de reporte semanal del COO | 6 h | ≤ 30 min | Encuesta + cronómetro |
| M3 | Mensajes "¿dónde va X?" en `#projects` | Baseline 2026-03 | −50 % | Slack analytics |
| M4 | Tareas sin asignado | N/A | < 2 % del total | Query DB |
| M5 | Incidentes de pérdida de datos | N/A | 0 | Bitácora ops |
| M6 | NPS interno (empleados) | N/A | ≥ +30 | Encuesta trimestral |

---

## 6. Principios de producto

Heurísticas que guían las decisiones cuando hay duda.

1. **Una tarea, un responsable.** Nunca diluir la responsabilidad.
2. **Defaults sensatos.** El 80 % de los flujos no debe requerir configuración.
3. **Visible por defecto.** El trabajo se asume público dentro de la agencia, salvo proyectos confidenciales.
4. **Sin duplicación.** Una tarea vive en un solo lugar; lo demás referencia.
5. **Audit-first.** Toda acción crítica deja rastro inmutable.

---

## 7. No-objetivos (lo que TaskFlow **no** será en v1)

Para evitar *scope creep*, se documenta explícitamente:

- ❌ No reemplazará Slack como herramienta de comunicación
- ❌ No incluirá *time tracking* ni facturación (eso lo hace Harvest)
- ❌ No tendrá usuarios externos (clientes reciben PDFs)
- ❌ No tendrá Gantt ni *resource leveling*
- ❌ No tendrá app móvil nativa (web responsiva)
- ❌ No incluirá edición colaborativa en tiempo real

Los no-objetivos pueden reevaluarse para v2 según los aprendizajes de v1.

---

## 8. Restricciones

| # | Restricción | Origen |
|---|-------------|--------|
| C1 | Presupuesto v1: USD 18,000 | CFO Lumen Studio |
| C2 | Beta antes del 2026-09-15 (onboarding Q4) | CEO Lumen Studio |
| C3 | Datos en AWS región São Paulo (sa-east-1) | Política de residencia de datos |
| C4 | UI en español (es-CO); inglés como toggle futuro | UX Lumen Studio |
| C5 | Cumplimiento WCAG 2.1 AA | Política interna de inclusión |

---

## 9. Riesgos estratégicos

| # | Riesgo | Probabilidad | Impacto | Mitigación |
|---|--------|--------------|---------|------------|
| R1 | Baja adopción por resistencia al cambio | Media | Alto | Plan de change management; champions por equipo; rollout gradual |
| R2 | Sobrecosto del alcance original | Media | Alto | Backlog priorizado MoSCoW; revisión quincenal con PO |
| R3 | Migración fallida desde Google Sheets | Baja | Medio | Importador CSV con validación por fila (FR-012) |
| R4 | Dependencia de un solo proveedor cloud | Baja | Bajo | Stack portable (PostgreSQL, contenedores); ADR de salida |

---

## 10. Roadmap de alto nivel

| Fase | Periodo | Entregable principal |
|------|---------|----------------------|
| Discovery | 2026-02-15 → 2026-02-28 | Vision, stakeholders, alcance firmado |
| Diseño + arquitectura | 2026-03-01 → 2026-03-31 | C4, ADRs, modelo de datos |
| Build sprint 0–6 | 2026-04-01 → 2026-08-15 | MVP funcional |
| Beta interna | 2026-08-15 → 2026-09-15 | Beta con 2 equipos piloto |
| Launch | 2026-09-15 → 2026-09-30 | Rollout a los 6 equipos |
| Post-launch | 2026-10-01 → 2026-12-31 | Estabilización + métricas M1–M6 |

---

## Referencias

- Moore, G. *Crossing the Chasm* — plantilla de posicionamiento
- Pichler, R. [Product Vision Board](https://www.romanpichler.com/blog/double-vision-how-to-capture-the-product-vision/)
- Documentos relacionados: [Stakeholders](stakeholders.md) · [Personas](personas.md) · [Alcance](scope.md)
