from fastapi.testclient import TestClient
from app.main import app
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.database import get_db
from app.database import Base
import pytest
from alembic import command

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

