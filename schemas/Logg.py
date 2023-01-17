from datetime import date
from datetime import datetime
from typing import Optional

from pydantic import BaseModel

# shared properties


class LoggBase(BaseModel):
    activity: Optional[str] = None
    username: Optional[str] = None
    description: Optional[str] = "no description"
    loggtime: Optional[datetime] = datetime.now()


# this will be used to validate data while creating a logg
class LoggCreate(LoggBase):
    activity: str
    username: str
    description: str

    class Config:  # to convert non dict obj to json
        orm_mode = True

# this will be used to format the response to not to have id,user_id etc


class ShowLogg(LoggBase):
    activity: str
    username: str
    description: Optional[str]
    loggtime: datetime
    
    class Config:  # to convert non dict obj to json
        orm_mode = True
