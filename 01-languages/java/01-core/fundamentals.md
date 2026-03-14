# Java Fundamentals

### References
- https://www.w3schools.com/java/java_ref_reference.asp

---

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

## Naming Conventions
*Standard rules for naming in Java*

### Packages
```java
com.company.project          // ✓ correct
com.mycompany.myapp.utils    // ✓ correct
MyPackage                    // ✗ wrong (uppercase)
```

### Classes – PascalCase
```java
class Car                    // ✓ correct
class UserAccount            // ✓ correct
class car                    // ✗ wrong (lowercase)
```

### Variables – camelCase
```java
int age;                     // ✓ correct
String firstName;            // ✓ correct
int Age;                     // ✗ wrong (uppercase start)
```

### Constants – UPPER_SNAKE_CASE
```java
static final int MAX_SIZE = 100;           // ✓ correct
static final String API_KEY = "abc123";    // ✓ correct
```

### Methods – camelCase (verbs)
```java
void calculateTotal()        // ✓ correct
String getName()             // ✓ correct
```

### Boolean Variables – is/has/can/should prefix
```java
boolean isActive;            // ✓ correct
boolean hasPermission;       // ✓ correct
boolean canEdit;             // ✓ correct
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

## Data Types
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
```java
// Implicit (widening)
int x = 10;
double y = x;    // int → double

// Explicit (narrowing)
double z = 9.78;
int w = (int) z; // double → int (loses decimal)
```

---

## Strings
*Text manipulation*

```java
String s = "Hello World";

// Info
s.length();              // 11
s.charAt(0);             // 'H'
s.indexOf("World");      // 6
s.contains("Hello");     // true
s.isEmpty();             // false
s.isBlank();             // false (also checks whitespace)

// Transform
s.toUpperCase();         // "HELLO WORLD"
s.toLowerCase();         // "hello world"
s.trim();                // remove leading/trailing spaces
s.strip();               // like trim() but Unicode-aware
s.replace("Hello", "Hi"); // "Hi World"

// Extract
s.substring(6);          // "World"
s.substring(0, 5);       // "Hello"
s.split(" ");            // ["Hello", "World"]

// Compare
s.equals("Hello World");         // true (use this, not ==)
s.equalsIgnoreCase("hello world"); // true

// Check
s.startsWith("Hello");  // true
s.endsWith("World");    // true

// Build
String joined = String.join(", ", "a", "b", "c");  // "a, b, c"
String formatted = "Name: %s, Age: %d".formatted("Alice", 25);

// StringBuilder (mutable, efficient for concatenation)
StringBuilder sb = new StringBuilder();
sb.append("Hello");
sb.append(" World");
String result = sb.toString();  // "Hello World"
```

---

## Arrays
*Fixed-size ordered collection of elements*

```java
// Declaration and initialization
int[] nums = {1, 2, 3, 4, 5};
String[] names = new String[3];    // size 3, all null
int[] zeros = new int[5];          // size 5, all 0

// Access
nums[0];              // 1 (first)
nums[nums.length - 1]; // 5 (last)
nums.length;           // 5

// Modify
nums[0] = 10;

// Iterate
for (int n : nums) {
    System.out.println(n);
}

// Utility (java.util.Arrays)
Arrays.sort(nums);                          // sort in place
Arrays.toString(nums);                      // "[1, 2, 3, 4, 5]"
Arrays.fill(nums, 0);                       // fill all with 0
int[] copy = Arrays.copyOf(nums, nums.length);  // copy
Arrays.copyOfRange(nums, 1, 4);             // partial copy [1..3]

// 2D array
int[][] matrix = {{1, 2}, {3, 4}, {5, 6}};
matrix[0][1];  // 2
```

---

## Operators
*Arithmetic and assignment*

```java
// Arithmetic
+   -   *   /   %    // add, subtract, multiply, divide, modulo
10 / 3   // 3 (integer division)
10 % 3   // 1 (remainder)
10.0 / 3 // 3.333... (double division)

