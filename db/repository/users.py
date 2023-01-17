from typing import List
from core.hashing import Hasher
from db.models.users import User
from schemas.users import ShowUser, UserCreate
from sqlalchemy.orm import Session


def create_new_user(user: UserCreate, db: Session):
    user = User(
        username=user.username,
        email=user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    return user


def get_all_user(db: Session):
    users = db.query(User).all()
    return users


def delete_user_by_id(id: int, db: Session, owner_id):
    existing_user = db.query(User).filter(User.id == id)
    if not existing_user.first():
        return 0
    existing_user.delete(synchronize_session=False)
    db.commit()
    return 1


def retreive_user(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    return user
def delete_user_by_id(id: int, db: Session):
    existing_user = db.query(User).filter(User.id == id)
    if not existing_user.first():
        return 0
    existing_user.delete(synchronize_session=False)
    db.commit()
    return 1


def update_user_by_id(id: int, user: UserCreate, db: Session):
    existing_user = db.query(User).filter(User.id == id)
    if not existing_user.first():
        return 0
  # update dictionary with new key value of owner_id
    existing_user.update(user.__dict__)
    db.commit()
    return 1
