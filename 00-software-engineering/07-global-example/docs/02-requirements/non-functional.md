# Requisitos no funcionales

| | |
|---|---|
| **Documento** | SRS — Sección No Funcional |
| **Versión** | 1.0 |
| **Última revisión** | 2026-04-27 |
| **Responsable** | Tech Lead + PO |
| **Estándares** | ISO/IEC 25010:2011 (modelo de calidad) + ISO/IEC/IEEE 29148:2018 |
| **Estado** | Aprobado |

---

## 1. Introducción

Este documento define los **requisitos no funcionales** (NFR) de TaskFlow v1, organizados según las ocho características de calidad de **ISO/IEC 25010:2011** (también conocido como SQuaRE — *Software product Quality Requirements and Evaluation*).

A diferencia de los [funcionales](functional.md), los NFR describen **cómo se comporta** el sistema: qué tan rápido, seguro, mantenible, accesible, etc. Cada NFR es:

- **Medible** — definido con un valor objetivo concreto
- **Verificable** — método explícito de comprobación
- **Trazable** — asociado a un origen (restricción, stakeholder, regulación)

### 1.1 Modelo ISO/IEC 25010 — ocho características

```
                    ┌──────────────────┐
                    │ Software Product │
                    │     Quality      │
                    └────────┬─────────┘
        ┌─────────┬──────────┼──────────┬──────────┐
        ▼         ▼          ▼          ▼          ▼
  Functional  Performance  Compatib.  Usability  Reliability
  Suitability  Efficiency
        ▼         ▼          ▼          ▼          ▼
                Security  Maintain.   Portability
```

| # | Característica | Cubre |
|---|---------------|-------|
| 1 | Functional Suitability | Completitud, exactitud, idoneidad funcional |
| 2 | Performance Efficiency | Tiempo de respuesta, uso de recursos, capacidad |
| 3 | Compatibility | Interoperabilidad, coexistencia |
| 4 | Usability | Aprendibilidad, accesibilidad, estética |
| 5 | Reliability | Disponibilidad, tolerancia a fallos, recuperabilidad |
| 6 | Security | Confidencialidad, integridad, autenticidad, no-repudio |
| 7 | Maintainability | Modularidad, reutilización, modificabilidad, testeabilidad |
| 8 | Portability | Adaptabilidad, instalabilidad, reemplazabilidad |

---

## 2. NFR detallados

### 2.1 Performance Efficiency (Rendimiento)

#### NFR-001 — Tiempo de respuesta de la API

| | |
|---|---|
| **Subcaracterística** | Time behaviour |
| **Descripción** | Latencia de respuesta del API REST bajo carga normal. |
| **Métrica** | p50, p95, p99 (ms) |
| **Objetivo** | p95 ≤ 300 ms · p99 ≤ 800 ms · p50 ≤ 100 ms |
| **Excluye** | Generación de reporte PDF (NFR-003), importación CSV (NFR-004) |
| **Carga asumida** | 50 RPS sostenidos, 200 RPS pico |
| **Verificación** | Pruebas de carga con `k6` en staging; observabilidad en prod |
| **Origen** | Restricción técnica / experiencia de usuario |

#### NFR-002 — Tiempo de carga de la UI

| | |
|---|---|
| **Subcaracterística** | Time behaviour |
| **Descripción** | Carga inicial de la aplicación web. |
| **Métrica** | Largest Contentful Paint (LCP) |
| **Objetivo** | LCP ≤ 2.5 s sobre conexión 4G simulada (Chrome DevTools throttling: *Slow 4G*) |
| **Verificación** | Lighthouse CI en cada PR; RUM en prod |
| **Origen** | Core Web Vitals / NN/g |

#### NFR-003 — Generación de reportes

