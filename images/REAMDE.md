# java-notes

The **Java Development Kit (JDK)** is the complete environment for developing Java applications. It includes the libraries and tools required to write, compile, and run Java code.

**Code editor:** IntelliJ IDEA.

Create a project in IntelliJ IDEA and write source code inside the `src` directory.

**Recommendation:** Install the SonarQube plugin to detect code smells and improve code quality.

## Key concepts

**JVM (Java Virtual Machine):** Executes platform-independent Java bytecode and translates it into operating system–specific instructions. 
Java source code is compiled into `.class` files containing bytecode, which allows programs to run on multiple platforms.  
The **Java Runtime Environment (JRE)** provides the runtime needed to execute Java applications and includes the JVM.  
The **JDK** extends the JRE with development tools such as the Java compiler (`javac`) and other utilities for building and debugging programs.
> JDK = JRE(JVM) + otters tools developers

![imagen](img.png)


### Data types
Data types define the kind of values a variable can hold. Java has primitive types for simple values, and reference types for more complex data.

```java
void main() {

    // ==================== Data types ==================== //
    // Each data type has a capacity

    // Primitive types
    int number;        // integer
    double decimal;    // floating-point number
    boolean active;    // true/false value
    char letter;       // single character
    long bigNumber;    // large integer
    float ratio;       // decimal number (less precision)
    short smallInt;    // small integer
    byte tinyInt;      // very small integer

    // Non-primitive (reference) types
    String text;       // sequence of characters
    LocalDate date;    // date object
    int[] values;      // array of integers
    Object object;     // generic object reference

}

```

### Casting in java
Casting is converting a value from one type to another. In Java, it can be **implicit** (automatic, e.g., int → double) or **explicit** (manual, e.g., (int) 3.5).


```java
void main(){
// ==================== casting ==================== //

    // Implicit casting (widening): automatic conversion
    int intValue = 10;
    double doubleValue = intValue; // int → double
    System.out.println(doubleValue);

    // Explicit casting (narrowing): manual conversion
    double decimalValue = 9.78;
    int convertedValue = (int) decimalValue; // double → int
    System.out.println(convertedValue);
}
```
### Scanner
Scanner is a class used to read input from the user, such as text, numbers, or other data types. You create a Scanner object and call its methods like nextInt(), nextLine(), or nextDouble() to get input.
```java
void main() {
// ==================== scanner ==================== //

    // Scanner = reads user input from the terminal
    Scanner scanner = new Scanner(System.in);

    System.out.println("¿Cuál es tu nombre?");
    String nombre = scanner.nextLine(); // nextLine(): reads a String
    System.out.println(nombre + ", tienes " +" anios");
    
    scanner.close(); // good practice: close resources
}
```

### Java memory management

**Memory model**

* **Stack:** Stores primitive values and object references. Limited size. Overflow causes *StackOverflowError*.
* **Heap:** Stores objects. Dynamically managed memory. Overflow causes *OutOfMemoryError*.

**Primitive types vs. objects**

* **Primitives:** Assignment copies the value → independent variables.
* **Objects:** Assignment copies the reference → multiple variables can share the same object.

```java
package mynotes.fundamentals;

public class MemoryExample {
    public static void main(String[] args) {

        // Primitive type (stored in stack)
        int a = 10;
        int b = 20;

        b = a;   // copy of value
        b = 20;

        System.out.println("a: " + a + ", b: " + b );


        // Object type (reference in stack, object in heap)
        String text1 = new String("Hello");
        String text2 = new String("Hi");

        text1 = text2; // Copy reference → both variables point to the same object

        System.out.println("text1: " + text1 + ", text2: " + text2 );

        // Object becomes unreachable → eligible for garbage collection
        text1 = null;
    }
}

```

# Loops and Conditionals

Control flow structures that decide what code runs and how many times.

