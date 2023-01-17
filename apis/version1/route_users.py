from typing import List
from fastapi import status
from apis.version1.route_login import get_current_user_from_token
from db.models.users import User
from db.repository.users import create_new_user, get_all_user, delete_user_by_id, retreive_user, delete_user_by_id, update_user_by_id
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from schemas.users import ShowUser
from schemas.users import UserCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException
from db.repository.login import get_use_by_username, get_user
from db.repository.Logg import create_new_logging
router = APIRouter()


@router.post("/", response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    if get_user(username=user.email, db=db):
        raise HTTPException(
            status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, detail=f"user email already exist"
        )

    if get_use_by_username(username=user.username, db=db):
        raise HTTPException(
            status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, detail=f"username already exist"
        )
    user = create_new_user(user=user, db=db)
#     create_new_logging(username=current_user.username,
#                        activity="created new user with usename"+user.username, user_id=current_user.i, db=db)
    return user


@router.get('/allUser', response_model=List[ShowUser])
def getall(db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    users = get_all_user(db=db)
    create_new_logging(username=current_user.username,
                       activity="viewed all system users", user_id=current_user.id, db=db)
    return users


@router.delete("/deleteuser/{id}")
def delete_user(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    user = retreive_user(id=id, db=db)
    if not user:
        create_new_logging(username=current_user.username, activity="tried deleting user by id: {}but user was not found".format(
            id), user_id=current_user.id, db=db)
        return HTTPException(

            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} does not exist",
        )
    delete_user_by_id(id=id, db=db)
    create_new_logging(username=current_user.username,
                       activity="viewed all system users", user_id=current_user.id, db=db)
    create_new_logging(username=current_user.username, activity="deleted user by id: {} successfully".format(
        id), user_id=current_user.id, db=db)
    return {"detail": "Successfully deleted."}


@router.put("/updateuser/{id}")
def update_user(id: int, user: UserCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):

    message = update_user_by_id(id=id, user=user, db=db)
    if not message:
        create_new_logging(username=current_user.username, activity="tried updating user by id: {}but user was not found".format(
            id), user_id=current_user.id, db=db)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not found"
        )
    create_new_logging(username=current_user.username, activity="updated user by id: {} successfully".format(
        id), user_id=current_user.id, db=db)
    return {"msg": "User Successfully updated data."}