| | |
|---|---|
| **Subcaracterística** | Time behaviour |
| **Descripción** | Tiempo para generar un reporte PDF de un proyecto. |
| **Métrica** | Tiempo de extremo a extremo (s) |
| **Objetivo** | ≤ 10 s para proyectos con ≤ 500 tareas |
| **Verificación** | Test de integración + monitoreo en prod |
| **Origen** | Mariana (Exec), métrica M2 de la [visión](../01-product/vision.md#5-métricas-de-éxito) |

#### NFR-004 — Importación CSV

| | |
|---|---|
| **Subcaracterística** | Time behaviour |
| **Descripción** | Procesamiento de archivos CSV para importación masiva. |
| **Métrica** | Filas procesadas / segundo |
| **Objetivo** | 5,000 filas en ≤ 60 s (≥ 83 filas/s) |
| **Verificación** | Test de integración con dataset real |
| **Origen** | FR-017, J7 |

#### NFR-005 — Capacidad

| | |
|---|---|
| **Subcaracterística** | Capacity |
| **Descripción** | Volumen de datos soportado sin degradación. |
| **Objetivo año 1** | 80 usuarios concurrentes · 30 proyectos activos · 15,000 tareas · 50,000 comentarios |
| **Objetivo año 3** | 3× los valores anteriores sin cambio arquitectónico (escalado vertical aceptable) |
| **Verificación** | Pruebas de capacidad trimestrales |
| **Origen** | Crecimiento proyectado de Lumen Studio |

---

### 2.2 Reliability (Confiabilidad)

#### NFR-006 — Disponibilidad

| | |
|---|---|
| **Subcaracterística** | Availability |
| **Descripción** | Disponibilidad mensual del servicio. |
| **SLO** | 99.5 % mensual (excluyendo ventanas de mantenimiento anunciadas con ≥ 48 h) |
| **Presupuesto de error** | ≤ 3 h 38 min de inactividad/mes |
| **Verificación** | Synthetic checks cada 60 s desde 2 regiones (CloudWatch Synthetics) |
| **Origen** | SLA con Lumen Studio |

#### NFR-007 — Tolerancia a fallos

| | |
|---|---|
| **Subcaracterística** | Fault tolerance |
| **Descripción** | El sistema continúa operando con funcionalidad degradada ante fallos parciales. |
| **Objetivo** | (1) Caída del servicio de email → notificaciones in-app siguen activas. (2) Caída del servicio de PDF → reportes consultables en pantalla. (3) Caída de S3 → tareas siguen funcionando, adjuntos no disponibles temporalmente. |
| **Verificación** | Pruebas de caos trimestrales |
| **Origen** | Buenas prácticas SRE |

#### NFR-008 — Recuperabilidad (RPO/RTO)

| | |
|---|---|
| **Subcaracterística** | Recoverability |
| **Métrica RPO** | Recovery Point Objective ≤ **1 hora** (pérdida máxima de datos aceptable) |
| **Métrica RTO** | Recovery Time Objective ≤ **4 horas** (tiempo máximo de restauración) |
| **Backup** | RDS Point-in-Time Recovery continuo + snapshot diario, retención 30 días |
| **Verificación** | Simulacro DR trimestral con restauración a entorno aislado |
| **Origen** | Política interna + restricción C3 |

---

### 2.3 Security (Seguridad)

Subcaracterísticas: confidencialidad, integridad, no-repudio, autenticidad, *accountability*.

#### NFR-009 — Cifrado en tránsito

| | |
|---|---|
| **Descripción** | Toda comunicación cliente-servidor y servidor-servidor cifrada. |
| **Objetivo** | TLS 1.3 mínimo · HSTS habilitado · `Strict-Transport-Security: max-age=63072000; includeSubDomains; preload` |
| **Verificación** | Mozilla SSL Test (grado A+); inspección automática semanal |
| **Origen** | OWASP ASVS V9 |

#### NFR-010 — Cifrado en reposo

| | |
|---|---|
| **Descripción** | Datos persistidos cifrados con claves administradas. |
| **Objetivo** | AES-256 para PostgreSQL (RDS encryption) y S3 (SSE-KMS). Claves rotadas anualmente. |
| **Verificación** | Auditoría AWS Config |
| **Origen** | Restricción C3 + buenas prácticas |

#### NFR-011 — Gestión de credenciales

| | |
|---|---|
| **Descripción** | Contraseñas y secretos manejados de forma segura. |
| **Objetivo** | (1) Contraseñas con `bcrypt`, factor de costo ≥ 12. (2) Sesiones JWT con expiración 8 h, refresh 30 días. (3) Secretos en AWS Secrets Manager, nunca en código ni `.env` versionado. |
| **Verificación** | Auditoría de código + escaneo `truffleHog` en CI |
| **Origen** | OWASP ASVS V2 |

#### NFR-012 — OWASP Top 10

| | |
|---|---|
| **Descripción** | El sistema mitiga las 10 vulnerabilidades más comunes según OWASP. |
| **Objetivo** | Checklist OWASP Top 10 (versión vigente) verificado antes de cada release mayor. Cero hallazgos `HIGH` o `CRITICAL` abiertos al desplegar. |
| **Verificación** | (1) `pip-audit` + `npm audit` en CI, severidad `HIGH` bloquea merge. (2) DAST (OWASP ZAP) en staging. (3) Pentest externo anual. |
| **Origen** | OWASP, ASVS Level 2 |

#### NFR-013 — Privacidad de datos personales (PII)

| | |
|---|---|
| **Descripción** | Datos personales tratados conforme a Ley 1581 de 2012 (Colombia) y a buenas prácticas internacionales. |
| **Objetivo** | (1) PII limitada a: nombre completo, email, foto. (2) Solicitud de eliminación atendida en ≤ 30 días (anonimización). (3) Bitácora de acceso a PII por `admin`. (4) Datos almacenados en AWS sa-east-1 (restricción C3). |
| **Verificación** | Auditoría manual semestral |
| **Origen** | Ley 1581 de 2012 + política Lumen |

---

### 2.4 Usability (Usabilidad)

#### NFR-014 — Accesibilidad WCAG 2.1 AA

| | |
|---|---|
| **Subcaracterística** | Accessibility |
| **Descripción** | La aplicación cumple WCAG 2.1 nivel AA. |
| **Objetivo** | (1) Navegación completa por teclado. (2) Contraste mínimo 4.5:1 (texto normal), 3:1 (texto grande). (3) Toda imagen significativa con `alt`. (4) `aria-*` en componentes interactivos. (5) El color **no** es el único portador de información. |
| **Verificación** | (1) `axe-core` en CI. (2) Auditoría manual con lector de pantalla (NVDA, VoiceOver) en pantallas críticas. (3) Lighthouse Accessibility ≥ 95. |
| **Origen** | Restricción C5 |

#### NFR-015 — Diseño responsivo

| | |
|---|---|
| **Subcaracterística** | User interface aesthetics |
| **Descripción** | La UI funciona en móviles, tabletas y escritorio. |
| **Objetivo** | Compatibilidad desde 360 px de ancho (móvil) hasta ≥ 1920 px (escritorio). Sin scroll horizontal en ningún breakpoint. |
| **Verificación** | Responsive testing matrix; visual regression con Percy |
| **Origen** | Restricción funcional / movilidad de Lumen |

#### NFR-016 — Aprendibilidad

| | |
|---|---|
| **Subcaracterística** | Learnability |
| **Descripción** | Un usuario nuevo completa las tareas básicas con poca ayuda. |
| **Objetivo** | Un `contributor` nuevo completa 5 tareas básicas (login, ver "mis tareas", crear tarea, comentar, cerrar tarea) en su primera sesión sin documentación, en ≤ 10 min. |
| **Verificación** | Pruebas de usabilidad con ≥ 8 participantes representativos antes del beta |
| **Origen** | NN/g, restricción de adopción |

---

### 2.5 Compatibility (Compatibilidad)

#### NFR-017 — Compatibilidad de navegadores

| | |
|---|---|
| **Subcaracterística** | Co-existence |
| **Descripción** | La UI funciona correctamente en navegadores modernos. |
| **Objetivo** | Chrome / Edge: últimas 2 versiones mayores · Firefox: últimas 2 · Safari: ≥ 16. **No soportado**: Internet Explorer. |
| **Verificación** | Cross-browser testing (BrowserStack) en CI nightly |
| **Origen** | Asumir A02 (ver [scope](../01-product/scope.md#6-suposiciones)) |

#### NFR-018 — Interoperabilidad por API

| | |
|---|---|
| **Subcaracterística** | Interoperability |
| **Descripción** | Terceros pueden integrarse mediante una API pública documentada. |
| **Objetivo** | API REST con especificación OpenAPI 3.1 publicada. Versionado por URL (`/v1/...`). Cambios incompatibles → nueva versión. |
| **Verificación** | Validación OpenAPI en CI + contract testing |
| **Origen** | Necesidad futura de integraciones (Slack, Harvest) |

---

### 2.6 Maintainability (Mantenibilidad)

#### NFR-019 — Cobertura de pruebas

| | |
|---|---|
| **Subcaracterística** | Testability |
| **Métrica** | Line coverage |
| **Objetivo backend** | ≥ 80 % |
| **Objetivo frontend** | ≥ 70 % |
| **Excluye** | Migraciones, código generado, *boilerplate* de framework |
| **Verificación** | `pytest --cov` y `vitest --coverage` reportados en cada PR |
| **Origen** | Política interna calidad |

#### NFR-020 — Calidad estática

| | |
|---|---|
| **Subcaracterística** | Modifiability |
| **Descripción** | Código adherente a estándares automatizados. |
| **Objetivo** | (1) `ruff check` y `ruff format` (Python) — cero warnings en `main`. (2) `eslint` + `prettier` (TS/JS) — cero warnings. (3) `mypy --strict` (Python) — cero errores en código nuevo. (4) Complejidad ciclomática ≤ 10 por función. |
| **Verificación** | CI bloquea merge ante violaciones |
| **Origen** | Buenas prácticas |

#### NFR-021 — Tiempo de build y despliegue

| | |
|---|---|
| **Subcaracterística** | Modifiability |
| **Objetivo** | (1) Pipeline CI completo ≤ 8 min. (2) Despliegue a producción ≤ 10 min después de merge a `main`. (3) Rollback ≤ 5 min. |
| **Verificación** | Métricas de pipeline en GitHub Actions |
| **Origen** | DORA metrics |

---

### 2.7 Portability (Portabilidad)

#### NFR-022 — Reemplazabilidad de proveedor cloud

| | |
|---|---|
| **Subcaracterística** | Replaceability |
| **Descripción** | El sistema usa servicios estándar para reducir el lock-in. |
| **Objetivo** | (1) PostgreSQL estándar (no Aurora-specific features). (2) Almacenamiento via S3-compatible API. (3) Aplicación contenerizada (Docker). (4) IaC con Terraform en lugar de consola. (5) Una salida de AWS sería viable en ≤ 30 días-persona. |
| **Verificación** | Inspección arquitectónica anual |
| **Origen** | Riesgo R4 ([visión](../01-product/vision.md#9-riesgos-estratégicos)) |

#### NFR-023 — Instalabilidad en entorno de desarrollo

| | |
|---|---|
| **Subcaracterística** | Installability |
| **Objetivo** | Un dev nuevo levanta el entorno local en ≤ 30 min siguiendo la guía de [onboarding](../10-onboarding/local-setup.md). Comando único `make dev`. |
| **Verificación** | Validación con cada nuevo joiner |
| **Origen** | Productividad del equipo |

---

### 2.8 Functional Suitability — observabilidad transversal

#### NFR-024 — Logs estructurados

| | |
|---|---|
| **Descripción** | Toda traza emitida en JSON estructurado. |
| **Objetivo** | (1) Cada log incluye `timestamp`, `level`, `service`, `request_id`, `user_id` (si aplica), `message`. (2) Logs centralizados en CloudWatch Logs. (3) Retención 30 días (operacional) + 2 años (auditoría, en S3 Glacier). |
| **Verificación** | Inspección de logs muestrales en cada release |
| **Origen** | SRE Book — Google |

#### NFR-025 — Métricas y trazas

| | |
|---|---|
| **Descripción** | El sistema expone telemetría estándar. |
| **Objetivo** | (1) Métricas Prometheus: RED (Rate, Errors, Duration) por endpoint. (2) Trazas OpenTelemetry, sampling 10 %. (3) Endpoint `/health` retorna 200 si DB y dependencias críticas responden. (4) Endpoint `/metrics` para scraping. |
| **Verificación** | Dashboard Grafana en producción |
| **Origen** | Buenas prácticas SRE |

---

## 3. Resumen consolidado

| ID | Característica ISO 25010 | NFR | Objetivo principal |
|---|---|---|---|
| NFR-001 | Performance | API latency | p95 ≤ 300 ms |
| NFR-002 | Performance | UI load | LCP ≤ 2.5 s |
| NFR-003 | Performance | Reportes | ≤ 10 s |
| NFR-004 | Performance | Import CSV | ≥ 83 filas/s |
| NFR-005 | Performance | Capacity | 80 → 240 usuarios |
| NFR-006 | Reliability | Availability | 99.5 % mensual |
| NFR-007 | Reliability | Fault tolerance | Degradación parcial |
| NFR-008 | Reliability | Recoverability | RPO 1 h · RTO 4 h |
| NFR-009 | Security | TLS | TLS 1.3 + HSTS |
| NFR-010 | Security | Encryption at rest | AES-256 |
| NFR-011 | Security | Credentials | bcrypt cost ≥ 12 |
| NFR-012 | Security | OWASP Top 10 | Cero `HIGH` abiertos |
| NFR-013 | Security | Privacy / PII | Ley 1581/2012 |
| NFR-014 | Usability | Accessibility | WCAG 2.1 AA |
| NFR-015 | Usability | Responsive | 360 px → 1920+ |
| NFR-016 | Usability | Learnability | Onboarding < 10 min |
| NFR-017 | Compatibility | Browsers | Chrome/Edge/FF ult. 2 · Safari 16+ |
| NFR-018 | Compatibility | API | OpenAPI 3.1 |
| NFR-019 | Maintainability | Test coverage | BE ≥ 80 % · FE ≥ 70 % |
| NFR-020 | Maintainability | Code quality | Ruff/ESLint zero warn |
| NFR-021 | Maintainability | Build/Deploy | CI ≤ 8 min · Deploy ≤ 10 min |
| NFR-022 | Portability | Cloud lock-in | Salida ≤ 30 días-persona |
| NFR-023 | Portability | Local setup | ≤ 30 min |
| NFR-024 | Funct. suit. | Structured logs | JSON, retención 30d/2a |
| NFR-025 | Funct. suit. | Telemetry | RED + OpenTelemetry |

---

## 4. Verificación cruzada

Estos NFR se traducen en pruebas concretas en [test-strategy](../07-quality/test-strategy.md) (bloque 7) y en SLOs operativos en [slo-sli](../08-operations/slo-sli.md) (bloque 8). La trazabilidad está consolidada en [traceability.md](traceability.md).

---

## Referencias

- ISO/IEC 25010:2011 — *Systems and software Quality Requirements and Evaluation (SQuaRE)*
- ISO/IEC/IEEE 29148:2018 — *Requirements engineering*
- OWASP ASVS — *Application Security Verification Standard*
- OWASP Top 10 — vigente
- WCAG 2.1 — *Web Content Accessibility Guidelines*
- Google SRE Book — capítulos sobre SLOs y observabilidad
- Ley 1581 de 2012 (Colombia) — Protección de datos personales
- Documentos relacionados: [Funcionales](functional.md) · [Trazabilidad](traceability.md) · [Estrategia de pruebas](../07-quality/test-strategy.md)