```java
void main() {

    // ==================== if / else ==================== //

    int age = 20;

    if (age >= 18) {
        System.out.println("adult");
    } else if (age >= 13) {
        System.out.println("teenager");
    } else {
        System.out.println("child");
    }


    // ==================== Operators ==================== //

    // Comparison
    a == b    // equal
    a != b    // not equal
    a > b     // greater than
    a < b     // less than
    a >= b    // greater or equal
    a <= b    // less or equal

    // Logical
    a && b    // AND — true if both are true
    a || b    // OR  — true if at least one is true
    !a        // NOT — inverts the value


    // ==================== Ternary ==================== //

    // condition ? valueIfTrue : valueIfFalse
    String result = (age >= 18) ? "adult" : "minor";


    // ==================== switch ==================== //

    String day = "Monday";

    switch (day) {
        case "Monday":
            System.out.println("start of week");
            break;
        case "Friday":
            System.out.println("end of week");
            break;
        default:
            System.out.println("midweek");
    }

    // Switch expression (Java 14+)
    String type = switch (day) {
        case "Monday", "Friday" -> "edge day";
        default                 -> "midweek";
    };


    // ==================== while ==================== //

    // Runs while condition is true
    int i = 0;
    while (i < 5) {
        System.out.println(i);
        i++;
    }

    // do-while: always runs at least once
    int j = 0;
    do {
        System.out.println(j);
        j++;
    } while (j < 5);


    // ==================== for ==================== //

    // Classic for
    for (int k = 0; k < 5; k++) {
        System.out.println(k);
    }

    // Enhanced for-each — use with arrays and collections
    int[] numbers = {1, 2, 3, 4, 5};
    for (int n : numbers) {
        System.out.println(n);
    }


    // ==================== break / continue ==================== //

    for (int k = 0; k < 10; k++) {
        if (k == 3) continue;   // skip iteration
        if (k == 7) break;      // exit loop
        System.out.println(k);
    }

}
```

## collections

### Lists

A **List** is an ordered, dynamic collection that allows duplicate elements.

> Default choice: ArrayList.

```java
void main() {

    // ==================== List types ==================== //

    // string can change for int, objects ...
    List<String> names = new ArrayList<>();            // dynamic array, fast access by index
    List<String> names = new LinkedList<>();           // linked nodes, fast insert/delete
    List<String> names = List.of("Alice", "Bob");      // immutable
    List<String> copy  = new ArrayList<>(names);       // mutable copy


    // ==================== Methods ==================== //

    names.add("Alice");        // append to end
    names.add(1, "Bob");       // insert at index
    names.get(0);              // read by index
    ...


    // ==================== Iterating ==================== //

    for (int i = 0; i < names.size(); i++) { }        // classic for, use when you need the index
    for (String name : names) { }                     // enhanced for-each
    names.forEach(name -> System.out.println(name));  // lambda


    // ==================== Sorting ==================== //

    Collections.sort(names);                              // natural order
    names.sort(Comparator.reverseOrder());                // reverse
    names.sort(Comparator.comparingInt(String::length));  // custom


    // ==================== Patterns ==================== //

    List<String> list = new ArrayList<>(Arrays.asList("a", "b", "c"));  // array → list
    String[] arr      = list.toArray(new String[0]);                     // list → array
    List<String> sub  = list.subList(1, 3);                              // sublist [b, c]
    list.removeIf(s -> s.equals("a"));                                   // safe remove

}
```

# Streams and Lambdas

**Lambda:** a short anonymous function. `(parameters) -> expression`  
**Stream:** a pipeline to process collections in a functional style. Does not modify the original list.

```java
void main() {

    // ==================== Lambda ==================== //

    // Without lambda
    Runnable r = new Runnable() {
        public void run() { System.out.println("hello"); }
    };

    // With lambda
    Runnable r = () -> System.out.println("hello");

    // Lambda with parameters
    Comparator<String> c = (a, b) -> a.compareTo(b);

    // Lambda with block body
    Comparator<String> c = (a, b) -> {
        return a.compareTo(b);
    };


    // ==================== Stream pipeline ==================== //

    // source → intermediate operations → terminal operation
    List<String> names = List.of("Alice", "Bob", "Carlos", "Ana");

    names.stream()
         .filter(n -> n.startsWith("A"))    // intermediate — keep matching
         .map(n -> n.toUpperCase())          // intermediate — transform
         .sorted()                           // intermediate — sort
         .forEach(System.out::println);      // terminal — ALICE, ANA


    // ==================== Intermediate operations ==================== //

    List<Integer> numbers = List.of(1, 2, 3, 4, 5, 6);

    // filter — keeps elements that match the condition
    numbers.stream().filter(n -> n % 2 == 0);           // [2, 4, 6]

    // map — transforms each element
    numbers.stream().map(n -> n * 2);                    // [2, 4, 6, 8, 10, 12]

    // sorted — natural order
    numbers.stream().sorted();                           // [1, 2, 3, 4, 5, 6]

    // sorted with comparator
    numbers.stream().sorted(Comparator.reverseOrder());  // [6, 5, 4, 3, 2, 1]

    // distinct — removes duplicates
    List.of(1, 2, 2, 3).stream().distinct();             // [1, 2, 3]

    // limit / skip
    numbers.stream().limit(3);                           // [1, 2, 3]
    numbers.stream().skip(3);                            // [4, 5, 6]


    // ==================== Terminal operations ==================== //

    // forEach — iterate
    numbers.stream().forEach(System.out::println);

    // collect — gather results into a list
    List<Integer> evens = numbers.stream()
                                 .filter(n -> n % 2 == 0)
                                 .collect(Collectors.toList());  // [2, 4, 6]

    // count — number of elements
    long count = numbers.stream().filter(n -> n > 3).count();   // 3

    // reduce — combine elements into one value
    int sum = numbers.stream().reduce(0, (a, b) -> a + b);      // 21

    // anyMatch / allMatch / noneMatch
    boolean hasEven = numbers.stream().anyMatch(n -> n % 2 == 0);   // true
    boolean allPos  = numbers.stream().allMatch(n -> n > 0);         // true
    boolean noneNeg = numbers.stream().noneMatch(n -> n < 0);        // true

    // min / max
    Optional<Integer> min = numbers.stream().min(Comparator.naturalOrder());  // 1
    Optional<Integer> max = numbers.stream().max(Comparator.naturalOrder());  // 6


    // ==================== Stream with objects ==================== //

    List<Person> people = List.of(
        new Person("Alice", 30),
        new Person("Bob", 17),
        new Person("Carlos", 25)
    );

    List<String> adults = people.stream()
                                .filter(p -> p.age >= 18)
                                .map(p -> p.name)
                                .sorted()
                                .collect(Collectors.toList());  // [Alice, Carlos]

}
```

