from fastapi import FastAPI, HTTPException, Depends
from app.sentiments import get_sentiment 
from app.model import UserCreate, UserResponse
from app.auth import create_token, verify_token
from app.config import SECRET_KEY, ALGORITHM
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

data_db = {"username":"admin",
        "password":"abcd"
}
app = FastAPI()

origins = ["*"]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)


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
def predict(payload: PredictSchema, token:str = Depends(verify_token)):

  text = payload.text

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