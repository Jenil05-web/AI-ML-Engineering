from database.connection import engine
from database.schema import Base

Base.metadata.create_all(engine)

print("Database created sucessfully !")

