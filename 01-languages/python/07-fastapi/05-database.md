# FastAPI Database
*SQLAlchemy integration with dependency injection*

## Setup
*Install and configure SQLAlchemy*

```bash
pip install sqlalchemy psycopg2-binary   # PostgreSQL
# or
pip install sqlalchemy aiosqlite          # SQLite async
```

**SQLAlchemy** – Python ORM for relational databases  
**Session** – Unit of work; opened per request, closed after  
**Base** – Declarative base class all models inherit from

---

## Database Connection
*Engine, session, and base setup*

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:pass@localhost/mydb"

engine       = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base         = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

## Model and CRUD
*Define a model and wire it to endpoints*

```python
from fastapi import FastAPI, Depends
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from database import Base, engine, get_db

class User(Base):
    __tablename__ = "users"
    id    = Column(Integer, primary_key=True)
    name  = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.post("/users")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"deleted": user_id}

# Usage
# GET    /users        → list all users
# POST   /users        → create user
# DELETE /users/42     → delete user
```
