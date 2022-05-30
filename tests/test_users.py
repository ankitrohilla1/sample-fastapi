from app import schemas
import pytest
from jose import JWTError, jwt
from app.config import settings

# from .database import client, session


# def test_root(client):
#     res = client.get("/")
#     print(res.json().get("message"))
#     assert res.json().get("message") == " This is my world"
#     assert res.status_code == 200


def test_create_users(client):
    res = client.post("/users/", json={"email": "121@gmail.com", "password": "12345"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "121@gmail.com"
    assert res.status_code == 201


def test_login_user(test_user, client):
    res = client.post("/login", data={"username": test_user['email'], "password": test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == 'bearer'
    assert res.status_code == 200


@pytest.mark.parametrize("email, password, status_code", [(None, '12345', 422), ('11121@gmail.com', '122345', 403)])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password})
    assert res.status_code == status_code
    # assert res.json().get('detail') == 'Invalid Credentials'

