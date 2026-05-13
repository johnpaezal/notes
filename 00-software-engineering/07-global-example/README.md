# TaskFlow

> Plataforma interna de gestión de tareas para **Lumen Studio**.

[![Status](https://img.shields.io/badge/status-in%20development-yellow)]()
[![Docs](https://img.shields.io/badge/docs-mkdocs--material-blue)]()
[![License](https://img.shields.io/badge/license-Proprietary-lightgrey)]()

TaskFlow reemplaza el flujo basado en hojas de cálculo que utilizan ~80 empleados de 6 equipos creativos para coordinar el portafolio de proyectos de la agencia. Centraliza la asignación, el seguimiento y el reporte del trabajo.

---

## Documentación

La documentación completa del proyecto vive en [`docs/`](./docs/) y se publica como un sitio estático con [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

```bash
pip install mkdocs-material mkdocs-mermaid2-plugin
mkdocs serve
```

Abrir <http://localhost:8000>.

| Sección | Audiencia | Propósito |
|--------|-----------|-----------|
| [01 — Product](docs/01-product/) | Cliente, PO | Visión, stakeholders, alcance, glosario |
| [02 — Requirements](docs/02-requirements/) | Cliente, dev, QA | Requisitos funcionales y no-funcionales, historias |
| [03 — Process](docs/03-process/) | Equipo | Metodología (Scrum), DoR / DoD |
| [04 — Architecture](docs/04-architecture/) | Dev, arquitecto | arc42 + C4 |
| [05 — Design](docs/05-design/) | Dev | Modelo de dominio, ER, diagramas de secuencia |
| [06 — API](docs/06-api/) | Dev, integrador | Referencia REST |
| [07 — Quality](docs/07-quality/) | QA, dev | Estrategia de pruebas, cobertura |
| [08 — Operations](docs/08-operations/) | SRE, DevOps | Despliegue, observabilidad, runbook |
| [09 — Decisions](docs/09-decisions/) | Equipo | ADRs (Architecture Decision Records) |
| [10 — Onboarding](docs/10-onboarding/) | Dev nuevo | Setup local, estándares, flujo Git |
| [11 — User guides](docs/11-user-guides/) | Usuario final | Cómo usar la plataforma |

---

## Hechos del proyecto

| | |
|---|---|
| **Cliente** | Lumen Studio (agencia creativa, Bogotá) |
| **Usuarios objetivo** | ~80 empleados, 6 equipos |
| **Inicio** | 2026-02-15 |
| **Beta objetivo** | 2026-Q3 |
| **Stack** | Python 3.12 · FastAPI · PostgreSQL 16 · React 18 · AWS (sa-east-1) |
| **Repositorio** | `github.com/lumen-studio/taskflow` |

---

## Equipo

| Rol | Persona | Contacto |
|-----|---------|----------|
| Product Owner | Mariana Restrepo (Lumen) | mariana@lumen.studio |
| Tech Lead | John Páez | jpaez@consultora.co |
| Backend | (TBD) | |
| Frontend | (TBD) | |
| QA / SRE | (TBD) | |

---

## Licencia

Proyecto privado. Todos los derechos reservados © 2026 Lumen Studio.
