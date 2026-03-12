# Exceptions
*Handle errors and exceptional situations*

## Exception Types
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

## Try-Catch

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

## Throw and Throws
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
