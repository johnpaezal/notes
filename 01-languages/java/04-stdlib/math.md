# Math
*Common mathematical operations*

```java
// Basic
Math.abs(-5);          // 5       (absolute value)
Math.max(3, 7);        // 7       (maximum)
Math.min(3, 7);        // 3       (minimum)

// Rounding
Math.round(3.5);       // 4       (rounds to nearest)
Math.floor(3.9);       // 3.0     (round down)
Math.ceil(3.1);        // 4.0     (round up)

// Power and roots
Math.pow(2, 10);       // 1024.0  (2 to the power of 10)
Math.sqrt(16);         // 4.0     (square root)
Math.cbrt(27);         // 3.0     (cube root)

// Logarithms
Math.log(Math.E);      // 1.0     (natural log)
Math.log10(100);       // 2.0     (log base 10)

// Trigonometry (radians)
Math.sin(Math.PI / 2); // 1.0
Math.cos(0);           // 1.0
Math.tan(Math.PI / 4); // 1.0

// Constants
Math.PI;               // 3.141592653589793
Math.E;                // 2.718281828459045

// Random (0.0 inclusive to 1.0 exclusive)
Math.random();                            // e.g. 0.742...
(int)(Math.random() * 10);               // 0–9
(int)(Math.random() * 10) + 1;           // 1–10

// Preferred: java.util.Random
Random rng = new Random();
rng.nextInt(10);       // 0–9
rng.nextInt(1, 11);    // 1–10  (Java 17+)
rng.nextDouble();      // 0.0–1.0
rng.nextBoolean();
```
