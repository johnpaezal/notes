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

// Create directories
Files.createDirectory(Path.of("mydir"));           // single directory
Files.createDirectories(Path.of("a/b/c"));         // nested directories

// List and walk
Files.list(Path.of("."))                           // direct children
    .forEach(System.out::println);

Files.walk(Path.of("."))                           // all files recursively
    .filter(Files::isRegularFile)
    .forEach(System.out::println);
```

---

## Paths
*Work with file and directory paths*

```java
Path path = Path.of("src/main/java/App.java");

path.getFileName();    // App.java
path.getParent();      // src/main/java
path.getRoot();        // / (or null if relative)
path.toString();       // "src/main/java/App.java"
path.toAbsolutePath(); // full absolute path

// Combine paths
Path base = Path.of("/home/user");
Path full = base.resolve("docs/file.txt"); // /home/user/docs/file.txt

// Relative path between two paths
Path from = Path.of("/home/user");
Path to = Path.of("/home/user/docs/file.txt");
from.relativize(to);   // docs/file.txt

// Check
Files.isRegularFile(path);
Files.isDirectory(path);
Files.isReadable(path);
Files.isWritable(path);
```
