from sqlalchemy.orm import configure_mappers

# import our models so sqlalchemy can register them
import python.test_models as test_models

# validate ORM configuration
def testModelRelationships():
    # mapper will connect a python class to its db table
    configure_mappers()
    print("ORM relationships configured successfully")


if __name__ == "__main__":
    testModelRelationships()

