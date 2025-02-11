from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel

from .database import engine
from .routes import referral_code, manager_referral_code

fast_app = FastAPI()

fast_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow All
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  # upcoming headers
    expose_headers=["*"],  # return headers
)

fast_app.include_router(referral_code.router)
fast_app.include_router(manager_referral_code.router)


@fast_app.on_event("startup")
def startup_event():
    SQLModel.metadata.create_all(engine)
