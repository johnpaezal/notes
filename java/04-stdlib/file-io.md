# File I/O
*Reading and writing files*

```java
// Read entire file
String content = Files.readString(Path.of("file.txt"));

// Read line by line
List<String> lines = Files.readAllLines(Path.of("file.txt"));

// Read with BufferedReader
try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
    String line;
    while ((line = br.readLine()) != null) {
        System.out.println(line);
    }
} catch (IOException e) {
    e.printStackTrace();
}

// Write to file
Files.writeString(Path.of("output.txt"), "Hello World");
List<String> lines = List.of("line1", "line2", "line3");
Files.write(Path.of("output.txt"), lines);

// Append to file
Files.writeString(Path.of("file.txt"), "new content",
    StandardOpenOption.APPEND);

// Check if file exists
boolean exists = Files.exists(Path.of("file.txt"));

// Delete file
Files.delete(Path.of("file.txt"));
```
