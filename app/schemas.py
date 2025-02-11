from sqlmodel import SQLModel


class ReferralSchema(SQLModel):
    address: str
    ref_code: str
    is_manager_code: bool
