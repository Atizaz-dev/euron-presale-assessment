from sqlmodel import Field, SQLModel


class ReferralCode(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    ref_code: str
    address: str = Field(index=True)
    is_manager_code: bool = Field(default=False)
