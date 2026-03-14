# Concurrency
*Run code in parallel and manage shared state*

## Threads

```java
// Option 1: extend Thread
class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println("Running in: " + Thread.currentThread().getName());
    }
}

MyThread t = new MyThread();
t.start();   // start (don't call run() directly)

// Option 2: implement Runnable (preferred)
Runnable task = () -> System.out.println("Task running");
Thread t = new Thread(task);
t.start();

// Thread info
Thread.currentThread().getName();   // thread name
Thread.sleep(1000);                 // pause 1 second (throws InterruptedException)
t.join();                           // wait for thread to finish
t.isAlive();                        // is thread running?
```

---

## ExecutorService
*Thread pool — preferred over creating raw threads*

```java
import java.util.concurrent.*;

// Fixed thread pool
ExecutorService executor = Executors.newFixedThreadPool(4);

// Submit tasks
executor.execute(() -> System.out.println("task"));  // fire and forget

Future<Integer> future = executor.submit(() -> {
    return 42;  // returns a result
});

Integer result = future.get();  // blocks until done

// Shutdown (always do this)
executor.shutdown();             // wait for tasks to finish
executor.shutdownNow();          // interrupt running tasks

// Common pool types
Executors.newFixedThreadPool(n);      // n threads
Executors.newCachedThreadPool();      // grows as needed
Executors.newSingleThreadExecutor();  // 1 thread, sequential
Executors.newScheduledThreadPool(n);  // for scheduled tasks
```

---

## Synchronized
*Prevent concurrent access to shared data*

```java
class Counter {
    private int count = 0;

    // synchronized method – only one thread at a time
    public synchronized void increment() {
        count++;
    }

    // synchronized block – finer control
    public void add(int n) {
        synchronized (this) {
            count += n;
        }
    }

    public int getCount() { return count; }
}

// Atomic types (faster than synchronized for simple ops)
import java.util.concurrent.atomic.*;

AtomicInteger counter = new AtomicInteger(0);
counter.incrementAndGet();   // thread-safe ++
counter.addAndGet(5);        // thread-safe +=
counter.get();               // read
```

---

## volatile
*Ensure visibility of variable across threads*

```java
class Worker {
    private volatile boolean running = true;  // visible to all threads

    void stop() {
        running = false;
    }

    void run() {
        while (running) {
            // work...
        }
    }
}
// Use volatile for flags; use synchronized/atomic for compound operations
```

---

## CompletableFuture
*Async programming without blocking*

```java
import java.util.concurrent.*;

// Run async (no return value)
CompletableFuture.runAsync(() -> {
    System.out.println("async task");
});

// Supply async (with return value)
CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> {
    return "result";
});

// Chain operations
CompletableFuture<Integer> result = CompletableFuture
    .supplyAsync(() -> "hello")
    .thenApply(s -> s.length())        // transform result
    .thenApply(n -> n * 2);

result.get();  // 10

// Consume result
future.thenAccept(s -> System.out.println(s));

// Combine two futures
CompletableFuture<String> f1 = CompletableFuture.supplyAsync(() -> "Hello");
CompletableFuture<String> f2 = CompletableFuture.supplyAsync(() -> "World");

f1.thenCombine(f2, (a, b) -> a + " " + b)
  .thenAccept(System.out::println);  // "Hello World"

// Wait for all
CompletableFuture.allOf(f1, f2).join();

// Handle errors
future
    .thenApply(s -> s.toUpperCase())
    .exceptionally(e -> "default on error")
    .thenAccept(System.out::println);
```
