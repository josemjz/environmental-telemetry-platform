from db_connection import Session
import models
from datetime import datetime, timezone

def testParentTables():
    sess = Session()

    try:
        # create test records
        source = models.Source("OpenWeather_test_1", "API_1")

        # griffith observatory coords
        location = models.Location("Griffith Observatory", 34.1184, -118.3005)

        # add records to our sesh
        sess.add(source)
        sess.add(location)

        # save records to postgres
        sess.commit()

        # query the records we inserted above
        sources = sess.query(models.Source).all()
        locations = sess.query(models.Location).all()

        for source in sources:
            print(source.source_id, source.source_name, source.source_type)

        for location in locations:
            print(location.location_id, location.location_name, location.lat, location.lon)

    except Exception:
        sess.rollback()
        raise

    finally:
        Session.remove()


"""
TODO:
Test children tables
Test db queries
"""

def testAPITables():
    sess = Session()

    try:
        ## Create test records for parent tables first 
        source = models.Source(source_name="OpenWeather_test_1", source_type="API_1")

        # griffith observatory coords
        location = models.Location(location_name="Griffith Observatory", lat=34.1184, lon=-118.3005)

        # add parent records to sesh before children to avoid source_id being None
        sess.add(source)
        sess.add(location)

        # Insert parent records and get their ID's without commiting. 
        # allows us to roll everything back if a child record insert fails. 
        sess.flush() 

        # api <- source
        api = models.API(source=source, api_name="TestName1")
        sess.add(api)
        sess.flush()

        # apireading <- (api, location)
        apiReading = models.APIReading(
            recorded_at=datetime.now(timezone.utc),
            aqi=2,
            pm2_5=8.5,
            pm10=14.2,
            co=215.4,
            no=0.1,
            no2=4.8,
            o3=65.3,
            so2=1.2,
            nh3=0.7,
            location=location,
            api=api
        )
        # add records to our sesh
        sess.add(apiReading)
        
        # save records to postgres
        sess.commit()

        # query records we inserted
        apis = sess.query(models.API).all()
        readings = sess.query(models.APIReading).all()

        for api in apis:
            print(api.api_id, api.api_name)

        for reading in readings:
            print(reading.reading_id, reading.recorded_at, reading.aqi, reading.nh3)

    except Exception:
        sess.rollback()
        raise
    finally:
        Session.remove()



if __name__ == "__main__":
    #testParentTables()
    testAPITables()