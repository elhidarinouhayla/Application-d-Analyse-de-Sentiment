from sqlalchemy import String, Integer, Column
from app.database import Base
from pydantic import BaseModel



# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True)
#     username = Column(String, unique=True, nullable=False)
#     password = Column(String, nullable=False)


class UserCreate(BaseModel):
    username : str
    password : str


class UserResponse(UserCreate):
    id : int