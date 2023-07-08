import os, sys
import psycopg2
import logging

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="edteam_db",
        user="root",
        password="root")
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
        cur.execute('DROP TABLE IF EXISTS transactions;')
        cur.execute('CREATE TABLE transactions (id serial PRIMARY KEY,'
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