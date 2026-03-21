from app.database.connection import engine, Base
from app.models.models import User, Account, Category, Transaction

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas correctamente.")

if __name__ == "__main__":
    init_db()
