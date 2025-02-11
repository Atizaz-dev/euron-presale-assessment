from typing import Annotated

from fastapi import Depends
from sqlmodel import create_engine, Session
from .models import referral_code as referral_model

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def get_session():
    with Session(engine) as session:
        yield session


SessionDepends = Annotated[Session, Depends(get_session)]
