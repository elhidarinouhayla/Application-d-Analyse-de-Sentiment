from fastapi import HTTPException
from app.config import SECRET_KEY, ALGORITHM 
from jose import jwt
from app.config import SECRET_KEY, ALGORITHM 





def create_token(username: str):
    payload = { "sub": username}

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_token(token: str):
    try:
       token_new = jwt.decode(token, SECRET_KEY, algorithms= ALGORITHM)
    except :
        raise HTTPException(status_code=401, detail="token invalide")
        return token_new