from fastapi import HTTPException
from app.config import SECRET_KEY, ALGORITHM 
from jose import jwt
# from datetime import datetime, timedelta
# import sys, os

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.config import SECRET_KEY, ALGORITHM 
from jose import jwt




def create_token(username):
    payload = {}

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_token(token):
    try:
       token_new = jwt.decode(token, SECRET_KEY, algorithms= ALGORITHM)
    except :
        raise HTTPException(status_code=401, detail="token invalide")
        return data