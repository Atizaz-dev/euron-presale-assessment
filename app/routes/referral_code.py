from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.database import SessionDepends
from app.db_helpers import get_ref_code
from app.schemas import ReferralSchema
from services import create_ref_code_service

router = APIRouter(
    prefix="/api/referral_data",
    tags=["Referral Codes"]
)


@router.get(path="/{address}", response_model=ReferralSchema)
def get_referral_code(address: str, session: SessionDepends):
    referral = get_ref_code(session, address)
    if not referral:
        return JSONResponse(status_code=404, content={"detail": "Referral Code Not Found!"})
    return referral


@router.post(
    path="/",
    response_model=ReferralSchema
)
def create_referral_code(data: ReferralSchema, session: SessionDepends):
    return create_ref_code_service(data, session)
