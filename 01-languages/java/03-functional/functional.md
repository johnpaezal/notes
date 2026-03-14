# Functional Programming
*Process data with functions and streams*

## Lambdas
*Short anonymous functions*

**Anonymous functions**: `(params) -> expression`

```java
// Simple
Runnable r = () -> System.out.println("hello");

// With parameters
Comparator<String> c = (a, b) -> a.compareTo(b);

// With block
Function<String, Integer> f = (s) -> {
    return s.length();
};
```

---

## Streams
*Pipeline for processing collections*

```java
List<Integer> nums = List.of(1, 2, 3, 4, 5, 6);

// Pipeline: source → intermediate → terminal
nums.stream()
    .filter(n -> n % 2 == 0)
    .map(n -> n * 2)
    .sorted()
    .forEach(System.out::println);

// Common operations
.filter(n -> n > 3)              // keep matching
.map(n -> n * 2)                 // transform
.sorted()                        // order
.distinct()                      // remove duplicates
.limit(3)                        // first 3
.skip(2)                         // skip 2
.collect(Collectors.toList())    // to list
.count()                         // count
.anyMatch(n -> n > 5)            // any match?
.reduce(0, (a, b) -> a + b)      // combine
.forEach(n -> System.out.println(n))  // iterate each
```

---

## Enums
*Fixed set of named constants*

```java
// Basic enum
enum Day {
    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
}

Day today = Day.MONDAY;
today.name();        // "MONDAY"
today.ordinal();     // 0

// Usage
if (today == Day.MONDAY) { }

switch (today) {
    case MONDAY -> System.out.println("start");
    case FRIDAY -> System.out.println("end");
    default -> System.out.println("middle");
}

// With fields
enum Status {
    PENDING(0), ACTIVE(1), CLOSED(2);

    final int code;

    Status(int code) {
        this.code = code;
    }
}

// Utility methods
Day.values();           // all constants
Day.valueOf("FRIDAY");  // from string
```

---

## Records
*Immutable data carriers (Java 14+)*

**Purpose** – Compact syntax for data-only classes
**Features** – Auto-generates constructor, getters, equals(), hashCode(), toString()

```java
// Traditional class (verbose)
class Person {
    private final String name;
    private final int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String name() { return name; }
    public int age() { return age; }
    // + equals, hashCode, toString
}

// Record (equivalent)
record Person(String name, int age) {}

// Usage
Person p = new Person("Alice", 25);
p.name();       // "Alice"
p.age();        // 25
p.toString();   // "Person[name=Alice, age=25]"

// Records with methods
record Point(int x, int y) {
    // Custom constructor
    Point {
        if (x < 0 || y < 0) {
            throw new IllegalArgumentException("Negative coordinates");
        }
    }

    // Instance method
    double distance() {
        return Math.sqrt(x * x + y * y);
    }

    // Static method
    static Point origin() {
        return new Point(0, 0);
    }
}

// Records are immutable
Point p1 = new Point(3, 4);
// p1.x = 5;  // Error: cannot modify
```
