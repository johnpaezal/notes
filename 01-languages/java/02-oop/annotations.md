# Annotations
*Metadata attached to code — read by compiler or runtime*

## Built-in Annotations

```java
// @Override – tells compiler this overrides a parent method
// Catches typos at compile time
@Override
public String toString() { return "..."; }

// @Deprecated – marks something as outdated
@Deprecated
void oldMethod() { }

// @SuppressWarnings – silence specific compiler warnings
@SuppressWarnings("unchecked")
List list = new ArrayList();

@SuppressWarnings("unused")
int unusedVar = 5;

// @FunctionalInterface – ensures interface has exactly one abstract method
@FunctionalInterface
interface Transformer {
    String transform(String input);
}

// @SafeVarargs – suppress warnings on varargs with generics
@SafeVarargs
final <T> void print(T... items) { }
```

---

## Common Annotations by Context

```java
// On classes
@FunctionalInterface
@Deprecated

// On methods
@Override
@Deprecated
@SuppressWarnings("...")

// On fields
@SuppressWarnings("unused")
```

---

## Custom Annotations

```java
// Define an annotation
import java.lang.annotation.*;

@Retention(RetentionPolicy.RUNTIME)   // available at runtime
@Target(ElementType.METHOD)           // only on methods
public @interface Log {
    String value() default "INFO";    // element with default
}

// Use it
class Service {
    @Log("DEBUG")
    void process() { }

    @Log   // uses default "INFO"
    void start() { }
}

// Read at runtime via reflection
Method method = Service.class.getMethod("process");
Log log = method.getAnnotation(Log.class);
log.value();  // "DEBUG"
```

---

## @Retention Values

| Value     | Visible at                        |
|-----------|-----------------------------------|
| `SOURCE`  | Source code only (discarded)      |
| `CLASS`   | Bytecode (default, not at runtime)|
| `RUNTIME` | Available via reflection          |

## @Target Values

| Value        | Applies to         |
|--------------|--------------------|
| `TYPE`       | Class, interface   |
| `METHOD`     | Methods            |
| `FIELD`      | Fields             |
| `PARAMETER`  | Method parameters  |
| `CONSTRUCTOR`| Constructors       |
