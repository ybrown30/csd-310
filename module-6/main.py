import mysql.connector
from mysql.connector import errorcode

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)


mycursor = mydb.cursor()

print(mydb)

mydb.close()