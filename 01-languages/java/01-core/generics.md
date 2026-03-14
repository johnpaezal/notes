# Generics
*Write type-safe code that works with any type*

## Generic Classes

```java
// Define a generic class with type parameter T
class Box<T> {
    private T value;

    Box(T value) {
        this.value = value;
    }

    T get() {
        return value;
    }
}

// Use with any type
Box<String> strBox = new Box<>("hello");
Box<Integer> intBox = new Box<>(42);

strBox.get();  // "hello"
intBox.get();  // 42

// Multiple type parameters
class Pair<A, B> {
    A first;
    B second;

    Pair(A first, B second) {
        this.first = first;
        this.second = second;
    }
}

Pair<String, Integer> pair = new Pair<>("age", 25);
```

---

## Generic Methods

```java
// Generic method (T declared before return type)
<T> T identity(T value) {
    return value;
}

<T> List<T> repeat(T item, int times) {
    List<T> list = new ArrayList<>();
    for (int i = 0; i < times; i++) list.add(item);
    return list;
}

// Call – type inferred automatically
String s = identity("hello");
List<Integer> nums = repeat(5, 3);  // [5, 5, 5]
```

---

## Bounded Types
*Restrict which types are allowed*

```java
// Upper bound – T must be Number or subclass
<T extends Number> double sum(List<T> list) {
    double total = 0;
    for (T n : list) total += n.doubleValue();
    return total;
}

sum(List.of(1, 2, 3));       // works (Integer extends Number)
sum(List.of(1.5, 2.5));      // works (Double extends Number)

// Multiple bounds
<T extends Comparable<T> & Cloneable> T max(T a, T b) {
    return a.compareTo(b) >= 0 ? a : b;
}
```

---

## Wildcards

```java
// ? – unknown type
List<?> list = new ArrayList<String>();

// Upper bounded wildcard – ? extends X (read-only)
void printAll(List<? extends Number> list) {
    for (Number n : list) {
        System.out.println(n);
    }
}

printAll(List.of(1, 2, 3));      // Integer
printAll(List.of(1.5, 2.5));     // Double

// Lower bounded wildcard – ? super X (write-friendly)
void addNumbers(List<? super Integer> list) {
    list.add(1);
    list.add(2);
}

// Rule of thumb:
// extends → use for reading (producer)
// super   → use for writing (consumer)
```

---

## Generics with Collections

```java
// Collections are generic by nature
List<String> names = new ArrayList<>();
Map<String, Integer> scores = new HashMap<>();

// Generic utility method
<T> void swap(List<T> list, int i, int j) {
    T temp = list.get(i);
    list.set(i, list.get(j));
    list.set(j, temp);
}
```

---

## Type Erasure
*Generics are compile-time only*

```java
// At runtime, generic types are erased
List<String> strings = new ArrayList<>();
List<Integer> ints = new ArrayList<>();

// Both become List at runtime
strings.getClass() == ints.getClass();  // true

// Cannot do:
// new T()           – can't instantiate generic type
// new T[]           – can't create generic array
// instanceof List<String>  – can't check generic type at runtime
```
