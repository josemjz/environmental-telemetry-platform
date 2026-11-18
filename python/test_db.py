from db_connection import Session
from models import Source, Location

def testParentTables():
    sess = Session()

    try:
        # create test records
        source = Source("OpenWeather_test_1", "API_1")

        # griffith observatory coords
        location = Location("Griffith Observatory", 34.1184, -118.3005)

        # add records to our sesh
        sess.add(source)
        sess.add(location)

        # save records to postgres
        sess.commit()

        # query the records we inserted above
        sources = sess.query(Source).all()
        locations = sess.query(Location).all()

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

if __name__ == "__main__":
    testParentTables()