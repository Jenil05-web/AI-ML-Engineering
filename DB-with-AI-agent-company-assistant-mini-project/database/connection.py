from sqlalchemy import create_engine


DATABASE_URL = "sqlite:///data/company.db" # this means our sqlLite will use company.db 

engine = create_engine(
    DATABASE_URL,
    connect_args = {"check_same_thread": False},
)