// Increment / Decrement
i++   // use then increment
++i   // increment then use
i--   // use then decrement
--i   // decrement then use

// Assignment shortcuts
x += 5;   // x = x + 5
x -= 5;
x *= 2;
x /= 2;
x %= 3;
```

---

## Wrapper Classes & Autoboxing
*Primitive types as objects*

Each primitive has a wrapper class — needed for collections and generics.

| Primitive | Wrapper   |
|-----------|-----------|
| `int`     | `Integer` |
| `double`  | `Double`  |
| `boolean` | `Boolean` |
| `char`    | `Character` |
| `long`    | `Long`    |
| `float`   | `Float`   |

```java
// Autoboxing – primitive → wrapper (automatic)
int n = 5;
Integer obj = n;           // auto-boxed

// Unboxing – wrapper → primitive (automatic)
Integer obj = 42;
int n = obj;               // auto-unboxed

// Useful static methods
Integer.parseInt("42");        // String → int
Integer.toString(42);          // int → String
Integer.MAX_VALUE;             // 2147483647
Integer.MIN_VALUE;             // -2147483648
Double.parseDouble("3.14");    // String → double
Character.isDigit('5');        // true
Character.isLetter('a');       // true
Character.toUpperCase('a');    // 'A'

// Collections need wrappers, not primitives
List<Integer> nums = new ArrayList<>();  // not List<int>
nums.add(5);   // autoboxing happens here
int x = nums.get(0);  // unboxing happens here
```

---

## Varargs
*Variable number of arguments*

```java
// Declare with ...
void printAll(String... words) {
    for (String w : words) {
        System.out.println(w);
    }
}

// Call with any number of args
printAll("hello");
printAll("a", "b", "c");
printAll();  // zero args also valid

// Varargs is just an array internally
int sum(int... nums) {
    int total = 0;
    for (int n : nums) total += n;
    return total;
}

// Must be the last parameter
void log(String level, String... messages) { }
```

---

## Packages & Imports
*Organize and reuse code across files*

```java
// Declare package (top of file, matches folder structure)
package com.company.project;

// Import a specific class
import java.util.ArrayList;
import java.util.List;

// Import all classes from a package
import java.util.*;

// Static import (use static members without class name)
import static java.lang.Math.PI;
import static java.lang.Math.*;

double area = PI * r * r;   // instead of Math.PI
double x = sqrt(16);        // instead of Math.sqrt(16)

// java.lang is imported automatically (String, Math, System, etc.)
```

---

## Text Blocks (Java 15+)
*Multiline strings without escape characters*

```java
// Traditional string (ugly escaping)
String json = "{\n  \"name\": \"Alice\",\n  \"age\": 25\n}";

// Text block (clean)
String json = """
        {
          "name": "Alice",
          "age": 25
        }
        """;

// SQL example
String query = """
        SELECT *
        FROM users
        WHERE age > 18
        ORDER BY name
        """;

// Indentation is relative to the closing """
// Trailing newline is included; to remove it, put """ on last line:
String noTrailingNewline = """
        hello""";
```

---

## `var` – Type Inference (Java 10+)
*Let the compiler infer the type*

```java
var name = "Alice";         // String
var age = 25;               // int
var list = new ArrayList<String>();  // ArrayList<String>

// Only works for local variables
// Cannot be used for fields, parameters, or return types
```

---

## Input
*Reading user data from console*

```java
Scanner sc = new Scanner(System.in);
String name = sc.nextLine();    // text
int age = sc.nextInt();         // number
sc.close();
```

---

## Memory Model
*How Java stores data in memory*

**Stack** – Stores primitives and references (limited size)
**Heap** – Stores objects (dynamic, managed by GC)

Primitives are stored directly in the stack, while objects are stored in the heap and their references in the stack.

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
