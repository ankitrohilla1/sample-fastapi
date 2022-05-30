from fastapi.testclient import TestClient
from app.main import app
from app.config import settings
from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.database import get_db
from app.database import Base
import pytest
from app.oath2 import create_access_token
from app import models
# from alembic import command

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:12345@localhost:5432/fastapi_test"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@" \
    f"{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# client = TestClient(app)

@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    # command.upgrade
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()
    # command.upgrade("base")
    # return TestClient(app)


@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture
def test_user2(client):
    user_data = {"email":"ankit123@gmail.com",
                 "password":"123"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user

@pytest.fixture
def test_user(client):
    user_data = {"email":"ankit@gmail.com",
                 "password":"12345"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user


@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user['id']})


@pytest.fixture
def authorized_client(client, token):
    client.headers = {**client.headers, "Authorization": f"Bearer {token}"}
    return client


@pytest.fixture
def test_posts(test_user, session, test_user2):
    posts_data = [{"title":"first",
                   "content":"yes this is",
                   "owner_id": test_user['id']},
                  {"title": "second",
                   "content": "yes this is",
                   "owner_id": test_user['id']},
                   {"title": "third",
                    "content": "yes this is",
                    "owner_id": test_user['id']
                   },
                  {"title": "forth",
                   "content": "forth this is",
                   "owner_id": test_user2['id']
                   }
                  ]

    def create_post_model(post):
        return models.Post(**post)

    post_map = map(create_post_model, posts_data)
    posts = list(post_map)

    session.add_all(posts)
    session.commit()
    all_posts = session.query(models.Post).all()
    return all_posts
