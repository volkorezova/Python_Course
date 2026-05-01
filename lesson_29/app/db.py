import psycopg2
import os
import time

def get_connection():
    for _ in range(10):  # retry щоб контейнер дочекався БД
        try:
            return psycopg2.connect(
                dbname=os.getenv("POSTGRES_DB"),
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port="5432"
            )
        except:
            print("DB not ready, retry...")
            time.sleep(2)
    raise Exception("Cannot connect to DB")