# Java Notes

### References
- https://www.w3schools.com/java/java_ref_reference.asp 

## Setup
*Development environment and tools*

**JDK (Java Development Kit)** – Complete development environment (compiler, libraries, tools)  
**IDE** – IntelliJ IDEA  
**Plugin** – SonarQube (code quality)

### Architecture
*How Java executes your code*

```
JDK = JRE + Development Tools
JRE = JVM + Runtime Libraries
```

**JVM (Java Virtual Machine)**  
Executes bytecode (`.class` files) and translates it into machine-specific instructions. Acts as an abstraction layer between Java code and the operating system, enabling platform independence.

**JRE (Java Runtime Environment)**  
Provides everything needed to run Java applications. Includes the JVM plus standard libraries (like `java.lang`, `java.util`). End users only need JRE to run programs.

**JDK (Java Development Kit)**  
Complete toolkit for developers. Contains JRE plus development tools like:
- `javac` (compiler: `.java` → `.class`)
- `javadoc` (documentation generator)
- `jar` (archive tool)
- Debugger and other utilities

**Write once, run anywhere** – Java compiles to platform-independent bytecode

![imagen](img.png)

---

## IntelliJ IDEA Shortcuts
*Essential keyboard shortcuts*

### Most Important

```
Ctrl + Space        Code completion
Alt + Enter         Quick fix / Show intentions
Ctrl + D            Duplicate line
Ctrl + Y            Delete line
Ctrl + /            Comment line
Ctrl + Alt + L      Reformat code
Shift + F10         Run
Shift + F9          Debug
Ctrl + F8           Toggle breakpoint
Ctrl + N            Search class
Ctrl + Shift + N    Search file
Shift + F6          Rename
Alt + Insert        Generate code (getter/setter/constructor)
```

### Live Templates (word + Tab)

```
psvm + Tab          public static void main(String[] args)
sout + Tab          System.out.println()
soutv + Tab         System.out.println("variable = " + variable)
fori + Tab          for (int i = 0; i < ; i++)
iter + Tab          for (Type item : collection)
ifn + Tab           if (var == null)
inn + Tab           if (var != null)
```

**Note**: macOS users replace `Ctrl` with `Cmd`, `Alt` with `Option`

---

## Naming Conventions
*Standard rules for naming in Java*

### Packages
*Organize and group related classes*

```java
// Rules:
// - All lowercase
// - Reverse domain name notation
// - Use dots to separate levels

com.company.project          // ✓ correct
com.mycompany.myapp.utils    // ✓ correct
MyPackage                    // ✗ wrong (uppercase)
com.Company.Project          // ✗ wrong (uppercase)
```

### Classes
*Use PascalCase (UpperCamelCase)*

```java
// Rules:
// - Start with uppercase letter
// - Capitalize first letter of each word
// - Use nouns

class Car                    // ✓ correct
class UserAccount            // ✓ correct
class BankTransaction        // ✓ correct
class car                    // ✗ wrong (lowercase)
class user_account           // ✗ wrong (underscores)
```

### Variables
*Use camelCase*

```java
// Rules:
// - Start with lowercase letter
// - Capitalize first letter of subsequent words
// - Use descriptive names

int age;                     // ✓ correct
String firstName;            // ✓ correct
double accountBalance;       // ✓ correct
int Age;                     // ✗ wrong (uppercase start)
String first_name;           // ✗ wrong (underscores)
int x;                       // ✗ avoid (not descriptive)
```

### Constants
*Use UPPER_SNAKE_CASE*

```java
// Rules:
// - All uppercase
// - Underscores between words
// - Typically static final

static final int MAX_SIZE = 100;           // ✓ correct
static final String API_KEY = "abc123";    // ✓ correct
static final double PI = 3.14159;          // ✓ correct
static final int maxSize = 100;            // ✗ wrong (lowercase)
static final String ApiKey = "abc123";     // ✗ wrong (mixed case)
```

### Methods
*Use camelCase (verbs)*

```java
// Rules:
// - Start with lowercase letter
// - Use verbs or verb phrases
// - Capitalize subsequent words

void calculateTotal()        // ✓ correct
String getName()             // ✓ correct
boolean isValid()            // ✓ correct
void CalculateTotal()        // ✗ wrong (uppercase start)
void calculate_total()       // ✗ wrong (underscores)
```

### Boolean Variables
*Use question-like prefixes*

