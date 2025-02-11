from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.database import SessionDepends
from app.db_helpers import get_ref_code
from app.schemas import ReferralSchema
from app.services import create_ref_code_service

router = APIRouter(
    prefix="/api/referral_data/manager",
    tags=["Manager Referral Codes"],
)


@router.get(path="/{address}", response_model=ReferralSchema)
def get_manager_ref_code(address: str, session: SessionDepends):
    referral = get_ref_code(session, address, is_manager_code=True)
    if not referral:
        return JSONResponse(status_code=404, content={"detail": "Manager Code Not Found!"})
    return referral


@router.post(
    path="/",
    response_model=ReferralSchema
)
def create_manager_ref_code(data: ReferralSchema, session: SessionDepends):
    return create_ref_code_service(data, session, text="Manager")
