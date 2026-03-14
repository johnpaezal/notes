# HttpClient
*Make HTTP requests — built-in since Java 11*

## Setup

```java
import java.net.http.*;
import java.net.URI;
```

---

## GET Request

```java
HttpClient client = HttpClient.newHttpClient();

HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://api.example.com/users"))
    .header("Accept", "application/json")
    .GET()
    .build();

// Synchronous (blocking)
HttpResponse<String> response = client.send(
    request,
    HttpResponse.BodyHandlers.ofString()
);

response.statusCode();  // 200
response.body();        // response body as String
response.headers();     // response headers
```

---

## POST Request

```java
String json = """
        {"name": "Alice", "age": 25}
        """;

HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://api.example.com/users"))
    .header("Content-Type", "application/json")
    .POST(HttpRequest.BodyPublishers.ofString(json))
    .build();

HttpResponse<String> response = client.send(
    request,
    HttpResponse.BodyHandlers.ofString()
);
```

---

## Async Request

```java
client.sendAsync(request, HttpResponse.BodyHandlers.ofString())
    .thenApply(HttpResponse::body)
    .thenAccept(System.out::println)
    .join();  // wait for completion
```

---

## HttpClient Configuration

```java
HttpClient client = HttpClient.newBuilder()
    .connectTimeout(Duration.ofSeconds(10))
    .followRedirects(HttpClient.Redirect.NORMAL)
    .build();
```

---

## Common Response Codes

```
200  OK
201  Created
400  Bad Request
401  Unauthorized
403  Forbidden
404  Not Found
500  Internal Server Error
```
