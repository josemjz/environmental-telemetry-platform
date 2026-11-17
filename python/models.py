from datetime import datetime
from sqlalchemy  import Column, String, Integer, Float, DateTime,ForeignKey, ForeignKeyConstraint, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import TIMESTAMP

from orm_base import Base

"""
TODO: 
Create APIReadings parent tables Location and API 

"""
class APIReadings(Base):
    __tablename__ = 'api_readings'
    
    ### attributes
    reading_id = Column("reading_id", Integer, primary_key=True, autoincrement=True)
    location_id = Column("location_id", Integer, ForeignKey("locations.location_id"), nullable=False)
    api_id = Column("api_id", Integer, ForeignKey("apis.api_id"), nullable=False)

    recorded_at = Column("recorded_at", DateTime(timezone=True), nullable=False)

    # Air quality measurements from the OpenWeather API
    aqi = Column("aqi", Integer)
    pm2_5 = Column("pm2_5", Float)
    pm10 = Column("pm10", Float)
    co = Column("co", Float)
    no = Column("no", Float)
    no2 = Column("no2", Float)
    o3 = Column("o3", Float)
    so2 = Column("so2", Float)
    nh3 = Column("nh3", Float)
    
    # no children

    # parent connections since we are a child of location and api
    location = relationship('Locations', back_populates="locations_list", viewonly=False)
    api = relationship('APIs', back_populates="apis_list", viewonly=False)


    def __init__(self,recorded_at:datetime, aqi:int, pm2_5:float, pm10:float, 
                 co:float, no:float, no2:float, o3:float, so2:float, nh3:float, location, api):
        #self.reading_id = unique_id # does this need to be instantiated? since it is auto incrementing

        # Can write self.location = location and self.api = api 
        # since I have defined ORM relationships in line 33 and 34 but will leave for now
        self.location_id = location.location_id
        self.api_id = api.api_id
        

        self.recorded_at = recorded_at
        self.aqi = aqi
        self.pm2_5 = pm2_5
        self.pm10 = pm10
        self.co = co
        self.no = no
        self.no2 = no2
        self.o3 = o3
        self.so2 = so2
        self.nh3 = nh3