```java
// Prefixes: is, has, can, should

boolean isActive;            // ✓ correct
boolean hasPermission;       // ✓ correct
boolean canEdit;             // ✓ correct
boolean shouldUpdate;        // ✓ correct
boolean active;              // ✗ less clear
```

### Summary Table

| Element    | Convention       | Example              |
|------------|------------------|----------------------|
| Package    | lowercase        | `com.company.app`    |
| Class      | PascalCase       | `UserAccount`        |
| Variable   | camelCase        | `firstName`          |
| Constant   | UPPER_SNAKE_CASE | `MAX_SIZE`           |
| Method     | camelCase        | `calculateTotal()`   |
| Boolean    | is/has/can       | `isActive`           |

---

## Fundamentals
*Basic building blocks of Java*

### Data Types
*Variables and their value types*

```java
// Primitives
int n;           // integer
double d;        // decimal
boolean b;       // true/false
char c;          // single character
long l;          // large integer
float f;         // less precise decimal
short s;         // small integer
byte bt;         // tiny integer

// Reference types
String text;     // text
LocalDate date;  // date
int[] arr;       // array
Object obj;      // generic object
```

### Type Conversion
*Converting values between types*

```java
// Implicit (widening)
int x = 10;
double y = x;    // int → double

// Explicit (narrowing)
double z = 9.78;
int w = (int) z; // double → int (loses decimal)
```

### Input
*Reading user data from console*

```java
Scanner sc = new Scanner(System.in);
String name = sc.nextLine();    // text
int age = sc.nextInt();         // number
sc.close();
```

---

### File I/O
*Reading and writing files*

```java
// Read entire file
String content = Files.readString(Path.of("file.txt"));

// Read line by line
List<String> lines = Files.readAllLines(Path.of("file.txt"));

// Read with BufferedReader
try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
    String line;
    while ((line = br.readLine()) != null) {
        System.out.println(line);
    }
} catch (IOException e) {
    e.printStackTrace();
}

// Write to file
Files.writeString(Path.of("output.txt"), "Hello World");
List<String> lines = List.of("line1", "line2", "line3");
Files.write(Path.of("output.txt"), lines);

// Append to file
Files.writeString(Path.of("file.txt"), "new content", 
    StandardOpenOption.APPEND);

// Check if file exists
boolean exists = Files.exists(Path.of("file.txt"));

// Delete file
Files.delete(Path.of("file.txt"));
```

---

### Memory Model
*How Java stores data in memory*

**Stack** – Stores primitives and references (limited size)  
**Heap** – Stores objects (dynamic, managed by GC)

Primitives are stored directly in the stack, while objects are stored in the heap and their references in the stack

```java
// Primitives: copy value
int a = 10;
int b = a;      // b is independent copy

// Objects: copy reference
String s1 = new String("Hi");
String s2 = s1; // both point to same object
s1 = null;      // s2 still exists
```

---

## Control Flow
*Decision making and repetition*

### Conditionals
*Execute code based on conditions*

```java
// if-else
if (age >= 18) {
    // adult
} else if (age >= 13) {
    // teen
} else {
    // child
}

// Ternary
String result = (age >= 18) ? "adult" : "minor";

// Switch
switch (day) {
    case "Mon", "Fri" -> System.out.println("edge day");
    default -> System.out.println("midweek");
}
```

### Operators
*Compare and combine conditions*

```java
// Comparison
==  !=  >  <  >=  <=

// Logical
&&  (and)
||  (or)
!   (not)
```

### Loops
*Repeat code multiple times*

```java
// while
while (i < 5) {
    System.out.println(i++);
}

// do-while (runs at least once)
do {
    System.out.println(i++);
} while (i < 5);

// for
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

// for-each
int[] nums = {1, 2, 3};
for (int n : nums) {
    System.out.println(n);
}

// Control
continue;  // skip iteration
break;     // exit loop
```

---

## Collections
*Storing and managing groups of data*

### Lists
*Ordered sequences with duplicates allowed*

**Dynamic ordered collection allowing duplicates**

