from sqlalchemy.orm import declarative_base

# Base class for our db tables
Base = declarative_base()

# to keep track of table defenitions
metadata = Base.metadata