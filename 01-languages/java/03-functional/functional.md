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

## Functional Interfaces
*Single-method interfaces used with lambdas*

```java
// Function<T, R> – takes T, returns R
Function<String, Integer> length = s -> s.length();
length.apply("hello");  // 5

// Predicate<T> – takes T, returns boolean
Predicate<Integer> isEven = n -> n % 2 == 0;
isEven.test(4);   // true
isEven.test(3);   // false

// Consumer<T> – takes T, returns nothing
Consumer<String> print = s -> System.out.println(s);
print.accept("hello");

// Supplier<T> – takes nothing, returns T
Supplier<String> greeting = () -> "Hello!";
greeting.get();  // "Hello!"

// BiFunction<T, U, R> – takes two args, returns R
BiFunction<String, Integer, String> repeat = (s, n) -> s.repeat(n);
repeat.apply("ab", 3);  // "ababab"

// Composing
Function<Integer, Integer> times2 = n -> n * 2;
Function<Integer, Integer> plus3 = n -> n + 3;

times2.andThen(plus3).apply(5);  // (5*2)+3 = 13
times2.compose(plus3).apply(5);  // (5+3)*2 = 16
```

---

## Method References
*Shorthand for lambdas that just call a method*

```java
// Static method
Function<String, Integer> parse = Integer::parseInt;
// equivalent: s -> Integer.parseInt(s)

// Instance method (on parameter)
Function<String, String> upper = String::toUpperCase;
// equivalent: s -> s.toUpperCase()

// Instance method (on specific object)
String prefix = "Hello";
Predicate<String> startsWith = prefix::startsWith;
// equivalent: s -> prefix.startsWith(s)  ← note: reversed

// Constructor
Supplier<ArrayList<String>> newList = ArrayList::new;
// equivalent: () -> new ArrayList<>()

// Common uses with streams
List<String> words = List.of("hello", "world");
words.stream()
    .map(String::toUpperCase)           // instance method
    .forEach(System.out::println);      // instance method on System.out
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

## Collectors
*Terminal operations that collect stream results*

```java
List<String> names = List.of("Alice", "Bob", "Charlie", "Anna");
List<Person> people = List.of(
    new Person("Alice", "Madrid"),
    new Person("Bob", "Barcelona"),
    new Person("Anna", "Madrid")
);

// Collect to list / set
.collect(Collectors.toList())
.collect(Collectors.toUnmodifiableList())
.collect(Collectors.toSet())

// joining – concatenate strings
names.stream()
    .collect(Collectors.joining(", "));              // "Alice, Bob, Charlie, Anna"

names.stream()
    .collect(Collectors.joining(", ", "[", "]"));    // "[Alice, Bob, Charlie, Anna]"

// counting
long count = names.stream()
    .filter(n -> n.startsWith("A"))
    .collect(Collectors.counting());  // 2

// toMap – collect into a Map
Map<String, Integer> nameLengths = names.stream()
    .collect(Collectors.toMap(
        name -> name,        // key
        String::length       // value
    ));
// {"Alice"=5, "Bob"=3, ...}

// groupingBy – group elements by a classifier
Map<String, List<Person>> byCity = people.stream()
    .collect(Collectors.groupingBy(Person::getCity));
// {"Madrid"=[Alice, Anna], "Barcelona"=[Bob]}

// groupingBy + downstream collector
Map<String, Long> countByCity = people.stream()
    .collect(Collectors.groupingBy(
        Person::getCity,
        Collectors.counting()
    ));
// {"Madrid"=2, "Barcelona"=1}

Map<String, List<String>> namesByCity = people.stream()
    .collect(Collectors.groupingBy(
        Person::getCity,
        Collectors.mapping(Person::getName, Collectors.toList())
    ));

// partitioningBy – split into true/false
Map<Boolean, List<Integer>> evenOdd = Stream.of(1, 2, 3, 4, 5)
    .collect(Collectors.partitioningBy(n -> n % 2 == 0));
// {true=[2, 4], false=[1, 3, 5]}

// summarizingInt – stats in one pass
IntSummaryStatistics stats = Stream.of(1, 2, 3, 4, 5)
    .collect(Collectors.summarizingInt(Integer::intValue));
stats.getMin();    // 1
stats.getMax();    // 5
stats.getSum();    // 15
stats.getAverage(); // 3.0
stats.getCount();  // 5
```

---

## Optional
*Wrapper to avoid NullPointerException*

```java
// Creation
Optional<String> opt = Optional.of("hello");         // has value
Optional<String> empty = Optional.empty();            // no value
Optional<String> maybe = Optional.ofNullable(value); // null-safe

// Check and get
opt.isPresent();          // true
opt.isEmpty();            // false
opt.get();                // "hello" (throws if empty)

// Safe access
opt.orElse("default");          // value or default
opt.orElseGet(() -> compute()); // value or computed default
opt.orElseThrow();              // value or NoSuchElementException

// Transform
opt.map(String::toUpperCase);           // Optional<"HELLO">
opt.filter(s -> s.length() > 3);        // Optional<"hello"> or empty
opt.flatMap(s -> Optional.of(s + "!"));

// Execute if present
opt.ifPresent(s -> System.out.println(s));
opt.ifPresentOrElse(
    s -> System.out.println(s),
    () -> System.out.println("empty")
);

// Common pattern
Optional<User> user = findUser(id);
String name = user
    .map(User::getName)
    .orElse("Anonymous");
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