```java
// Creation
List<String> list = new ArrayList<>();           // fast access
List<String> list = new LinkedList<>();          // fast insert/delete
List<String> list = List.of("a", "b");           // immutable
List<String> copy = new ArrayList<>(list);       // mutable copy

// Common operations
list.add("item");           // append
list.add(1, "item");        // insert at index
list.get(0);                // read
list.set(0, "new");         // update
list.remove(0);             // delete
list.size();                // length
list.contains("item");      // check
list.clear();               // empty

// Iteration
for (int i = 0; i < list.size(); i++) {}        // indexed
for (String item : list) {}                     // for-each
list.forEach(item -> System.out.println(item)); // lambda

// Sorting
Collections.sort(list);                              // ascending
list.sort(Comparator.reverseOrder());                // descending
list.sort(Comparator.comparingInt(String::length));  // custom

// Conversion
List<String> l = new ArrayList<>(Arrays.asList("a", "b"));
String[] arr = l.toArray(new String[0]);
```

---

### Maps
*Key-value pairs*

**Store data as key-value associations**

```java
// Creation
Map<String, Integer> map = new HashMap<>();           // fast, unordered
Map<String, Integer> map = new LinkedHashMap<>();     // insertion order
Map<String, Integer> map = new TreeMap<>();           // sorted by key
Map<String, Integer> map = Map.of("a", 1, "b", 2);    // immutable

// Common operations
map.put("key", 100);           // add/update
map.get("key");                // read (returns null if not found)
map.getOrDefault("key", 0);    // read with default
map.remove("key");             // delete
map.containsKey("key");        // check key exists
map.containsValue(100);        // check value exists
map.size();                    // number of entries
map.clear();                   // remove all

// Iteration
for (String key : map.keySet()) {
    System.out.println(key + ": " + map.get(key));
}

for (Map.Entry<String, Integer> entry : map.entrySet()) {
    System.out.println(entry.getKey() + ": " + entry.getValue());
}

map.forEach((key, value) -> System.out.println(key + ": " + value));

// Useful methods
map.putIfAbsent("key", 100);   // add only if key doesn't exist
map.replace("key", 200);       // update if key exists
map.merge("key", 1, Integer::sum);  // combine values
```

---

## Functional Programming
*Process data with functions and streams*

### Lambdas
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

### Streams
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
// Traditional class
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

---

## Exceptions
*Handle errors and exceptional situations*

### Exception Types
*Checked vs Unchecked*

**Checked Exceptions** – Must be handled or declared (compile-time)  
**Unchecked Exceptions** – Optional to handle (runtime)

```java
// Checked exceptions (must handle)
IOException
SQLException
FileNotFoundException
ClassNotFoundException

// Unchecked exceptions (optional)
NullPointerException
ArrayIndexOutOfBoundsException
ArithmeticException
IllegalArgumentException
```

---

### Try-Catch
*Handle exceptions*

```java
// Basic try-catch
try {
    int result = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Cannot divide by zero");
}

// Multiple catch blocks
try {
    String text = null;
    text.length();
} catch (NullPointerException e) {
    System.out.println("Null value");
} catch (Exception e) {
    System.out.println("Other error");
}

// Finally (always executes)
try {
    // code
} catch (Exception e) {
    // handle error
} finally {
    // cleanup (always runs)
}

// Try-with-resources (auto-close)
try (Scanner sc = new Scanner(System.in)) {
    String input = sc.nextLine();
} catch (Exception e) {
    System.out.println("Error reading input");
}
```

---

### Throw and Throws
*Propagate exceptions*

```java
// Throw exception
void checkAge(int age) {
    if (age < 18) {
        throw new IllegalArgumentException("Too young");
    }
}

// Throws declaration (checked exceptions)
void readFile() throws IOException {
    FileReader file = new FileReader("file.txt");
}

// Custom exception
class InvalidUserException extends Exception {
    InvalidUserException(String message) {
        super(message);
    }
}

void validateUser(String name) throws InvalidUserException {
    if (name == null) {
        throw new InvalidUserException("Name cannot be null");
    }
}
```

---


## Object-Oriented Programming
*Organizing code around objects and their interactions*

### Core Concepts
*Fundamental OOP principles*

**Object** – Entity combining data (state) and operations (behavior)

**Benefits**: Reusability, Maintainability, Modifiability, Reliability

**Four Pillars**: Abstraction, Encapsulation, Inheritance, Polymorphism

---

### Classes and Objects
*Blueprints and instances*

**Class** – Template defining structure and behavior  
**Object** – Instance of a class with its own state

```java
class Car {
    String model;
    int year;

    Car(String model, int year) {
        this.model = model;
        this.year = year;
    }

    void drive() {
        System.out.println(model + " is driving");
    }
}

// Each object has its own state
Car car1 = new Car("Tesla", 2024);
Car car2 = new Car("BMW", 2023);
car1.drive();
```

---

