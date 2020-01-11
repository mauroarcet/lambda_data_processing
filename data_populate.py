import boto3
import psycopg2
import sqlalchemy as db

from config_data_process import config


def connect():
    params = config()
    connect = psycopg2.connect(**params)
    return connect

# TODO: Refactor this


def populate_db(mean, min_value, max_value, created_at):
    try:
        print('Connecting to data processing database...')
        engine = db.create_engine('postgresql://', creator=connect)
        connection = engine.connect()
        metadata = db.MetaData()

        data_processing = db.Table('data_processing', metadata, autoload=True,
                                   autoload_with=engine)

        print("Inserting processed data...")

        query = db.insert(data_processing).values(
            mean=mean,
            min_value=min_value,
            max_value=max_value,
            created_at=created_at)

        connection.execute(query)

    except:
        return "Error connecting to database"
