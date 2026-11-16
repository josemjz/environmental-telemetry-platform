from datetime import datetime
from sqlalchemy  import Column, String, Integer, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import TIMESTAMP

from orm_base import Base

class WeatherData(Base):
    __tablename__ = 'weatherdata'
    
    ### attributes
    unique_id = Column(Integer, primary_key=True, autoincrement=True)
    # Which data source the reading came from
    source = Column("source", String(50), nullable=False)

    recorded_at = Column("recorded_at", DateTime(timezone=True), nullable=False)

    # where the reading came from using latitude and longitude
    lat = Column("lat", Float, nullable=False)
    lon = Column("lon", Float, nullable=False)

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
    
    # no children so far

    def __init__(self, source:str, recorded_at:datetime, lat:float, lon:float, aqi:int, pm2_5:float, pm10:float, 
                 co:float, no:float, no2:float, o3:float, so2:float, nh3:float):
        #self.unique_id = unique_id # does this need to be instantiated? since it is auto incrementing

        self.source = source
        self.recorded_at = recorded_at
        self.lat = lat
        self.lon = lon
        self.aqi = aqi
        self.pm2_5 = pm2_5
        self.pm10 = pm10
        self.co = co
        self.no = no
        self.no2 = no2
        self.o3 = o3
        self.so2 = so2
        self.nh3 = nh3
