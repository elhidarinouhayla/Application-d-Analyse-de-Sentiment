from fastapi import HTTPException
from app.config import SECRET_KEY, ALGORITHM 
from jose import jwt
# from datetime import datetime, timedelta, timezone
from app.config import SECRET_KEY, ALGORITHM 





def create_token(username):
    payload = {
        # "sub": username,
        # "exp": datetime.now(timezone.utc) + timedelta(hours=1)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_token(token):
    try:
       token_new = jwt.decode(token, SECRET_KEY, algorithms= ALGORITHM)
    except :
        raise HTTPException(status_code=401, detail="token invalide")
        return token_new