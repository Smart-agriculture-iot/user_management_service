from db.models.Logg import Logg
from schemas.Logg import LoggCreate
from sqlalchemy.orm import Session


def create_new_logg(logg: LoggCreate, db: Session, user_id: int):
    Logg_object = Logg(**logg.dict(), user_id=user_id)
    db.add(Logg_object)
    db.commit()
    db.refresh(Logg_object)
    return Logg_object


def create_new_logging(username: str, activity: str, db: Session, user_id: int):

    new_log = LoggCreate(username=username, activity=activity,
                         description="test description")
    Logg_object = Logg(**new_log.dict(), user_id=user_id)
    db.add(Logg_object)
    db.commit()
    db.refresh(Logg_object)
    return Logg_object


def retreive_logs(username: str, db: Session):
    loggs = db.query(Logg).filter(Logg.username == username)
    return loggs


def list_logss(db: Session):
    logs = db.query(Logg).all()
    return logs

