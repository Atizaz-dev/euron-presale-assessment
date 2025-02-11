from fastapi import FastAPI
from sqlmodel import SQLModel

from .database import engine
from .routes import referral_code, manager_referral_code

fast_app = FastAPI()

fast_app.include_router(referral_code.router)
fast_app.include_router(manager_referral_code.router)


@fast_app.on_event("startup")
def startup_event():
    SQLModel.metadata.create_all(engine)