# Enum

An **enum** is a fixed set of named constants. Use it when a variable can only be one of a limited set of values.

```java
void main() {

    // ==================== Basic enum ==================== //

    enum Day { MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY }

    Day today = Day.MONDAY;
    System.out.println(today);          // MONDAY
    System.out.println(today.name());   // MONDAY  — as String
    System.out.println(today.ordinal()); // 0       — position (0-based)


    // ==================== Enum in conditionals ==================== //

    if (today == Day.MONDAY) {
        System.out.println("start of week");
    }

    switch (today) {
        case MONDAY  -> System.out.println("start of week");
        case FRIDAY  -> System.out.println("end of week");
        default      -> System.out.println("midweek");
    }


    // ==================== Enum with fields and methods ==================== //

    enum Planet {
        MERCURY(3.303e+23, 2.4397e6),
        VENUS  (4.869e+24, 6.0518e6),
        EARTH  (5.976e+24, 6.37814e6);

        final double mass;
        final double radius;

        Planet(double mass, double radius) {
            this.mass   = mass;
            this.radius = radius;
        }

        double surfaceGravity() {
            final double G = 6.67300E-11;
            return G * mass / (radius * radius);
        }
    }

    System.out.println(Planet.EARTH.surfaceGravity());   // 9.80


    // ==================== Useful methods ==================== //

    // values() — returns all constants as array
    for (Day d : Day.values()) {
        System.out.println(d);
    }

    // valueOf() — get enum from String
    Day friday = Day.valueOf("FRIDAY");   // Day.FRIDAY

}
```

# POO

**Object (OOP):** An object is an entity that encapsulates data and the operations that act on that data, representing real or abstract elements in a system.

**Advantages of OOP:**

* **Reusability:** Classes and objects can be reused across different modules or projects, reducing code duplication and development time.
* **Maintainability:** Modular structure and clear separation of responsibilities make code easier to understand, debug, and update.
* **Modifiability:** Encapsulation allows internal changes without breaking external interfaces, enabling safer extension of functionality.
* **Reliability:** Isolated components reduce error propagation and improve system stability and testability.

**Core pillars of OOP:** Abstraction, encapsulation, inheritance, and polymorphism.


## Abstraction


In Java, the program starts in `main`. Only code inside `main` runs automatically. Other methods and classes run only when `main` calls them.

```java 
public class Main {
    public static void main(String[] args) {
    //code
    }
}
```

### Class and objects

**Class**: A blueprint (template) that defines the structure and behavior of objects (fields + methods).  
**Object**: A concrete instance created from a class; it represents a real entity in memory with its own state.

> One class → many objects.  
> Objects hold data; the class defines how they behave

**Example**:
```java
class MyClass {        // Class
    int attribute;     // Attribute: object data

    void method() {   // Method: object action
        // action
    }
}
```

Instance in main:
```
// Create object and use it
MyClass obj = new MyClass();  // Object: instance of the class
obj.attribute = 5;           // Assign value
obj.method();                // Call method

```

### Attributes - Method

**Attributes (fields)**: Variables that store the state of an object or class (instance vs static).  
**Methods**: Functions that define the behavior of an object or class.

> Attributes = data  
> Methods = actions

