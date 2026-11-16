import os
from pathlib import Path

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import text

# load db credentials from the .env file
load_dotenv(Path(__file__).resolve().parent / ".env")


db_url = os.environ["DB_URL"]

# Create the db engine and config connection pooling
engine = create_engine(
    db_url,
    pool_size=5, 
    pool_recycle=3600,
    pool_pre_ping=True, 
    echo=True
    )

# Creates session factory for db ops.
session_factory = sessionmaker(bind=engine)

# Manage db sessions
Session = scoped_session(session_factory)

# Test the db connection when this file is ran directly
if __name__ == "__main__":
    with engine.connect() as conn:
        print(conn.execute(text('SELECT current_database()')).scalar())

