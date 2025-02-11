from app.tests.conftest import create_referral, test_client, create_ten_referrals


def test_get_referral_code_success():
    referral = create_referral()

    response = test_client.get(f"/api/referral_data/{referral["address"]}")
    assert response.status_code == 200
    assert response.json()["ref_code"] == referral["ref_code"]


def test_get_referral_code_not_found():
    response = test_client.get(f"/api/referral_data/abc")
    assert response.status_code == 404
    assert response.json() == {"detail": "Referral Code Not Found!"}


def test_create_referral_code_success():
    payload = {"address": "0x456", "ref_code": "XYZ789", "is_manager_code": False}

    response = test_client.post("/api/referral_data/", json=payload)
    assert response.status_code == 201
    assert response.json()["ref_code"] == "XYZ789"


def test_create_referral_code_limit_reached():
    create_ten_referrals()

    payload = {"address": "0x789", "ref_code": "LIMIT123", "is_manager_code": False}
    response = test_client.post("/api/referral_data/", json=payload)

    assert response.status_code == 400
    assert "Reached Referral Code Limit!" in response.json()["detail"]


def test_create_referral_code_already_exists():
    payload = create_referral()

    response = test_client.post("/api/referral_data/", json=payload)

    assert response.status_code == 204
    assert "Code Already Exists!" in response.json()["detail"]
