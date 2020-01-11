import boto3
import psycopg2
import sqlalchemy as db

from config_real_states_db import config


def connect():
    params = config()
    connect = psycopg2.connect(**params)
    return connect


def get_real_states_prices():
    real_states_prices = []

    try:
        print('Connecting to the AWS RDS database...')
        engine = db.create_engine('postgresql://', creator=connect)
        connection = engine.connect()
        metadata = db.MetaData()
        real_states = db.Table('real_states', metadata, autoload=True,
                               autoload_with=engine)

        query = db.select([real_states.columns.price])

        result_proxy = connection.execute(query).fetchall()

        for row_proxy in result_proxy:
            real_states_prices.append(row_proxy[0])

        return(real_states_prices)

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
