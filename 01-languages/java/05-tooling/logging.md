# Logging
*Record application events — SLF4J + Logback (standard in Java)*

## Setup (Maven)

```xml
<dependency>
  <groupId>ch.qos.logback</groupId>
  <artifactId>logback-classic</artifactId>
  <version>1.4.11</version>
</dependency>
```

SLF4J is the API; Logback is the implementation. You code against SLF4J only.

---

## Basic Usage

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

class UserService {
    private static final Logger log = LoggerFactory.getLogger(UserService.class);

    void createUser(String name) {
        log.debug("Creating user: {}", name);
        log.info("User created: {}", name);
        log.warn("Duplicate user detected: {}", name);
        log.error("Failed to create user: {}", name);
    }
}
```

---

## Log Levels (lowest → highest)

```
TRACE   → very detailed (method entry/exit)
DEBUG   → development details
INFO    → normal app events
WARN    → something unexpected but recoverable
ERROR   → failures that need attention
```

Only messages at or above the configured level are shown.

---

## Log with Exception

```java
try {
    // ...
} catch (IOException e) {
    log.error("Failed to read file: {}", filename, e);  // includes stack trace
}
```

---

## Configuration – logback.xml
*Place in `src/main/resources/`*

```xml
<configuration>

  <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
      <pattern>%d{HH:mm:ss} %-5level %logger{36} - %msg%n</pattern>
    </encoder>
  </appender>

  <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
    <file>logs/app.log</file>
    <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
      <fileNamePattern>logs/app.%d{yyyy-MM-dd}.log</fileNamePattern>
      <maxHistory>30</maxHistory>
    </rollingPolicy>
    <encoder>
      <pattern>%d{yyyy-MM-dd HH:mm:ss} %-5level %logger - %msg%n</pattern>
    </encoder>
  </appender>

  <root level="INFO">
    <appender-ref ref="CONSOLE"/>
    <appender-ref ref="FILE"/>
  </root>

  <!-- Set DEBUG for a specific package -->
  <logger name="com.company.service" level="DEBUG"/>

</configuration>
```

---

## Pattern Tokens

```
%d          date/time
%level      log level
%logger     logger name (class)
%msg        the message
%n          newline
%-5level    left-padded level (5 chars)
%logger{36} logger name truncated to 36 chars
```
