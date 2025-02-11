import pytest
from fastapi.testclient import TestClient
from sqlmodel import create_engine, Session, SQLModel

from app.database import get_session
from app.main import fast_app
from app.models.referral_code import ReferralCode
from app.schemas import ReferralSchema

TEST_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(TEST_DATABASE_URL, echo=True)


def get_test_session():
    with Session(engine) as session:
        yield session


fast_app.dependency_overrides[get_session] = get_test_session
test_client = TestClient(fast_app)


@pytest.fixture(scope="function", autouse=True)
def setup_database():
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)


def create_referral(is_manager=False):
    with Session(engine) as session:
        referral = ReferralCode(
            address="abc",
            ref_code="ABC123",
            is_manager_code=is_manager,
        )
        session.add(referral)
        session.commit()
        session.refresh(referral)
        return ReferralSchema.model_validate(referral).model_dump()


def create_ten_referrals(is_manager=False):
    with Session(engine) as session:
        for i in range(10):  # Insert 10 referral codes to hit the limit
            referral = ReferralCode(address="0x789", ref_code=f"CODE{i}", is_manager_code=is_manager)
            session.add(referral)
        session.commit()
