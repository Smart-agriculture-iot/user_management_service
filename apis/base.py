
from apis.version1 import route_login
from apis.version1 import route_users
from apis.version1 import route_weather_forecast
from apis.version1 import route_prediction
from apis.version1 import route_loggs
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(route_users.router, prefix="/users", tags=["users"])
api_router.include_router(route_login.router, prefix="/login", tags=["login"])
# api_router.include_router(route_weather_forecast.router, prefix="/weather", tags=["weather"])
# api_router.include_router(route_prediction.router, prefix="/prediction", tags=["predction"])
api_router.include_router(route_loggs.router, prefix="/logs", tags=["logs"])
