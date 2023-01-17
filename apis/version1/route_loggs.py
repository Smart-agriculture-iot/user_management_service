from typing import List
from typing import Optional

from apis.version1.route_login import get_current_user_from_token
from db.models.users import User
from db.repository.Logg import create_new_logg, create_new_logging, list_logss, retreive_logs
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.templating import Jinja2Templates
from schemas.Logg import LoggCreate, ShowLogg
from schemas.Logg import ShowLogg
from sqlalchemy.orm import Session


router = APIRouter()

# @router.post("/create-logg/", response_model=ShowLogg)
# def create_logg(
#         logg: LoggCreate,
#         db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)
#         ):
#     logg = create_new_logg(logg=logg, db=db, user_id=1)
#     create_new_logging(username=current_user.username, activity="Viewed user logs ", user_id=current_user.id, db=db)
#     return logg


@router.get("/all", response_model=List[ShowLogg])
def read_logs(db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):

    create_new_logging(username=current_user.username,
                       activity="Viewed user logs", user_id=current_user.id, db=db)
    logs = list_logss(db=db)
    return logs
