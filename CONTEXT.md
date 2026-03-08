# Prompt para Crear Notas Técnicas Minimalistas

Crea notas técnicas sobre **[TEMA]** siguiendo este estilo minimalista y universal:

---

## ESTRUCTURA GENERAL

### 1. Encabezado Principal

- Título: `# [Tema] Notes`
- Sin introducción larga, directo al contenido

### 2. Organización por Secciones

```markdown
## Sección Principal
*Descripción corta en cursiva (3-6 palabras)*

### Subsección
*Descripción corta en cursiva (3-6 palabras)*

Contenido...

---

## Siguiente Sección
```

---

## REGLAS DE FORMATO

### Descripciones

- **Cada sección y subsección** debe tener una línea en cursiva debajo del título, de 3 a 6 palabras máximo.
- **Propósito**: Responder "¿qué hace/es esto?" de forma inmediata.
- Ejemplos:
  - `*Storing and managing data*`
  - `*Execute code based on conditions*`
  - `*Ordered sequences with duplicates allowed*`

### Definiciones

- Formato obligatorio: `**Término** – Definición corta (max 10 palabras)`
- Sin explicaciones largas, solo lo esencial.
- **IMPORTANTE — Saltos de línea**: Cuando hay varias definiciones seguidas en vertical, cada línea DEBE terminar con **dos espacios** (`  `) para forzar el salto de línea en Markdown. Sin esto, las líneas se renderizan como texto continuo pegado.

Ejemplo correcto (cada línea termina con dos espacios):

```markdown
**int** – Whole numbers  
**float** – Decimal numbers  
**str** – Text (single or double quotes)  
**bool** – `True` / `False`  
**None** – Absence of value
```

Ejemplo incorrecto (sin dos espacios al final):

```markdown
**int** – Whole numbers
**float** – Decimal numbers
**str** – Text
```

Esto se renderiza como un solo párrafo continuo en lugar de líneas separadas.

### Listas de Características en Línea

Cuando se listan beneficios, pilares o propiedades cortas, usar una sola línea:

```markdown
**Benefits**: Reusability, Maintainability, Modifiability, Reliability

**Four Pillars**: Abstraction, Encapsulation, Inheritance, Polymorphism
```

NO hacer listas verticales largas con explicaciones para cada punto cuando la idea es simple.

### Separadores y Saltos de Línea

- `---` entre secciones mayores (entre cada `##`).
- **Dos espacios al final de línea** (`  `) para forzar saltos en listas de definiciones verticales (`**Term** – Def  `).
- NO usar líneas en blanco excesivas.
- Una línea en blanco entre conceptos relacionados dentro de la misma sección.

---

## ESTILO DE CÓDIGO

### Bloques de Código

```python
# Comentarios SOLO cuando agregan valor
# NO comentar lo obvio

class User:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello, {self.name}")

# Usage
user = User("Alice")
user.greet()  # "Hello, Alice"
```

### Reglas para Código

1. **Ejemplos cortos**: Máximo 20-30 líneas por bloque.
2. **Un concepto por ejemplo**: No mezclar múltiples ideas.
3. **Comentarios inline**: Solo para clarificar salida o contexto (ej. `# "Hello, Alice"`).
4. **Sin código repetitivo**: Mostrar el patrón una sola vez.
5. **Nombres descriptivos**: `user`, `product`, `order` — nunca `x`, `y`, `foo`.
6. **Siempre incluir "# Usage"**: Mostrar cómo se usa después de definir.

### Mostrar Múltiples Variantes

Cuando existan varias formas de hacer algo, mostrarlas juntas con comentarios cortos:

```python
# Basic
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Multiple catch
try:
    # code
except TypeError:
    # handle
except ValueError:
    # handle

# Finally
try:
    # code
finally:
    # always runs
```

---

## PRESENTACIÓN DE CONCEPTOS

### Comparaciones y Relaciones

Usar definiciones alineadas con `**Término** – Definición` (cada línea con dos espacios al final), seguidas de código si es necesario:

```markdown
**Inheritance** – "Is-a" relationship  
**Composition** – "Has-a" relationship (strong)  
**Aggregation** – "Has-a" relationship (weak)
```

### Tablas de Referencia Rápida

Usar tablas solo cuando hay 3+ columnas de información paralela:

