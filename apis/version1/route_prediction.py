from datetime import timedelta

from apis.utils import OAuth2PasswordBearerWithCookie
from apis.version1.route_login import get_current_user_from_token
from db.models.Logg import Logg
from db.models.users import User
from core.config import settings
from core.hashing import Hasher
from core.security import create_access_token
from db.repository.Logg import create_new_logg, create_new_logging
from db.repository.login import get_user
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from jose import JWTError
from schemas.tokens import Token
from sqlalchemy.orm import Session


router = APIRouter()


@router.post('/')
def prediction(db: Session = Depends(get_db),):
    logg = Logg(activity="test logs", description="this is a cool feature",
                username="test@iot.com")
    print("made:", logg)

    create_new_logging(username="test@iot.com",
                       activity="test logs", user_id=1, db=db)

    return "hello,predictions not yet ready"
