import pandas as pd 
import pg8000
from dotenv import load_dotenv
import os

#df = pd.read_excel('people sample.xlsx')
#print(type(df))


def connect_to_db():
    """ Connect to databse. """
    # Load environment variables from .env file
    load_dotenv()
    print(f"DB_PORT: {os.getenv('DB_PASSWORD')}")
    # Database connection details
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_PORT = int(os.getenv("DB_PORT"))

    try:
        # Connect to the database
        connection = pg8000.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        print("Connection successful!")
    except Exception as e:
        print("Sorry, we are unable to connect to your database:", e)
    finally:
        if connection:
            connection.close()

if __name__=="__main__":
    connect_to_db()

