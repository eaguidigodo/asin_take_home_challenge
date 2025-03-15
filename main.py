import pandas as pd 
import pg8000
from dotenv import load_dotenv
from datetime import datetime
import os
import time
import argparse
import sys


def connect_to_db(data=None):
    """ Connect to databse. """
    # Load environment variables from .env file
    load_dotenv()
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
        print("Connection successful! We will now create the table that will store your data....")
    except Exception as e:
        print("Sorry, we are unable to connect to your database:", e)
    else:
        cursor = connection.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS people (
                       id SERIAL PRIMARY KEY,
                       matricule VARCHAR(255),
                       nom VARCHAR(255), 
                       prenom VARCHAR(50),
                       datedenaissance VARCHAR(255),
                       status VARCHAR(255)
                    )
                       """
        )
        print("Table created!")
        print("It's almost done! It's the last step. Your data is being inserted into a database. This may take some time. Wait please until it's completed....")
        if data is not None:
            query = "INSERT INTO people (matricule, nom, prenom, datedenaissance, status) VALUES (%s, %s, %s, %s, %s)"
            cursor.executemany(query, data)
            connection.commit()
            return cursor.rowcount
    finally:
        if connection:
            connection.close()

# def standardise_date(date_str):
#     date_obj = datetime.strptime(date_str, "%d/%m/%Y")
#     date_pg = date_obj.strftime("%Y-%m-%d")
#     return date_pg

def import_data(xls_file_path):
    """ Import data from excel file to database. """
    start_time = time.time()
    print(f"We are reading {xls_file_path} that you provide us...")
    try:
        df = pd.read_excel('people sample.xlsx')
        expected_columns = {"matricule","nom","prenom","datedenaissance","status"}
        if not expected_columns.issubset(df.columns):
            print("Sorry, seems that your file does not contains expected columns.")
            return None
        people = []
        print("We retrived your data. We are preparing them to insert them into the database.")
        for _, row in df.iterrows():
            people.append((row["matricule"], row["nom"], row["prenom"], row["datedenaissance"], row["status"]))
        print("Everything is going smoothly. Now we are about to connect to your database....")
        rowcount = connect_to_db(people)
        print(f"{rowcount} rows successful added.")
        print(f"Import completed in {time.time() - start_time:.2f} seconds.")

    except Exception as e:
        print("Sorry, we got an error while importing data from your files.", e)
        return None


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Import file from excel file to a database.')
    parser.add_argument("filename", help="Path of the excel file to import.")
    args = parser.parse_args()
    
    xls_file_path = args.filename
    import_data(xls_file_path)


