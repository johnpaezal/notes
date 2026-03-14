# Testing with JUnit 5
*Write and run automated tests*

## Setup (Maven)

```xml
<dependency>
  <groupId>org.junit.jupiter</groupId>
  <artifactId>junit-jupiter</artifactId>
  <version>5.10.0</version>
  <scope>test</scope>
</dependency>
```

---

## Basic Test

```java
import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {

    @Test
    void addsTwoNumbers() {
        Calculator calc = new Calculator();
        assertEquals(5, calc.add(2, 3));
    }

    @Test
    void dividesNumbers() {
        assertEquals(2.5, calc.divide(5, 2));
    }

    @Test
    void throwsOnDivideByZero() {
        assertThrows(ArithmeticException.class, () -> calc.divide(5, 0));
    }
}
```

---

## Assertions

```java
assertEquals(expected, actual);             // equal values
assertNotEquals(unexpected, actual);
assertTrue(condition);
assertFalse(condition);
assertNull(value);
assertNotNull(value);
assertThrows(Exception.class, () -> ...);   // expects exception
assertDoesNotThrow(() -> ...);
assertAll(                                  // group assertions
    () -> assertEquals(1, x),
    () -> assertTrue(y > 0)
);
```

---

## Lifecycle Annotations

```java
@BeforeAll    // runs once before all tests (static method)
static void setup() { }

@BeforeEach   // runs before each test
void init() { }

@AfterEach    // runs after each test
void cleanup() { }

@AfterAll     // runs once after all tests (static method)
static void teardown() { }
```

---

## Other Annotations

```java
@Test                          // marks a test method
@Disabled("reason")            // skip this test
@DisplayName("description")    // custom test name in report

@ParameterizedTest             // run test with multiple inputs
@ValueSource(ints = {1, 2, 3})
void test(int n) {
    assertTrue(n > 0);
}

@ParameterizedTest
@CsvSource({"1,1,2", "2,3,5", "0,0,0"})
void addTest(int a, int b, int expected) {
    assertEquals(expected, calc.add(a, b));
}
```

---

## Test Naming Convention

```
src/test/java/
  com/company/
    CalculatorTest.java    // tests for Calculator.java
    UserServiceTest.java   // tests for UserService.java
```

Convention: `[ClassUnderTest]Test.java`
