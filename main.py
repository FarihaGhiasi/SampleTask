from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random
from datetime import datetime, timedelta, date
from sqlalchemy.exc import SQLAlchemyError
from db import engine  

# to define the SQLAlchemy model
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    registration_date = Column(Date)

# creating user table
Base.metadata.create_all(engine)

# session
Session = sessionmaker(bind=engine)
session = Session()


def create_users():
    """to generate some random data"""
    number_user_to_be_created = 30
    for i in range(number_user_to_be_created):
        name = f'User_{i}'
        today = datetime.now()
        one_year_ago = today - timedelta(days=365)
        registration_date = one_year_ago + timedelta(
            days=random.randint(1, 365)
        )
        user = User(name=name, registration_date=registration_date)
        session.add(user)
        session.commit()

    print(f"{number_user_to_be_created} users has been created.")
    


def delete_users():
    """To delete user older than 2023, 1, 9"""
    threshold_date = date(2023, 1, 7)
    try:
        with session.begin():
            delete_query = session.query(User).filter(
                User.registration_date < threshold_date)
            deleted_count = delete_query.delete()
            session.commit()
            print(f"{deleted_count} user records has been deleted successfully.")
    except SQLAlchemyError as e:
        print(f"Failed to delete records: {e}")



if __name__ == "__main__":
    create_users()
    delete_users()
