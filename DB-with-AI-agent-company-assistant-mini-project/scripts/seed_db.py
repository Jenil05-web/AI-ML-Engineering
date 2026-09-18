from datetime import date

from sqlalchemy.orm import Session
from database.connection import engine

from database.connection import engine
from database.schema import (
    Customer,
    Product,
    order,
    OrderItem,
    Employee,
)

with Session(engine) as session:

    # Customers
    customers = [
        Customer(name="Rahul Sharma", email="rahul@example.com", city="Ahmedabad", country="India"),
        Customer(name="Priya Patel", email="priya@example.com", city="Mumbai", country="India"),
        Customer(name="Amit Shah", email="amit@example.com", city="Ahmedabad", country="India"),
        Customer(name="John Smith", email="john@example.com", city="London", country="UK"),
        Customer(name="Sarah Wilson", email="sarah@example.com", city="New York", country="USA"),
    ]

    session.add_all(customers)

    # Products
    products = [
        Product(name="Laptop Pro", category="Electronics", price=1200),
        Product(name="Wireless Mouse", category="Accessories", price=40),
        Product(name="Mechanical Keyboard", category="Accessories", price=100),
        Product(name="Monitor 4K", category="Electronics", price=500),
        Product(name="USB-C Hub", category="Accessories", price=60),
    ]

    session.add_all(products)

    # Employees
    employees = [
        Employee(name="Alice Johnson", department="Engineering", role="Software Engineer", salary=85000),
        Employee(name="Bob Williams", department="Engineering", role="Senior Engineer", salary=110000),
        Employee(name="Carol Davis", department="HR", role="HR Manager", salary=75000),
        Employee(name="David Brown", department="Sales", role="Sales Executive", salary=65000),
        Employee(name="Emma Wilson", department="Marketing", role="Marketing Manager", salary=80000),
    ]

    session.add_all(employees)

    session.commit()

    print("Database seeded successfully.")