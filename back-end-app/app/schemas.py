from datetime import datetime

from pydantic import BaseModel


class RecommendationBase(BaseModel):
    title: str
    description: str


class RecommendationCreate(RecommendationBase):
    pass


class Recommendation(RecommendationBase):
    id: int
    creation_time: datetime
    user_id: str

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: str
    recommendations: list[Recommendation] = []

    class Config:
        from_attributes = True
