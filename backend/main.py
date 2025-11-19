from fastapi import FastAPI, HTTPException, Depends
from backend.sentiments import get_sentiment 
from backend.model import UserCreate, UserResponse
from datetime import datetime, timedelta
from jose import jwt, JWTError
from backend.auth import create_token, verify_token
from config import SECRET_KEY, ALGORITHM
from pydantic import BaseModel

data = {"username":"admin",
        "password":"abcd"
}
app = FastAPI()

@app.post("/login")
def login(data:UserCreate):
  if data.username == data["username"] and data.password == data["password"]:
       token = create_token(data)  
       return {token}
  else:
    raise HTTPException(status_code=401,detail= "user name ou password incorrect")
  

class PredictSchema(BaseModel):
  text: str

@app.post("/predict")
def predict(text: PredictSchema):
  print(text)
  label =  get_sentiment(text)

  score = int(label[0])
  if score <= 2:
    sentiment = "negatif"
  elif score == 3:
    sentiment = "neutre"
  else:
    sentiment = "positif"

  return {"score": score, "sentiment":sentiment}  