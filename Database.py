import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import psycopg2


try:
    conn = psycopg2.connect(
        host="localhost",
        database="Admin",
        user="postgres",
        password="login123"
    )
    print("Connected to the PostgreSQL database!")
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL:", error)
    sys.exit(1)


    # this is about database connection by jay
    