**Example**:
```java

class MyClass {
    
    // ===== Methods =====
    
    public int attribute;           // Instance attribute: belongs to each object
    public static int staticAttribute; // Static attribute: shared by all instances
    public static final int CONSTANT = 5; // Constant value: cannot be modified (constants are typically static final and written in UPPER_CASE by convention)

    // ===== Methods =====

    public void method() {          // Instance method: no return value
        System.out.println("action\n");
    }

    public static int methodStatic() { // Static method: does not require an instance
        System.out.println("static method");
        return 0;                   // Required return value
    }

    public void methodWithParameter(int attribute) { // Updates the object's state
        this.attribute = attribute; // Assign parameter to instance attribute
        System.out.println("action " + this.attribute + "\n");
    }


}
```

Instance in main:
```
//Instance attribute
MyClass a = new MyClass();     //first instance
a.attribute = 1;              // Only 'a'

// Static attribute
MyClass.staticAttribute = 10; // Shared by all - no instance

//Constant value
int x = MyClass.CONSTANT;     // Read-only
```

### Constructors

Constructors are special methods that **initialize** objects when created. They have the **same name as the class**, no return type, and can have different parameters.

```java

public class Class {
    public int attribute;

    // ===== Constructors ===== 

    public Class() {                 // Default constructor
        this.attribute = 0;            // Initialize attribute with a default value
    }

    public Class(int attribute) {    // Parameterized constructor
        this.attribute = attribute;    // Initialize attribute with a custom value
        staticAttribute = 1;           // Initialize attribute with a default value
    }
}
```

Instance in main:
```
// Using default constructor
Class obj1 = new Class();        // attribute = 0

// Using parameterized constructor
Class obj2 = new Class(10);      // attribute = 10

```




## Encapsulation

Encapsulation is the practice of keeping an object’s attributes private and controlling access through getters and setters. Public attributes can be accessed directly, while private attributes require methods to read or modify their value, protecting the internal state and allowing controlled changes.

```java
public class Encapsulation {
    
    // ===== Attributes =====
    
    public int attributePublic;    // Public: accessible from any class
    private int attributePrivate;  // Private: accessible only within this class
    protected int attributeProtected; // Protected: accessible within the package and subclasses
    int attributeDefault;          // Default (package-private): accessible within the same package

    // ===== Getters and Setters =====

    public int getAttributePrivate() {      // Getter: read access to private attribute
        return attributePrivate;
    }

    public void setAttributePrivate(int value) { // Setter: controlled write access
        this.attributePrivate = value;
    }
}

```


Instance in main:
```
Encapsulation obj = new Encapsulation();

// Access public attribute directly
obj.attributePublic = 5;

// Read private attribute via getter
int value = obj.getAttributePrivate();

// Access private attribute via setter
obj.setAttributePrivate(10);
```

Recommendation 
> A private attribute is now used by default, with access managed through getter and setter methods.


# Association, Aggregation and Composition

Relationships between classes that describe how objects interact or depend on each other.

**Association:** a general relationship between two classes. Each can exist independently.  
**Aggregation:** a "has-a" relationship. The child can exist without the parent.  
**Composition:** a strong "has-a" relationship. The child cannot exist without the parent.

> Association → Aggregation → Composition (increasing dependency)

```java
void main() {

    // ==================== Association ==================== //
    // Two classes relate to each other, but neither owns the other

    class Teacher {
        String name;

        Teacher(String name) { this.name = name; }
    }

    class Student {
        String name;
        Teacher teacher;   // Student knows about Teacher

        Student(String name, Teacher teacher) {
            this.name    = name;
            this.teacher = teacher;   // Teacher exists independently
        }
    }

    Teacher teacher = new Teacher("Mr. Smith");
    Student student = new Student("Alice", teacher);
    // teacher still exists if student is deleted


    // ==================== Aggregation ==================== //
    // Parent has a child, but child can exist without the parent

    class Engine {
        String type;

        Engine(String type) { this.type = type; }
    }

    class Car {
        String model;
        Engine engine;   // Car has an Engine

        Car(String model, Engine engine) {
            this.model  = model;
            this.engine = engine;   // Engine is created outside Car
        }
    }

    Engine engine = new Engine("V8");   // Engine exists on its own
    Car car = new Car("Mustang", engine);
    // engine still exists if car is deleted


    // ==================== Composition ==================== //
    // Parent creates and owns the child — child cannot exist without parent

    class Room {
        String name;

        Room(String name) { this.name = name; }
    }

    class House {
        String address;
        Room room;   // House owns Room

        House(String address) {
            this.address = address;
            this.room    = new Room("Living Room");   // Room created inside House
        }
    }

    House house = new House("123 Main St");
    // room only exists as part of house — destroyed with it

}
```

```java
```



```java
```

```java
```

```java
```

```java
```

```java
```

```java
```

```java
```

```java
```

```java
```

```java
```
