### Constructors
*Initialize objects when created*

**Rules** – Same name as class, no return type

```java
class Person {
    String name;
    int age;

    Person() {                          // default
        this.name = "Unknown";
        this.age = 0;
    }

    Person(String name, int age) {      // parameterized
        this.name = name;
        this.age = age;
    }

    Person(String name) {               // overloaded
        this.name = name;
        this.age = 18;
    }
}
```

---

### State and Behavior
*What objects know and do*

**State** – Data stored in object  
**Behavior** – Actions object performs

```java
class BankAccount {
    private double balance;      // STATE

    BankAccount() {
        this.balance = 0.0;
    }

    void deposit(double amount) {    // BEHAVIOR
        this.balance += amount;
    }

    double getBalance() {
        return this.balance;
    }
}
```

---

### Attributes and Methods
*Object data and actions*

```java
class Example {
    // Instance - each object has its own
    public String name;
    private int age;

    // Static - shared by all instances
    public static int count;
    public static final int MAX = 100;

    Example(String name, int age) {
        this.name = name;
        this.age = age;
        count++;
    }

    // Instance method
    public void celebrate() {
        this.age++;
    }

    // Static method
    public static int getCount() {
        return count;
    }
}
```

---

### Encapsulation
*Protecting and controlling data access*

**Access Modifiers**:
- `public` – accessible everywhere
- `private` – only within this class
- `protected` – within package + subclasses
- (default) – within package only

```java
class User {
    public String username;
    private String password;

    // Getter
    public String getPassword() {
        return password;
    }

    // Setter with validation
    public void setPassword(String password) {
        if (password.length() >= 8) {
            this.password = password;
        }
    }
}

// Usage
User user = new User();
user.username = "alice";              // direct
user.setPassword("secret123");        // controlled
```

**Best Practice** – `private` attributes, `public` getters/setters

---

### `this` Keyword
*Reference to current object*

```java
class Product {
    String name;
    double price;

    Product(String name, double price) {
        this.name = name;       // distinguish parameter from attribute
        this.price = price;
    }

    Product(String name) {
        this(name, 0.0);        // call another constructor
    }

    Product setName(String name) {
        this.name = name;
        return this;            // method chaining
    }
}
```

---

### Relationships
*How classes connect and depend on each other*

**Association** – Independent existence  
**Aggregation** – Weak ownership, child can exist alone  
**Composition** – Strong ownership, child bound to parent

```java
// ASSOCIATION
class Student {
    Teacher teacher;  // knows about teacher
    
    Student(Teacher teacher) {
        this.teacher = teacher;  // teacher exists independently
    }
}

// AGGREGATION
class Car {
    Engine engine;  // has engine
    
    Car(Engine engine) {
        this.engine = engine;  // engine created outside
    }
}

// COMPOSITION
class House {
    Room room;  // owns room
    
    House() {
        this.room = new Room();  // room created inside
    }
}
```

**Summary**: Association → knows | Aggregation → has | Composition → owns

---

### Inheritance
*Reuse code through parent-child relationships*

**Extends** – Child inherits parent's attributes and methods  
**Super** – Reference to parent class

```java
// Parent class
class Animal {
    String name;
    
    Animal(String name) {
        this.name = name;
    }
    
    void eat() {
        System.out.println(name + " is eating");
    }
}

// Child class (inherits from Animal)
class Dog extends Animal {
    String breed;
    
    Dog(String name, String breed) {
        super(name);  // call parent constructor
        this.breed = breed;
    }
    
    // Override parent method
    @Override
    void eat() {
        System.out.println(name + " is eating dog food");
    }
    
    // New method
    void bark() {
        System.out.println(name + " is barking");
    }
}

// Usage
Dog dog = new Dog("Max", "Golden");
dog.eat();   // "Max is eating dog food" (overridden)
dog.bark();  // "Max is barking" (new method)
```

**Method Overriding**:
- Same signature as parent method
- Use `@Override` annotation
- `super.method()` calls parent version

**Final** – Prevent inheritance or overriding
```java
final class CannotExtend { }           // cannot be extended
class Parent {
    final void cannotOverride() { }    // cannot be overridden
}
```

**Abstract** – Force child classes to implement
```java
abstract class Shape {
    abstract double area();  // no implementation
}

class Circle extends Shape {
    double radius;
    
    @Override
    double area() {
        return Math.PI * radius * radius;
    }
}
```

---

### Polymorphism
*One interface, multiple implementations*

