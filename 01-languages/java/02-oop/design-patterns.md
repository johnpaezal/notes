# Design Patterns
*Reusable solutions to common software design problems*

## Creational Patterns

### Singleton
*Only one instance of a class exists*

```java
class Database {
    private static Database instance;

    private Database() { }  // private constructor

    public static Database getInstance() {
        if (instance == null) {
            instance = new Database();
        }
        return instance;
    }

    void query(String sql) { }
}

// Thread-safe version
class Database {
    private static volatile Database instance;

    public static Database getInstance() {
        if (instance == null) {
            synchronized (Database.class) {
                if (instance == null) {
                    instance = new Database();
                }
            }
        }
        return instance;
    }
}

Database db = Database.getInstance();
```

---

### Factory
*Create objects without specifying exact class*

```java
interface Notification {
    void send(String message);
}

class EmailNotification implements Notification {
    public void send(String message) {
        System.out.println("Email: " + message);
    }
}

class SmsNotification implements Notification {
    public void send(String message) {
        System.out.println("SMS: " + message);
    }
}

class NotificationFactory {
    static Notification create(String type) {
        return switch (type) {
            case "email" -> new EmailNotification();
            case "sms"   -> new SmsNotification();
            default -> throw new IllegalArgumentException("Unknown: " + type);
        };
    }
}

Notification n = NotificationFactory.create("email");
n.send("Hello!");
```

---

### Builder
*Construct complex objects step by step*

```java
class Person {
    private final String name;
    private final int age;
    private final String email;

    private Person(Builder builder) {
        this.name = builder.name;
        this.age = builder.age;
        this.email = builder.email;
    }

    static class Builder {
        private String name;
        private int age;
        private String email;

        Builder name(String name) { this.name = name; return this; }
        Builder age(int age) { this.age = age; return this; }
        Builder email(String email) { this.email = email; return this; }

        Person build() { return new Person(this); }
    }
}

Person p = new Person.Builder()
    .name("Alice")
    .age(25)
    .email("alice@example.com")
    .build();
```

---

## Structural Patterns

### Decorator
*Add behavior to objects without modifying their class*

```java
interface Coffee {
    String description();
    double cost();
}

class SimpleCoffee implements Coffee {
    public String description() { return "Coffee"; }
    public double cost() { return 1.0; }
}

// Decorator base
abstract class CoffeeDecorator implements Coffee {
    protected Coffee coffee;
    CoffeeDecorator(Coffee coffee) { this.coffee = coffee; }
}

class MilkDecorator extends CoffeeDecorator {
    MilkDecorator(Coffee coffee) { super(coffee); }
    public String description() { return coffee.description() + ", Milk"; }
    public double cost() { return coffee.cost() + 0.5; }
}

class SugarDecorator extends CoffeeDecorator {
    SugarDecorator(Coffee coffee) { super(coffee); }
    public String description() { return coffee.description() + ", Sugar"; }
    public double cost() { return coffee.cost() + 0.25; }
}

Coffee c = new SugarDecorator(new MilkDecorator(new SimpleCoffee()));
c.description();  // "Coffee, Milk, Sugar"
c.cost();         // 1.75
```

---

## Behavioral Patterns

### Strategy
*Swap algorithms at runtime*

```java
interface SortStrategy {
    void sort(int[] data);
}

class BubbleSort implements SortStrategy {
    public void sort(int[] data) { /* bubble sort */ }
}

class QuickSort implements SortStrategy {
    public void sort(int[] data) { /* quick sort */ }
}

class Sorter {
    private SortStrategy strategy;

    Sorter(SortStrategy strategy) {
        this.strategy = strategy;
    }

    void setStrategy(SortStrategy strategy) {
        this.strategy = strategy;
    }

    void sort(int[] data) {
        strategy.sort(data);
    }
}

Sorter sorter = new Sorter(new QuickSort());
sorter.sort(data);
sorter.setStrategy(new BubbleSort());  // swap at runtime
sorter.sort(data);
```

---

### Observer
*Notify multiple objects when state changes*

```java
import java.util.*;

interface Observer {
    void update(String event);
}

class EventBus {
    private List<Observer> observers = new ArrayList<>();

    void subscribe(Observer o) { observers.add(o); }
    void unsubscribe(Observer o) { observers.remove(o); }

    void publish(String event) {
        for (Observer o : observers) {
            o.update(event);
        }
    }
}

class Logger implements Observer {
    public void update(String event) {
        System.out.println("LOG: " + event);
    }
}

class AlertService implements Observer {
    public void update(String event) {
        System.out.println("ALERT: " + event);
    }
}

EventBus bus = new EventBus();
bus.subscribe(new Logger());
bus.subscribe(new AlertService());
bus.publish("user.login");  // both get notified
```
