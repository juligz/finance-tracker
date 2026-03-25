from app.database.connection import SessionLocal
from app.models.models import Account, Category, Transaction, User


def seed_db():
    db = SessionLocal()

    try:
        existing_user = db.query(User).filter(User.email == "julian@test.com").first()
        if existing_user:
            print("Database already seeded, skipping.")
            return

        user = User(email="julian@test.com", hashed_password="hashed_1234")
        db.add(user)
        db.commit()
        db.refresh(user)

        account = Account(
            user_id=user.id,
            name="Banco Nación",
            type="bank",
            balance=50000.0,
        )
        db.add(account)
        db.commit()
        db.refresh(account)

        category_income = Category(
            user_id=user.id,
            name="Sueldo",
            type="income",
        )
        category_expense = Category(
            user_id=user.id,
            name="Supermercado",
            type="expense",
        )
        db.add_all([category_income, category_expense])
        db.commit()
        db.refresh(category_income)
        db.refresh(category_expense)

        transactions = [
            Transaction(
                account_id=account.id,
                category_id=category_income.id,
                amount=50000.0,
                description="Sueldo marzo",
                type="income",
            ),
            Transaction(
                account_id=account.id,
                category_id=category_expense.id,
                amount=15000.0,
                description="Compras supermercado",
                type="expense",
            ),
        ]
        db.add_all(transactions)
        db.commit()

        print("Database seeded successfully.")

    except Exception as e:
        db.rollback()
        print(f"Error seeding database: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    seed_db()
