# SQL Notes

## Basic Concepts

- **Database**: Organized collection of structured data.
- **Table**: Collection of rows and columns.
- **Row (Record)**: A single entry in a table.
- **Column (Field)**: A category of data in a table.
- **Primary Key**: Unique identifier for each row.
- **Foreign Key**: A field that references a primary key in another table.

---

## Data Types

| Type         | Description                        |
|--------------|------------------------------------|
| INT          | Integer number                     |
| VARCHAR(n)   | Variable-length string (max n)     |
| TEXT         | Long text                          |
| DATE         | Date (YYYY-MM-DD)                  |
| BOOLEAN      | True / False                       |
| FLOAT        | Decimal number                     |

---

## DDL - Data Definition Language

```sql
-- Create a table
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    created_at DATE
);

-- Modify a table
ALTER TABLE users ADD COLUMN age INT;

-- Delete a table
DROP TABLE users;
```

---

## DML - Data Manipulation Language

```sql
-- Insert data
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

-- Read data
SELECT * FROM users;
SELECT name, email FROM users WHERE id = 1;

-- Update data
UPDATE users SET name = 'Bob' WHERE id = 1;

-- Delete data
DELETE FROM users WHERE id = 1;
```

---

## Filtering & Sorting

```sql
-- WHERE clause
SELECT * FROM users WHERE age > 18;

-- AND / OR
SELECT * FROM users WHERE age > 18 AND name = 'Alice';

-- ORDER BY
SELECT * FROM users ORDER BY name ASC;
SELECT * FROM users ORDER BY created_at DESC;

-- LIMIT
SELECT * FROM users LIMIT 10;

-- LIKE (pattern matching)
SELECT * FROM users WHERE name LIKE 'A%';
```

---

## Aggregate Functions

```sql
SELECT COUNT(*) FROM users;
SELECT AVG(age) FROM users;
SELECT MAX(age) FROM users;
SELECT MIN(age) FROM users;
SELECT SUM(age) FROM users;

-- GROUP BY
SELECT age, COUNT(*) FROM users GROUP BY age;

-- HAVING (filter after GROUP BY)
SELECT age, COUNT(*) FROM users GROUP BY age HAVING COUNT(*) > 1;
```

---

## JOINS

```sql
-- INNER JOIN
SELECT u.name, o.product
FROM users u
INNER JOIN orders o ON u.id = o.user_id;

-- LEFT JOIN (all from left, matching from right)
SELECT u.name, o.product
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- RIGHT JOIN
SELECT u.name, o.product
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

---

## Subqueries

```sql
-- Subquery in WHERE
SELECT name FROM users
WHERE id IN (SELECT user_id FROM orders WHERE total > 100);
```

---

## Indexes

```sql
-- Create index (speeds up queries)
CREATE INDEX idx_email ON users(email);

-- Drop index
DROP INDEX idx_email ON users;
```

---

## Constraints

```sql
NOT NULL       -- Field cannot be empty
UNIQUE         -- All values must be different
PRIMARY KEY    -- NOT NULL + UNIQUE
FOREIGN KEY    -- Links to another table
DEFAULT        -- Sets a default value
CHECK          -- Validates a condition
```
