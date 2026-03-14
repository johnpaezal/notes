# Reflection
*Inspect and manipulate classes, methods, and fields at runtime*

## Get Class Object

```java
// Three ways to get a Class<?>
Class<?> c1 = String.class;               // from type
Class<?> c2 = "hello".getClass();         // from instance
Class<?> c3 = Class.forName("java.lang.String");  // from name (throws ClassNotFoundException)
```

---

## Inspect Class

```java
Class<?> clazz = Person.class;

clazz.getName();           // "com.company.Person"
clazz.getSimpleName();     // "Person"
clazz.getPackageName();    // "com.company"
clazz.getSuperclass();     // parent class
clazz.getInterfaces();     // implemented interfaces
clazz.isInterface();
clazz.isRecord();
clazz.isEnum();
```

---

## Fields

```java
Class<?> clazz = Person.class;

// Public fields only
Field[] fields = clazz.getFields();

// All fields (including private)
Field[] allFields = clazz.getDeclaredFields();

Field field = clazz.getDeclaredField("name");
field.getName();     // "name"
field.getType();     // class java.lang.String
field.getModifiers(); // int (use Modifier.isPrivate(mod) etc.)

// Read/write private field
Person p = new Person("Alice", 25);
field.setAccessible(true);   // bypass private
field.get(p);                // "Alice"
field.set(p, "Bob");         // change value
```

---

## Methods

```java
Class<?> clazz = Person.class;

// Public methods (including inherited)
Method[] methods = clazz.getMethods();

// All declared methods (no inherited)
Method[] declared = clazz.getDeclaredMethods();

// Specific method by name and parameter types
Method method = clazz.getMethod("getName");
Method method = clazz.getMethod("setName", String.class);

method.getName();            // "getName"
method.getReturnType();      // class java.lang.String
method.getParameterTypes();  // parameter types

// Invoke method
Person p = new Person("Alice", 25);
method.setAccessible(true);
Object result = method.invoke(p);            // call getName()
method.invoke(p, "Bob");                     // call setName("Bob")
```

---

## Constructors

```java
// Get constructor
Constructor<?> ctor = clazz.getConstructor(String.class, int.class);

// Create instance dynamically
Person p = (Person) ctor.newInstance("Alice", 25);
```

---

## Annotations via Reflection

```java
// Check if annotation is present
boolean hasLog = method.isAnnotationPresent(Log.class);

// Read annotation values
Log log = method.getAnnotation(Log.class);
log.value();  // "DEBUG"

// All annotations on a class
Annotation[] annotations = clazz.getAnnotations();
```

---

## Common Use Cases

```java
// Frameworks use reflection to:
// - Inject dependencies (Spring @Autowired)
// - Map JSON to objects (Jackson)
// - Run test methods (JUnit @Test)
// - Implement ORM (Hibernate)

// Simple example: print all field values of any object
void printFields(Object obj) throws Exception {
    for (Field f : obj.getClass().getDeclaredFields()) {
        f.setAccessible(true);
        System.out.println(f.getName() + " = " + f.get(obj));
    }
}
```

> **Note**: Reflection is powerful but slow and bypasses type safety. Use it only when necessary (framework code, tooling). Prefer direct access in application code.
