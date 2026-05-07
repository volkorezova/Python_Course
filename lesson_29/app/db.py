import psycopg2
import os
import time

def get_connection():
    for _ in range(10):  # retry щоб контейнер дочекався БД
        try:
            return psycopg2.connect(
                dbname="testdb",
                user="user",
                password="password",
                host="host.docker.internal",
                port="5432"
            )
        except:
            print("DB not ready, retry...")
            time.sleep(2)
    raise Exception("Cannot connect to DB")