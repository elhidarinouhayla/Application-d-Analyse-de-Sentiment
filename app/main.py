from fastapi import FastAPI, HTTPException, Depends
from app.sentiments import get_sentiment 
from app.model import UserCreate, UserResponse
# from datetime import datetime, timedelta
# from jose import jwt, JWTError
from app.auth import create_token, verify_token
from app.config import SECRET_KEY, ALGORITHM
from pydantic import BaseModel

data_db = {"username":"admin",
        "password":"abcd"
}
app = FastAPI()

@app.post("/login")
def login(data:UserCreate):
  if data.username == data_db["username"] and data.password == data_db["password"]:
       token = create_token(data)  
       return {token}
  else:
    raise HTTPException(status_code=401,detail= "user name ou password incorrect")
  

class PredictSchema(BaseModel):
  text: str

@app.post("/predict")
def predict(text: str):

  predict =  get_sentiment(text)
  label = predict[0][0]["label"]
  score = predict[0][0]["score"]

  if score <= 2:
    sentiment = "negatif"
  elif score == 3:
    sentiment = "neutre"
  else:
    sentiment = "positif"

  return {"score": score, "sentiment":sentiment}  