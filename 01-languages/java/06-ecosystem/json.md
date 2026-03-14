# JSON – Jackson
*Most widely used JSON library for Java*

## Setup (Maven)

```xml
<dependency>
  <groupId>com.fasterxml.jackson.core</groupId>
  <artifactId>jackson-databind</artifactId>
  <version>2.16.0</version>
</dependency>
```

---

## ObjectMapper
*Core class — reuse it (it's thread-safe and expensive to create)*

```java
ObjectMapper mapper = new ObjectMapper();
```

---

## Java Object → JSON (Serialization)

```java
class Person {
    public String name;
    public int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}

Person person = new Person("Alice", 25);

// To JSON string
String json = mapper.writeValueAsString(person);
// {"name":"Alice","age":25}

// Pretty print
String pretty = mapper.writerWithDefaultPrettyPrinter()
    .writeValueAsString(person);

// To file
mapper.writeValue(new File("person.json"), person);
```

---

## JSON → Java Object (Deserialization)

```java
String json = "{\"name\":\"Alice\",\"age\":25}";

// To object (needs default constructor or @JsonCreator)
Person person = mapper.readValue(json, Person.class);
person.name;  // "Alice"

// From file
Person person = mapper.readValue(new File("person.json"), Person.class);

// To List
String jsonArray = "[{\"name\":\"Alice\"},{\"name\":\"Bob\"}]";
List<Person> people = mapper.readValue(
    jsonArray,
    new TypeReference<List<Person>>() {}
);

// To Map (generic JSON)
Map<String, Object> map = mapper.readValue(json, Map.class);
```

---

## Annotations

```java
class User {
    @JsonProperty("user_name")   // rename field in JSON
    public String username;

    @JsonIgnore                  // exclude from JSON
    public String password;

    @JsonInclude(JsonInclude.Include.NON_NULL)  // skip if null
    public String email;
}

// Constructor for immutable objects
class Point {
    public final int x;
    public final int y;

    @JsonCreator
    Point(@JsonProperty("x") int x, @JsonProperty("y") int y) {
        this.x = x;
        this.y = y;
    }
}
```

---

## Jackson with Records (Java 14+)

```java
// Add this dependency for records support
// jackson-databind 2.12+ supports records natively

record Person(String name, int age) {}

String json = mapper.writeValueAsString(new Person("Alice", 25));
Person p = mapper.readValue(json, Person.class);
```

---

## Common Configuration

```java
ObjectMapper mapper = new ObjectMapper()
    .configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false)  // ignore extra fields
    .configure(SerializationFeature.WRITE_DATES_AS_TIMESTAMPS, false)      // dates as ISO strings
    .registerModule(new JavaTimeModule());  // support LocalDate, LocalDateTime
```
