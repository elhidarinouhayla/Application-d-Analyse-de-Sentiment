from fastapi import Depends, HTTPException
from datetime import datetime, timedelta
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.config import SECRET_KEY, ALGORITHM 
from jose import jwt, JWTError




def create_token(username):
    payload = {
        # "sub": username,
        # "exp": datetime.utcnow() + timedelta(hours=1)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_token(token):
    try:
       token_new = jwt.decode(token, SECRET_KEY, algorithms= ALGORITHM)
        # username = payload.get("sub")

        # if username is None:
        # raise HTTPException(status_code=401, detail= "token invalide")
        # return username
    
    except :
        raise HTTPException(status_code=401, detail="token invalide")
        return data