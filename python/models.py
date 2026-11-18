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
class Source(Base):
    __tablename__ = 'source'

    ## attributes
    source_id = Column("source_id", Integer, primary_key=True, autoincrement=True)

    source_name = Column("source_name", String, nullable=False)
    source_type = Column("source_type", String)

    # no parents

    # children
    apis = relationship("API", back_populates='source', viewonly=False)
    devices = relationship("Device", back_populates='source', viewonly=False)

    def __init__(self, source_name: str, source_type: str):
        self.source_name = source_name
        self.source_type = source_type

        self.apis = []
        self.devices = []

class Location(Base):
    __tablename__ = 'location'

    ## attributes
    location_id = Column("location_id", Integer, primary_key=True, autoincrement=True)

    location_name = Column("location_name", String, nullable=False)
    lat = Column("lat", Float)
    lon = Column("lon", Float)

    # children
    apiReadings = relationship("APIReading", back_populates='location', viewonly=False)

    # create instance function

    def __init__(self, location_name: str, lat: float, lon: float):

        self.location_name = location_name
        self.lat = lat
        self.lon = lon

        # instantiate location list
        self.apiReadings = []


class API(Base):
    __tablename__ = "api"

    ## attributes
    api_id = Column("api_id", Integer, primary_key=True, autoincrement=True)
    source_id = Column("source_id", Integer, ForeignKey("source.source_id"), nullable=False)

    api_name = Column("api_name", String, nullable=False)

    # parents
    source = relationship('Source', back_populates="apis", viewonly=False)

    # children
    apiReadings = relationship('APIReading', back_populates='api', viewonly=False)

    def __init__(self, source, api_name: str):

        self.source_id = source.source_id

        self.api_name = api_name

        self.apiReadings= []


class APIReading(Base):
    __tablename__ = 'api_reading'
    
    ### attributes
    reading_id = Column("reading_id", Integer, primary_key=True, autoincrement=True)
    location_id = Column("location_id", Integer, ForeignKey("location.location_id"), nullable=False)
    api_id = Column("api_id", Integer, ForeignKey("api.api_id"), nullable=False)

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
    location = relationship('Location', back_populates="apiReadings", viewonly=False)
    api = relationship('API', back_populates="apiReadings", viewonly=False)


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