```markdown
| Element    | Convention       | Example              |
|------------|------------------|----------------------|
| Class      | PascalCase       | `UserAccount`        |
| Variable   | snake_case       | `first_name`         |
| Constant   | UPPER_SNAKE_CASE | `MAX_SIZE`           |
```

### Niveles de Acceso y Similares

Usar listas con prefijo de código cuando se describen variantes:

```markdown
- `public` – normal attributes (no prefix)
- `_protected` – convention, use underscore prefix
- `__private` – name mangling, use double underscore prefix
```

---

## LO QUE NO HACER

### 1. Explicaciones Verbosas

```markdown
❌ "A constructor is a special method that is called when an object 
    is instantiated. It is used to initialize the object's attributes 
    with values that are passed as parameters..."

✅ **Constructor (`__init__`)** – Initialize objects when created
```

### 2. Ejemplos Largos y Complejos

```markdown
❌ 50+ líneas de código con múltiples conceptos mezclados

✅ 10-20 líneas enfocadas en un solo concepto + sección "# Usage"
```

### 3. Comentarios Redundantes

```python
❌ x = 5  # assign 5 to variable x

✅ count = 0  # tracks active users
```

### 4. Repetir Información

```markdown
❌ Explicar lo mismo en descripción, definición y código

✅ Definición breve + código que lo demuestra
```

### 5. Código Sin Contexto de Uso

```python
❌ Solo definir función sin mostrar cómo se usa

✅ Definir + "# Usage" con ejemplo práctico al final
```

---

## ESTRUCTURA POR TIPO DE TEMA

### Para Lenguajes de Programación

1. Setup / IDE / Tools
2. Shortcuts (si aplica)
3. Naming Conventions
4. Fundamentals (tipos, variables, operadores)
5. Control Flow
6. Collections / Data Structures
7. Functions / Methods
8. OOP (si aplica)
9. Advanced Topics
10. Best Practices

### Para Bases de Datos

1. Fundamentals (tipos, conceptos)
2. Basic Operations (CRUD)
3. Advanced Queries
4. Constraints & Indexes
5. Transactions
6. Design Patterns
7. Best Practices

### Para Frameworks / Libraries

1. Setup & Installation
2. Core Concepts
3. Basic Usage
4. Common Patterns
5. Advanced Features
6. Best Practices

---

## PRINCIPIOS CLAVE

**Minimalismo** – Una idea por sección, ejemplos que se leen en 10 segundos, sin relleno.

**Universalidad** – Código y términos en inglés, ejemplos genéricos (`User`, `Product`, `Order`), convenciones estándar de industria.

**Escaneabilidad** – Jerarquía visual clara con `##` y `###`, código destacado en bloques, información agrupada por concepto.

**Practicidad** – Ejemplos realistas, código que funciona al copiar-pegar, patrones que realmente se usan en desarrollo.

---

## PLANTILLA BASE

```markdown
# [Topic] Notes

## Section Name
*Short description in italics*

### Subsection Name
*Short description in italics*

**Key Term** – Brief definition (max 10 words)

```[language]
# Minimal code example
concept demonstration

# Usage
practical application
```

---

## Next Section
*Short description*

### Subsection
*Short description*

Content following same pattern...

---

## Best Practices

**Naming Conventions**:
- Classes: `PascalCase`
- Methods/attributes: `snake_case`
- Constants: `UPPER_SNAKE_CASE`

**Principles**:
- Single Responsibility – One class, one purpose
- Keep methods short and focused
- Use descriptive names
```

---

## CHECKLIST FINAL

Antes de entregar las notas, verificar:

- [ ] Cada sección (`##`) y subsección (`###`) tiene descripción en cursiva
- [ ] Definiciones con formato `**Term** – Definition`
- [ ] Ejemplos de código < 30 líneas con sección `# Usage`
- [ ] Separadores `---` entre secciones mayores
- [ ] Sin explicaciones redundantes ni relleno
- [ ] Términos clave en negrita
- [ ] Jerarquía clara (`##` → `###`)
- [ ] Sin comentarios obvios en código
- [ ] Nombres descriptivos en ejemplos (`user`, `product`, no `x`, `foo`)
- [ ] Listas de definiciones verticales terminan con dos espacios por línea
- [ ] Listas de propiedades en línea cuando son cortas
- [ ] Best Practices al final del documento

**Regla de oro**: Si algo puede explicarse en menos palabras, hazlo.