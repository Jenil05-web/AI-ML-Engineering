from sqlalchemy.orm import Session

from database.connection import engine
from database.schema import Customer


with Session(engine) as session:
    customers = session.query(Customer).all()

    for customer in customers:
        print(customer.name, customer.city)