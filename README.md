# Environmental Telemetry Platform

An environmental monitoring and data analytics project integrating Arduino hardware, Python, PostgreSQL, and environmental data sources using weather APIs and physical sensors. 

## Project Overview

This project builds upon my original Weather-Data prototype, developed using an Arduino MKR WIFI 1010, an RGB Shield, Python, SQLAlchemy, and PostgreSQL. 

The original implementation successfully collected air-quality data through the Arduino MKR WiFi 1010, displayed readings on the RGB Shield, and transferred data to PostgreSQL using Python and serial communication.

The current iteration focuses on developing a reliable, testable data ingestion pipeline that supports environmental monitoring, structured data storage, and analytics.

## Technology Stack
* **Hardware**: Arduino MKR WiFi 1010, RGB Shield, variety of environmental sensors 
* **Programming**: Python, Arduino C++
* **Database**: PostgreSQL, SQLAlchemy
* **Data Sources**: OpenWeather API, environmental sensors
* **Analytics**: SQL, Power BI

## Development Status

The repository currently contains the original Arduino sketches and the original Python implementation. 

### TODO:
* Restore and validate the existing ingestion pipeline
* Improve data processing and PostgreSQL integration
* Add error handling, logging, and automated tests
* Improve environmental data visualizations
* Integrate local environmental sensors

## Hardware
The original Arduino prototype displayed air-quality measurements and classifications on an RGB Shield.

A separate DHT11 prototype was developed to measure temperature and humidity.

Future development will explore combining these inputs into a unified environmental telemetry platform.