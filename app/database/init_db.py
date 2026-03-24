from app.database.connection import Base, engine
from app.models import models  # noqa: F401 - required for SQLAlchemy to register models


def init_db():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")


if __name__ == "__main__":
    init_db()
