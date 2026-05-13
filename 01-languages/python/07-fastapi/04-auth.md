# FastAPI Authentication
*JWT-based auth with OAuth2*

## JWT Authentication
*Protect endpoints with tokens*

```bash
pip install python-jose[cryptography] passlib[bcrypt]
```

**JWT** – JSON Web Token; signed token carrying user claims  
**OAuth2PasswordBearer** – FastAPI utility that reads `Bearer <token>` from the `Authorization` header  
**passlib** – Password hashing library; use `bcrypt` scheme

---

## Token Generation and Validation
*Full login + protected endpoint example*

```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key"
ALGORITHM  = "HS256"

app          = FastAPI()
pwd_context  = CryptContext(schemes=["bcrypt"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires: timedelta = timedelta(minutes=30)):
    payload = {**data, "exp": datetime.utcnow() + expires}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"user_id": user_id}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/token")
def login(form: OAuth2PasswordRequestForm = Depends()):
    # validate credentials here
    token = create_access_token({"sub": form.username})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/me")
def get_me(current_user: dict = Depends(get_current_user)):
    return current_user

# Usage
# POST /token  body: username=alice&password=secret  → returns JWT
# GET  /me     Headers: Authorization: Bearer <token>
```
