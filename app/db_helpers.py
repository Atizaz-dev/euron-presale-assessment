from sqlmodel import Session, select

from app.models.referral_code import ReferralCode
from app.schemas import ReferralSchema


def get_referral_count(
        session: Session,
        address,
        is_manager_code,
):
    query = select(ReferralCode).where(
        ReferralCode.address == address,
        ReferralCode.is_manager_code == is_manager_code,
    )
    return session.exec(query).all().__len__()


def get_ref_code(
        session: Session,
        address,
        create=False,
        ref_code="",
        is_manager_code=False,
):
    statement = select(ReferralCode).where(
        ReferralCode.address == address,
        ReferralCode.is_manager_code == is_manager_code,
    )
    if create:
        statement = statement.where(
            ReferralCode.ref_code == ref_code,
        )
    result = session.exec(statement).all()
    return result[0] if result else None


def create_ref_code(
        session: Session,
        data: ReferralSchema,
):
    referral = ReferralCode(**data.model_dump())
    session.add(referral)
    session.commit()
    session.refresh(referral)
    return referral
