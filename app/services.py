from starlette.responses import JSONResponse
from sqlmodel import Session

from app.db_helpers import get_ref_code, get_referral_count, create_ref_code
from app.schemas import ReferralSchema


def create_ref_code_service(data: ReferralSchema, session: Session, text="Referral"):
    num_of_referrals = get_referral_count(session, data.address, data.is_manager_code)
    if num_of_referrals >= 10:
        return JSONResponse(status_code=400, content={"detail": f"Reached {text} Code Limit!"})

    referral_exists = get_ref_code(session, data.address, True, data.ref_code, data.is_manager_code)
    if referral_exists:
        return JSONResponse(status_code=204, content={"detail": f"{text} Code Already Exists!"})

    referral_created = create_ref_code(session, data)
    return JSONResponse(status_code=201, content=ReferralSchema.model_validate(referral_created).model_dump())
