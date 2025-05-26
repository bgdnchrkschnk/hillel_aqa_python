import os

from dotenv import load_dotenv
import psycopg2
# import sqlite3
# import mysql

load_dotenv()

class PostresDB:

    def __init__(self):
        self.dbname = os.getenv("db_name")
        self.user = os.getenv("user")
        self.password = os.getenv("password")
        self.host = os.getenv("host")
        self.port = os.getenv("port")
        self.__set_connection()


    def __set_connection(self):
        try:
            self.__connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.__connection.autocommit = True
            print("Connected to the database successfully!")
            self.__cursor = self.__connection.cursor()
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    @property
    def cursor(self):
        return self.__cursor

    @property
    def conn(self):
        return self.__connection

    def select(self, query) -> list[tuple] | None: # only for selects
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def mutation(self, query) -> None: # for inserts, updates, deletes
        self.cursor.execute(query)

    def close(self):
        self.cursor.close()
        self.__connection.close()
        print("Connection closed")

    def __del__(self):
        self.close()
        self.conn.close()

if __name__ == "__main__":
    db_client = PostresDB()
    query: str = f"INSERT INTO products (name) VALUES ('Lamp');"
    db_client.mutation(query=query)
    result = db_client.select("SELECT * FROM products")

    print(result)
    del db_client
