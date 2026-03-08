# Python Database

## sqlite3 (Built-in)
*Lightweight embedded SQL database*

```python
import sqlite3

conn = sqlite3.connect("app.db")    # file-based
# conn = sqlite3.connect(":memory:") # in-memory

cursor = conn.cursor()

# Create
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id   INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age  INTEGER
    )
""")
conn.commit()
```

---

## CRUD with sqlite3
*Basic data operations*

```python
# Insert
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
conn.commit()

# Read
cursor.execute("SELECT * FROM users WHERE age > ?", (18,))
rows = cursor.fetchall()        # list of tuples
row  = cursor.fetchone()        # single row

# Update
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (26, "Alice"))
conn.commit()

# Delete
cursor.execute("DELETE FROM users WHERE name = ?", ("Alice",))
conn.commit()

conn.close()
```

---

## Context Manager
*Auto-commit and close*

```python
import sqlite3

with sqlite3.connect("app.db") as conn:
    conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))
    # auto-commits on exit, rolls back on exception

# Usage
with sqlite3.connect("app.db") as conn:
    conn.row_factory = sqlite3.Row   # rows as dict-like objects
    rows = conn.execute("SELECT * FROM users").fetchall()
    for row in rows:
        print(row["name"], row["age"])
```

---

## SQLAlchemy (ORM)
*Map Python classes to database tables*

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session

engine = create_engine("sqlite:///app.db")

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id   = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age  = Column(Integer)

Base.metadata.create_all(engine)
```

### ORM CRUD
*Work with objects instead of SQL*

```python
from sqlalchemy.orm import Session

with Session(engine) as session:
    # Create
    user = User(name="Alice", age=25)
    session.add(user)
    session.commit()

    # Read
    user = session.get(User, 1)
    users = session.query(User).filter(User.age > 18).all()

    # Update
    user.age = 26
    session.commit()

    # Delete
    session.delete(user)
    session.commit()
```

---

## Migrations (Alembic)
*Manage schema changes over time*

```bash
pip install alembic
alembic init alembic          # setup migration folder
alembic revision --autogenerate -m "add users table"
alembic upgrade head          # apply migrations
alembic downgrade -1          # rollback one step
```

---

## Best Practices

**Parameterized queries** – Always use `?` placeholders; never f-strings in SQL  
**Context managers** – Use `with conn:` for automatic commit/rollback  
**`row_factory`** – Set `sqlite3.Row` for dict-like row access  
**SQLAlchemy** – Use ORM for complex apps; raw sqlite3 for simple scripts  
**Migrations** – Use Alembic for any schema that evolves over time  
