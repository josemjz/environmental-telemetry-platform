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

def testChildrenTables():
    sess = Session()

    try:
        ## Create test records for parent tables first 
        source = models.Source(source_name="OpenWeather_test_1", source_type="API_1")

        # griffith observatory coords
        location = models.Location(location_name="Griffith Observatory", lat=34.1184, lon=-118.3005)

        # add parent records to sesh before children to avoid source_id being None
        sess.add(source)
        sess.add(location)
        sess.flush() # This makes it so the transactions take place but are not commited to the disk, so that we can enter future child tables 

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

        # now adding some test records for children tables

        # save records to postgres
        sess.commit()


if __name__ == "__main__":
    testParentTables()