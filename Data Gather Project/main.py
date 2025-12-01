import sys
import serial
#from p
# 
# print import ppring
from db_connection import Session, engine
from orm_base import MetaData
import logging
from sqlalchemy import MetaData


import serial
import pymysql


from weather import WeatherData


"""
TODO:
-Capture data from arduino using serial reader

"""

### clean captured arduino console data

coord = "test"
weather_string = "test"

ser = serial.Serial('COM3', 9600)
try:
    while True:
        # Read data from Arduino. Data is not perfect, but good for testing purposes and to confirm code works
        data = ser.readline().decode().strip()
        if "coord" in data:
            coord = data
        weather_string += str(data)
        print(data)
        # if "CO" in data and "Levels" not in data:
            # weather_string = data

except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed")


#Pseudo code for the Temp & Humidity sensor data - how will the main interact with it and how will I capture and send data to the server
"""
#Do I want the data to be captured at the same time that the openweather data gets captured? 
# If not, will I communicate to the board which weather to capture
# If the sensor is attached, can the board still receive openweather data?
# Will I want to have the board to have the ability to capture both open weather data and sensor data and communicate to python at the same time?
    # If the above is true, will I want to be able to have the ability to have multiple sensors communicate with the board at once, being able to change it with the push of a button or just automatically?
        # How will I want to structure my code. It will be messy if it is all just one main file for the python and c++ code. 
            # Perhaps multiple classes that the board gets from. One for each sensor and or api key. 
            # What are the limitations
        #At what level do I want to communicate which sensor to use, at the python level, the Arduino code or even via input at the keyboard or the board itself
            # Or will the input come automatically depending on which sensor is live and capabilities of course. 
How will I want to structure my tables. Eventually after I have gotten my main code straightened out.

1. Figure out how to structure both the open weather code and temp & humidity sensor in one file. 
2. How to interact with the board and which data to gather
3. Update Tables to work with new data elements
4. work on python code itself to gather arduino information then send it to sql

** Are there better ways of communicating with the board besides serial connections?
"""

""""

-insert captured data into weather_data table

- print current data from table

- gather new data at intervals
"""

# clean captured arduino console data

if __name__== '__main__':
    metadata_object = MetaData()
    metadata_object.reflect(engine, schema="weather_shchema")
    metadata_object.create_all(bind=engine) #

    # testing adding one record to tabel in postgres
    row: WeatherData = WeatherData(coord, weather_string)
    with Session() as sess:
        sess.add(row)
        sess.commit()
        sys.exit()
#block worked without code lines 21-34, but good for testing purposes
