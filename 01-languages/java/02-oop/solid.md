# SOLID Principles
*Five design principles for maintainable OOP code*

## S – Single Responsibility
*A class should have only one reason to change*

```java
// ❌ Too many responsibilities
class User {
    void saveToDatabase() { }
    void sendEmail() { }
    void generateReport() { }
}

// ✅ Each class has one job
class User { }

class UserRepository {
    void save(User user) { }
}

class EmailService {
    void sendWelcomeEmail(User user) { }
}

class ReportGenerator {
    void generate(User user) { }
}
```

---

## O – Open/Closed
*Open for extension, closed for modification*

```java
// ❌ Must modify existing class for each new shape
class AreaCalculator {
    double calculate(Object shape) {
        if (shape instanceof Circle c) return Math.PI * c.radius * c.radius;
        if (shape instanceof Rectangle r) return r.width * r.height;
        // adding Triangle requires modifying this method
    }
}

// ✅ Extend without modifying
interface Shape {
    double area();
}

class Circle implements Shape {
    double radius;
    public double area() { return Math.PI * radius * radius; }
}

class Rectangle implements Shape {
    double width, height;
    public double area() { return width * height; }
}

// Adding Triangle: just create a new class, nothing changes
class Triangle implements Shape {
    double base, height;
    public double area() { return 0.5 * base * height; }
}
```

---

## L – Liskov Substitution
*Subclasses must be substitutable for their parent*

```java
// ❌ Subclass breaks parent contract
class Bird {
    void fly() { System.out.println("flying"); }
}

class Penguin extends Bird {
    @Override
    void fly() { throw new UnsupportedOperationException("can't fly"); }
}

// ✅ Model hierarchy correctly
interface Flyable {
    void fly();
}

class Sparrow implements Flyable {
    public void fly() { System.out.println("flying"); }
}

class Penguin {
    void swim() { System.out.println("swimming"); }
}
// Rule: if S extends P, then P can always be replaced by S without issues
```

---

## I – Interface Segregation
*Don't force classes to implement methods they don't need*

```java
// ❌ Fat interface
interface Worker {
    void work();
    void eat();
    void sleep();
}

class Robot implements Worker {
    public void work() { }
    public void eat() { }    // robots don't eat!
    public void sleep() { }  // robots don't sleep!
}

// ✅ Small, focused interfaces
interface Workable {
    void work();
}

interface Eatable {
    void eat();
}

class Human implements Workable, Eatable {
    public void work() { }
    public void eat() { }
}

class Robot implements Workable {
    public void work() { }
}
```

---

## D – Dependency Inversion
*Depend on abstractions, not concrete implementations*

```java
// ❌ High-level class depends on low-level class
class OrderService {
    MySQLDatabase db = new MySQLDatabase();  // tightly coupled

    void save(Order order) {
        db.insert(order);
    }
}

// ✅ Depend on interface
interface Database {
    void insert(Order order);
}

class MySQLDatabase implements Database {
    public void insert(Order order) { }
}

class PostgresDatabase implements Database {
    public void insert(Order order) { }
}

class OrderService {
    private final Database db;

    OrderService(Database db) {  // inject dependency
        this.db = db;
    }

    void save(Order order) {
        db.insert(order);
    }
}

// Usage
OrderService service = new OrderService(new MySQLDatabase());
OrderService service = new OrderService(new PostgresDatabase()); // easy to swap
```
