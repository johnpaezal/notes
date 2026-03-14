# JDBC
*Java Database Connectivity — connect to SQL databases*

## Setup (Maven – PostgreSQL example)

```xml
<dependency>
  <groupId>org.postgresql</groupId>
  <artifactId>postgresql</artifactId>
  <version>42.7.1</version>
</dependency>
```

Other drivers: `mysql-connector-j`, `h2` (in-memory), `sqlite-jdbc`

---

## Connect

```java
import java.sql.*;

String url = "jdbc:postgresql://localhost:5432/mydb";
String user = "postgres";
String password = "secret";

Connection conn = DriverManager.getConnection(url, user, password);
```

---

## Query (SELECT)

```java
String sql = "SELECT id, name, age FROM users WHERE age > ?";

try (PreparedStatement stmt = conn.prepareStatement(sql)) {
    stmt.setInt(1, 18);  // bind parameter (1-indexed)

    try (ResultSet rs = stmt.executeQuery()) {
        while (rs.next()) {
            int id      = rs.getInt("id");
            String name = rs.getString("name");
            int age     = rs.getInt("age");
            System.out.println(id + " " + name + " " + age);
        }
    }
}
```

---

## Insert / Update / Delete

```java
// INSERT
String sql = "INSERT INTO users (name, age) VALUES (?, ?)";
try (PreparedStatement stmt = conn.prepareStatement(sql)) {
    stmt.setString(1, "Alice");
    stmt.setInt(2, 25);
    int rowsAffected = stmt.executeUpdate();  // returns number of rows
}

// UPDATE
String sql = "UPDATE users SET age = ? WHERE name = ?";
try (PreparedStatement stmt = conn.prepareStatement(sql)) {
    stmt.setInt(1, 26);
    stmt.setString(2, "Alice");
    stmt.executeUpdate();
}

// DELETE
String sql = "DELETE FROM users WHERE id = ?";
try (PreparedStatement stmt = conn.prepareStatement(sql)) {
    stmt.setInt(1, 42);
    stmt.executeUpdate();
}
```

---

## Get Generated Keys

```java
String sql = "INSERT INTO users (name) VALUES (?)";
try (PreparedStatement stmt = conn.prepareStatement(
        sql, Statement.RETURN_GENERATED_KEYS)) {

    stmt.setString(1, "Bob");
    stmt.executeUpdate();

    try (ResultSet keys = stmt.getGeneratedKeys()) {
        if (keys.next()) {
            int generatedId = keys.getInt(1);
        }
    }
}
```

---

## Transactions

```java
conn.setAutoCommit(false);  // disable auto-commit

try {
    // multiple operations...
    stmt1.executeUpdate();
    stmt2.executeUpdate();

    conn.commit();   // all or nothing
} catch (SQLException e) {
    conn.rollback(); // undo everything
} finally {
    conn.setAutoCommit(true);
}
```

---

## Connection Pool (HikariCP)
*Don't create a new connection per request — use a pool*

```xml
<dependency>
  <groupId>com.zaxxer</groupId>
  <artifactId>HikariCP</artifactId>
  <version>5.1.0</version>
</dependency>
```

```java
HikariConfig config = new HikariConfig();
config.setJdbcUrl("jdbc:postgresql://localhost:5432/mydb");
config.setUsername("postgres");
config.setPassword("secret");
config.setMaximumPoolSize(10);

HikariDataSource dataSource = new HikariDataSource(config);

// Use like normal
try (Connection conn = dataSource.getConnection()) {
    // ...
}
```

---

## JDBC URL Formats

```
PostgreSQL:  jdbc:postgresql://host:5432/dbname
MySQL:       jdbc:mysql://host:3306/dbname
H2 (memory): jdbc:h2:mem:testdb
SQLite:      jdbc:sqlite:path/to/file.db
```
