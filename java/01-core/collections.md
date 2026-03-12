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
