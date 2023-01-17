import logging
from apis.base import api_router
from core.config import settings
from core.hashing import Hasher
from db.base import Base
from db.repository.users import create_new_user, get_user_by_email
from db.session import SessionLocal, engine
from db.utils import check_db_connected
from db.utils import check_db_disconnected
from fastapi import FastAPI
from db.session import get_db
from fastapi.staticfiles import StaticFiles
from db.models.users import User
from schemas.users import UserCreate
from fastapi.middleware.cors import CORSMiddleware
# username: str
#     email: EmailStr
#     password: str


def include_router(app):
    app.include_router(api_router)


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,
                  version=settings.PROJECT_VERSION)
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
        allow_origins=['*'])
    
    include_router(app)
    create_tables()
    return app

app = start_application()
app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
        allow_origins=['*'])

@app.on_event("startup")
async def app_startup():
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
        allow_origins=['*'])
    await check_db_connected()
    user = User(username="admin", email="admin@iot.com",
                is_superuser=True, hashed_password=Hasher.get_password_hash("RoofTop"),)
    # user_object = User(**user.dict())
    with SessionLocal() as session:
        adminUser = get_user_by_email("admin@iot.com", session)
        if not adminUser:
            session.add(user)
            session.commit()
            session.refresh(user)
            logging.info(
                "Initial accout created with emai:")
            # print("Initial accout created with emai")

        else:
            print(adminUser.id)
            logging.info(
                "Initial accout already exist")
            print("Initial accout already exist")
    # usercreated = create_new_user(user=user, db=get_db)


@app.on_event("shutdown")
async def app_shutdown():
    await check_db_disconnected()
