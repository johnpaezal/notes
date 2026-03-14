# Collections
*Storing and managing groups of data*

## Lists
*Dynamic ordered collection allowing duplicates*

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

## Sets
*Unordered collection with no duplicates*

```java
// Creation
Set<String> set = new HashSet<>();          // fast, unordered
Set<String> set = new LinkedHashSet<>();    // insertion order
Set<String> set = new TreeSet<>();          // sorted
Set<String> set = Set.of("a", "b", "c");   // immutable

// Common operations
set.add("item");          // add (ignored if duplicate)
set.remove("item");       // delete
set.contains("item");     // check
set.size();               // count
set.clear();              // empty
set.isEmpty();            // true/false

// Iteration
for (String item : set) {
    System.out.println(item);
}

// Set operations
Set<String> a = new HashSet<>(Set.of("x", "y", "z"));
Set<String> b = new HashSet<>(Set.of("y", "z", "w"));

a.retainAll(b);  // intersection → {y, z}
a.addAll(b);     // union → {x, y, z, w}
a.removeAll(b);  // difference → {x}
```

---

## Queue / Deque
*FIFO and double-ended queues*

```java
// Queue (FIFO - first in, first out)
Queue<String> queue = new LinkedList<>();
queue.offer("first");    // add to back
queue.offer("second");
queue.poll();            // remove from front → "first"
queue.peek();            // look at front (no remove)
queue.isEmpty();

// Deque (double-ended - use as stack or queue)
Deque<String> deque = new ArrayDeque<>();

// As Queue (FIFO)
deque.offerLast("a");    // add to back
deque.pollFirst();       // remove from front

// As Stack (LIFO)
deque.push("a");         // add to top (front)
deque.pop();             // remove from top
deque.peek();            // look at top
```

---

## Comparable & Comparator
*Sort custom objects*

```java
// Comparable – the object defines its own natural order
class Student implements Comparable<Student> {
    String name;
    int grade;

    Student(String name, int grade) {
        this.name = name;
        this.grade = grade;
    }

    @Override
    public int compareTo(Student other) {
        return this.grade - other.grade;  // ascending by grade
        // return other.grade - this.grade;  // descending
        // return this.name.compareTo(other.name);  // alphabetical
    }
}

List<Student> students = new ArrayList<>();
Collections.sort(students);  // uses compareTo

// Comparator – external sorting logic (more flexible)
Comparator<Student> byName = Comparator.comparing(s -> s.name);
Comparator<Student> byGrade = Comparator.comparingInt(s -> s.grade);
Comparator<Student> byGradeDesc = Comparator.comparingInt(Student::getGrade).reversed();

// Chain comparators
Comparator<Student> byGradeThenName = Comparator
    .comparingInt(Student::getGrade)
    .thenComparing(Student::getName);

students.sort(byName);
students.sort(Comparator.comparingInt(s -> s.grade));
students.sort((a, b) -> a.name.compareTo(b.name));  // lambda
```

---

## Collections Utilities

```java
List<Integer> nums = new ArrayList<>(List.of(3, 1, 4, 1, 5, 9));

Collections.sort(nums);                    // sort ascending
Collections.reverse(nums);                 // reverse order
Collections.shuffle(nums);                 // random order
Collections.min(nums);                     // minimum value
Collections.max(nums);                     // maximum value
Collections.frequency(nums, 1);            // count occurrences of 1
Collections.nCopies(3, "hello");           // [hello, hello, hello]
Collections.unmodifiableList(nums);        // read-only wrapper
```

---

## Maps
*Store data as key-value associations*

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
map.putIfAbsent("key", 100);        // add only if key doesn't exist
map.replace("key", 200);            // update if key exists
map.merge("key", 1, Integer::sum);  // combine values
```

---

## PriorityQueue
*Processes elements by priority, not insertion order*

```java
// Min-heap by default (smallest element first)
PriorityQueue<Integer> pq = new PriorityQueue<>();
pq.offer(5);
pq.offer(1);
pq.offer(3);

pq.peek();   // 1 (look at min, don't remove)
pq.poll();   // 1 (remove min)
pq.poll();   // 3
pq.poll();   // 5

// Max-heap (largest first)
PriorityQueue<Integer> maxPq = new PriorityQueue<>(Comparator.reverseOrder());
maxPq.offer(5);
maxPq.offer(1);
maxPq.offer(3);
maxPq.poll();   // 5

// Custom objects
PriorityQueue<Task> tasks = new PriorityQueue<>(
    Comparator.comparingInt(t -> t.priority)
);

tasks.offer(new Task("low", 3));
tasks.offer(new Task("high", 1));
tasks.offer(new Task("mid", 2));

tasks.poll();   // Task{name=high, priority=1}

// Common operations
pq.size();
pq.isEmpty();
pq.contains(3);
pq.clear();
```

---

## Iterator & Iterable
*How for-each works internally*

```java
// Iterator – manually traverse a collection
List<String> list = List.of("a", "b", "c");
Iterator<String> it = list.iterator();

while (it.hasNext()) {
    String item = it.next();
    System.out.println(item);
}

// for-each is just syntactic sugar for Iterator
for (String item : list) { }  // same as above

// Implement Iterable to support for-each on custom classes
class Range implements Iterable<Integer> {
    private final int start, end;

    Range(int start, int end) {
        this.start = start;
        this.end = end;
    }

    @Override
    public Iterator<Integer> iterator() {
        return new Iterator<>() {
            int current = start;

            public boolean hasNext() { return current < end; }
            public Integer next() { return current++; }
        };
    }
}

// Now supports for-each
for (int n : new Range(1, 5)) {
    System.out.println(n);  // 1, 2, 3, 4
}
```