**Compile-time (Overloading)** – Same method name, different parameters  
**Runtime (Overriding)** – Parent reference, child object

```java
// METHOD OVERLOADING (compile-time)
class Calculator {
    int add(int a, int b) {
        return a + b;
    }
    
    double add(double a, double b) {
        return a + b;
    }
    
    int add(int a, int b, int c) {
        return a + b + c;
    }
}

// RUNTIME POLYMORPHISM
class Animal {
    void sound() {
        System.out.println("Animal makes sound");
    }
}

class Dog extends Animal {
    @Override
    void sound() {
        System.out.println("Dog barks");
    }
}

class Cat extends Animal {
    @Override
    void sound() {
        System.out.println("Cat meows");
    }
}

// Usage - parent reference, child object
Animal animal1 = new Dog();
Animal animal2 = new Cat();
animal1.sound();  // "Dog barks"
animal2.sound();  // "Cat meows"

// Polymorphism with arrays
Animal[] animals = {new Dog(), new Cat(), new Dog()};
for (Animal a : animals) {
    a.sound();  // calls appropriate method for each object
}
```

**Interfaces** – Pure abstraction (all methods abstract)
```java
interface Drawable {
    void draw();  // public abstract by default
}

class Circle implements Drawable {
    @Override
    public void draw() {
        System.out.println("Drawing circle");
    }
}

class Square implements Drawable {
    @Override
    public void draw() {
        System.out.println("Drawing square");
    }
}

// Polymorphism with interface
Drawable shape = new Circle();
shape.draw();  // "Drawing circle"
```

**instanceof** – Check object type
```java
Animal animal = new Dog();

if (animal instanceof Dog) {
    System.out.println("It's a dog");
    Dog dog = (Dog) animal;  // safe cast
    dog.bark();
}

// Pattern matching (Java 16+)
if (animal instanceof Dog dog) {
    dog.bark();  // auto-cast
}

// Usage with polymorphism
Animal[] animals = {new Dog(), new Cat(), new Dog()};
for (Animal a : animals) {
    if (a instanceof Dog) {
        System.out.println("Found a dog");
    }
}
```

---

### Interfaces
*Contract for what a class must do*

**Purpose** – Define behavior without implementation  
**Rules** – All methods public abstract by default, can have default/static methods

```java
// Basic interface
interface Drawable {
    void draw();           // public abstract (implicit)
    void resize(int size);
}

class Circle implements Drawable {
    @Override
    public void draw() {
        System.out.println("Drawing circle");
    }
    
    @Override
    public void resize(int size) {
        System.out.println("Resizing to " + size);
    }
}

// Multiple interfaces
interface Movable {
    void move(int x, int y);
}

class Player implements Drawable, Movable {
    @Override
    public void draw() { }
    
    @Override
    public void move(int x, int y) { }
}

// Default methods (Java 8+)
interface Vehicle {
    void start();
    
    default void stop() {
        System.out.println("Vehicle stopped");
    }
}

class Car implements Vehicle {
    @Override
    public void start() {
        System.out.println("Car started");
    }
    // stop() inherited from interface
}

// Static methods
interface MathUtils {
    static int add(int a, int b) {
        return a + b;
    }
}

int result = MathUtils.add(5, 3);  // call without instance

// Constants (public static final by default)
interface Constants {
    int MAX_SIZE = 100;
    String APP_NAME = "MyApp";
}
```

**Interface vs Abstract Class**:
- Interface: multiple inheritance, no state
- Abstract: single inheritance, can have state

### Casting

*Converting one type into another*

```java
// Primitive casting

// Implicit (automatic)
int a = 10;
double b = a;        // int → double

// Explicit (manual)
double x = 10.5;
int y = (int) x;     // double → int
```

```java
// Object casting (inheritance)

// Upcasting (automatic)
Animal a = new Dog();

// Downcasting (manual)
Dog d = (Dog) a;
```

---

### Decoupling

*Reducing dependency between classes*

```java
// ❌ Tightly coupled
class Car {
    Engine engine = new Engine();
}
```

```java
// ✅ Decoupled (using interface)
interface Engine {
    void start();
}

class Car {
    private Engine engine;

    public Car(Engine engine) {
        this.engine = engine;
    }
}
```


## Entry Point
*Where your program begins*

```java
public class Main {
    public static void main(String[] args) {
        // Program starts here
    }
}
```

Only code inside `main()` runs automatically. Other methods and classes execute when called from `main()`.