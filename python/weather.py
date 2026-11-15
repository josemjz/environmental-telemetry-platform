from sqlalchemy  import Column, String, Integer, ForeignKey, DateTime, ForeignKeyConstraint, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import TIMESTAMP

from orm_base import Base
from sqlalchemy.ext.declarative import declarative_base # is this needed here?

class WeatherData(Base):
    # Table Name
    __tablename__ = 'weatherdata'
    #attributes
    unique_id = Column(Integer, primary_key=True, autoincrement=True)
    coord = Column("coords", String(4000), nullable=False)
    air_quality = Column("air_quality", String(4000), nullable=False)
    
    # no children so far

    def __init__(self, coord:str, air_quality: str):
        #self.unique_id = unique_id # does this need to be instantiated? since it is auto incrementing

        self.coord = coord
        self.air_quality = air_quality