# Spring Boot Basics
*Setup, auto-configuration, and first REST API*

## What is Spring Boot
*Convention-over-configuration web framework for Java*

**Spring Boot** – Opinionated Spring Framework wrapper; minimal config to build prod-ready apps  
**Auto-configuration** – Detects dependencies on classpath and configures beans automatically  
**Starter** – Curated dependency bundle (e.g., `spring-boot-starter-web` adds Tomcat + Spring MVC)  
**Embedded Server** – Tomcat/Jetty/Undertow bundled inside the JAR (no WAR deployment)  
**`@SpringBootApplication`** – Combines `@Configuration`, `@EnableAutoConfiguration`, `@ComponentScan`  

---

## Setup
*Create project with Spring Initializr*

```bash
# Via Spring Initializr CLI
curl https://start.spring.io/starter.zip \
  -d type=maven-project \
  -d language=java \
  -d bootVersion=3.2.0 \
  -d groupId=com.example \
  -d artifactId=my-api \
  -d dependencies=web,data-jpa,postgresql,lombok \
  -o my-api.zip && unzip my-api.zip

# Run
./mvnw spring-boot:run
# or
./mvnw package && java -jar target/my-api-0.0.1-SNAPSHOT.jar
```

Or use [start.spring.io](https://start.spring.io) in browser.

---

## Application Entry Point
*Main class structure*

```java
package com.example.myapi;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MyApiApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApiApplication.class, args);
    }
}
```

---

## REST Controller
*Expose HTTP endpoints*

```java
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController                      // @Controller + @ResponseBody
@RequestMapping("/api/users")
public class UserController {

    @GetMapping
    public List<String> getUsers() {
        return List.of("Alice", "Bob");
    }

    @GetMapping("/{id}")
    public String getUser(@PathVariable Long id) {
        return "User " + id;
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public String createUser(@RequestBody UserRequest req) {
        return "Created: " + req.name();
    }

    @DeleteMapping("/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void deleteUser(@PathVariable Long id) {
        // delete logic
    }
}
```

---

## application.properties / application.yml
*External configuration*

```yaml
# application.yml
server:
  port: 8080

spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb
    username: admin
    password: secret
  jpa:
    hibernate:
      ddl-auto: validate       # prod: validate / dev: create-drop
    show-sql: false

app:
  jwt-secret: ${JWT_SECRET}    # reads from env var
```

---

## Common Annotations
*Spring stereotype and mapping annotations*

**`@RestController`** – Marks class as REST controller; all methods return JSON  
**`@Service`** – Business logic layer; managed Spring bean  
**`@Repository`** – Data access layer; adds DB exception translation  
**`@Component`** – Generic Spring-managed bean  
**`@Autowired`** – Inject dependency (prefer constructor injection)  
**`@Value("${prop}")`** – Inject config value from properties  
