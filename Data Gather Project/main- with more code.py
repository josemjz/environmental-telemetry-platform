
#from pprint import pprint
from db_connection import Session, engine
from orm_base import metadata, Base
import logging
from sqlalchemy import MetaData

import serial
import pymysql

from weather import WeatherData

"""
TODO:
-Capture data from arduino using serial reader

-insert captured data into weather_data table

- print current data from table

- gather new data at intervals
"""

if __name__== '__main__':
    Base.metadata.create_all(bind=engine)
    metadata_object = MetaData()
    metadata_object.reflect(engine, schema="weather_schema")
    metadata.create_all(bind=engine)

   
   


"""import sys
import serial
#from pprint import pprint
from db_connection import Session, engine
from orm_base import metadata, Base
import logging
from sqlalchemy import MetaData

import serial
import pymysql

from weather import WeatherData

"""
TODO:
-Capture data from arduino using serial reader
"""
coord = "test"
weather_string = "test"
ser = serial.Serial('COM3', 9600)
try:
    while True:
        # Read data from Arduino. Ugly data but testing things works first
        data = ser.readline().decode().strip()
        if "coord" in data:
            coord = data
            break
        if "AQI" in data and "coord" not in data:
            weather_string = data
            break
        
except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed")



    

"""

-insert captured data into weather_data table

- print current data from table

- gather new data at intervals
"""

if __name__== '__main__':
    Base.metadata.create_all(bind=engine)
    metadata_object = MetaData()
    metadata_object.reflect(engine, schema="weather_schema")
    metadata.create_all(bind=engine)

    #testing adding one record to table in postgres
    row: WeatherData = WeatherData(coord, weather_string)
    with Session as sess:
        sess.add(row)
        sys.exit()"""


"""import serial
import time

coord = "test"
weather_string = "test"
ser = serial.Serial('COM3', 9600)

try:
    while True:
        data = ser.readline().decode().strip()
        
        # Process each line of data
        if "coord" in data:
            coord = data
        elif "AQI" in data:
            weather_string = data

        # Example condition to perform an action with the collected data
        if coord != "test" and weather_string != "test":
            # Placeholder for action, e.g., insert data into database
            print(f"Coordinates: {coord}, Weather Data: {weather_string}")
            
            # Reset variables if you're expecting more data
            coord = "test"
            weather_string = "test"
            
        # Example delay to avoid overwhelming the serial buffer - adjust as needed
        time.sleep(1)

except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed")
"""

"""
import sys
import serial
#from pprint import pprint
from db_connection import Session, engine
from orm_base import metadata, Base
import logging
from sqlalchemy import MetaData

import serial
import pymysql

from weather import WeatherData

"""
TODO:
-Capture data from arduino using serial reader
"""
coord = "test"
weather_string = "test"
ser = serial.Serial('COM3', 9600)
try:
    while True:
        # Read data from Arduino. Ugly data but testing things works first
        data = ser.readline().decode().strip()
        if "coord" in data:
            coord = data
            break
        if "AQI" in data and "coord" not in data:
            weather_string = data
            break
        
except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed")



    

"""

-insert captured data into weather_data table

- print current data from table

- gather new data at intervals
"""

if __name__== '__main__':
    Base.metadata.create_all(bind=engine)
    metadata_object = MetaData()
    metadata_object.reflect(engine, schema="weather_schema")
    metadata.create_all(bind=engine)

    #testing adding one record to table in postgres
    row: WeatherData = WeatherData(coord, weather_string)
    with Session as sess:
        sess.add(row)
        sys.exit()
"""