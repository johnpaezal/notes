# Control Flow
*Decision making and repetition*

## Conditionals
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

// Switch (statement)
switch (day) {
    case "Mon", "Fri" -> System.out.println("edge day");
    default -> System.out.println("midweek");
}

// Switch expression (returns a value, Java 14+)
String label = switch (day) {
    case "Mon" -> "Monday";
    case "Fri" -> "Friday";
    default -> "Other";
};

// Switch expression with block
int result = switch (status) {
    case 1 -> 100;
    case 2 -> {
        int x = 200;
        yield x * 2;   // yield returns the value from a block
    }
    default -> 0;
};
```

---

## Operators
*Compare and combine conditions*

```java
// Comparison
==  !=  >  <  >=  <=

// Logical
&&  (and)
||  (or)
!   (not)
```

---

## Loops
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
