from datetime import timedelta
import ast
from apis.utils import OAuth2PasswordBearerWithCookie
from apis.version1.route_login import get_current_user_from_token
from core.config import settings
from core.hashing import Hasher
from core.security import create_access_token
from db.models.Logg import Logg
from db.models.users import User
from db.repository.Logg import create_new_logging
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
# import pyaudioconvert as pac
from core.config import settings
from os import path
# from pydub import AudioSegment
from fastapi import UploadFile, File, status
import aiofiles
import timeit
# import nemo
# import nemo.collections.asr as nemo_asr
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
import requests
router = APIRouter()

# @router.get('/')
# def stt():
#     return "hello from stt"


@router.post("/weather/", response_description="", response_model="")
def weather(db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token),):
    logg = Logg(activity="test logs", description="this is a cool feature",
                username=current_user.username)
    print("made:", logg)

    create_new_logging(username=current_user.username,
                       activity="test logs", user_id=current_user.id, db=db)

    return "hello,weather forecasting not yet ready"