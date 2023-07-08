from dotenv import load_dotenv
load_dotenv()

import os, sys
import psycopg2
import logging

def get_db_connection():
    conn = psycopg2.connect(
        host = os.environ['POSTGRES_HOST'],
        database = os.environ['POSTGRES_DB'],
        user = os.environ['POSTGRES_USER'],
        password = os.environ['POSTGRES_PASSWORD'])
    return conn

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def create_table():
    cur = ''
    try:
        # Open a cursor to perform database operations
        conn = get_db_connection()
        cur = conn.cursor()

        # Execute a command: this creates a new table
        # cur.execute('DROP TABLE IF EXISTS transactions;')
        cur.execute('CREATE TABLE IF NOT EXISTS transactions (id serial PRIMARY KEY,'
                    'id_client integer NULL,'
                    't_balance float NOT NULL,'
                    'tx_for_month JSONB NULL,'
                    'avg_debit float NOT NULL,'
                    'avg_credit float NOT NULL,'
                    'date_added date DEFAULT CURRENT_TIMESTAMP);'
                    )
        conn.commit()

        cur.close()
        conn.close()
    except:
        logger.error("ERROR: Could not connect to Postgres instance.")
        sys.exit()