from passlib.context import CryptContext
from sqlalchemy import desc
from sqlalchemy.orm import Session

from . import models, schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        username=user.username, password=hashed_password, email=user.email
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, user_email: str):
    return db.query(models.User).filter(models.User.email == user_email).first()


def create_recommendation(
    db: Session, recommendation: schemas.RecommendationCreate, user_id: str
):
    db_recommendation = models.Recommendation(
        title=recommendation.title,
        description=recommendation.description,
        user_id=user_id,
    )
    db.add(db_recommendation)
    db.commit()
    db.refresh(db_recommendation)
    return db_recommendation


def get_recommendations_by_user_id(db: Session, user_id: str):
    return (
        db.query(models.Recommendation)
        .filter(models.Recommendation.user_id == user_id)
        .order_by(desc(models.Recommendation.creation_date))
    )
