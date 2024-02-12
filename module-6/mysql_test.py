import mysql.connector
from mysql.connector import errorcode



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

mycursor = mydb.cursor()

mycursor.execute("USE DATABASE movies")
