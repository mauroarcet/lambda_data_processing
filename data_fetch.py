import boto3
import psycopg2
from config import config

def get_real_states_prices():
    conn = None

    real_states_prices_query = """
                        SELECT price
                        FROM real_states
                        """
    real_states_prices = []

    try:
        params = config()
        print('Connecting to the AWS RDS database...')

        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        print("Fetching data from database...")
        cur.execute(real_states_prices_query)

        rows = cur.fetchall()

        for row in rows:
            real_states_prices.append(row[0])

        cur.close()

        return(real_states_prices)

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
