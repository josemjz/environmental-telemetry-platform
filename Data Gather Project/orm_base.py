from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData

Base = declarative_base(metadata=MetaData(schema="weather_schema")) # do I need to create the schema first within postgresql
metadata = Base.metadata