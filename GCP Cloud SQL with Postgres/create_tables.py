import configparser
import sqlalchemy
import psycopg2
from sqlalchemy import create_engine
#from google.cloud.sql.connector import connector
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(conn):
    """
    This function drops all tables. 
    
    INPUTS: 
    * cur = the cursor variable
    * conn = the connection variable
    """
    for query in drop_table_queries:
        conn.execute(query)
        conn.execute("COMMIT")


def create_tables(conn):
    """
    This function creates all tables. 
    
    INPUTS: 
    * cur = the cursor variable
    * conn = the connection variable
    """
    for query in create_table_queries:
        conn.execute(query)
        conn.execute("COMMIT")


def main():
    """
    This function parsers all config information from dwh.cjg file storing them into the cursor and connection variables. Then executes drop_tables and create_tables functions. Both functions are explained above.
    """
    
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    # initialize Connector object
    #connector = Connector()

        # function to return the database connection
    #def getconn() -> pg8000.connections.Connection:
        #conn: pg8000.connections.Connection = connector.connect(
        #    {},{},user={},password={},db={}).format(*config['GCP'].values())
    #return conn

    # create connection pool
    #pool = sqlalchemy.create_engine(
        #"postgresql+pg8000://",
        #creator=getconn,
        #)

    #conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['GCP'].values()))
    #conn = connector.connect({},{},user={},password={},db={}).format(*config['GCP'].values())
    #trim-mix-266820:us-west1:my-sql-instance

    db_url = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(*config['GCP'].values())

    engine = sqlalchemy.create_engine(db_url)

    conn = engine.connect()

    #conn.execute("COMMIT")
   
# Execute a query
    #cur = conn.cursor()

    drop_tables(conn)
    create_tables(conn)

    conn.close()


if __name__ == "__main__":
    main()