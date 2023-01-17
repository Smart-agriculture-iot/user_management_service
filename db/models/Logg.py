import datetime

from datetime import datetime
from db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Logg(Base):
    id = Column(Integer, primary_key=True, index=True)
    activity = Column(String, nullable=False)
    description = Column(String, nullable=True)
    username = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    loggtime = Column(DateTime(timezone=True), server_default=func.now())
