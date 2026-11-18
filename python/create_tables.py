from orm_base import Base

from db_connection import engine
import models

def createTables():
    # create new tables not in db
    Base.metadata.create_all(bind=engine)
    print("DB tables created successfully")


if __name__ == "__main__":
    createTables()