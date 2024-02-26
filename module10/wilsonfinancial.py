import mysql.connector

# Database connection parameters
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="wilsonfinancial"
)

# create a cursor object
crsr = db.cursor()

#  create variable called tables and list an array with the tables within the database
tables = ['clientassets', 'clients', 'clienttransactions', 'employees', 'officesupplies', 'portallogin']

# make a for loop to display all the data within all the tables one after another 
for table_name in tables:
    print(f"\nDisplaying '{table_name}':") # prints the title of the table using the array
    data = f"SELECT * FROM {table_name};" # gets all the data within that same table and assign action to "data"
    crsr.execute(data) # executes the sql action to get data
    
    # fetch all rows and appends it to the rows variable
    rows = crsr.fetchall()

    # prints the names of the columns separated by tabs beneath the table names
    columns = [desc[0] for desc in crsr.description] 
    print("\t".join(columns)) 

    # display the data within the rows separated by tabs
    for row in rows:
        print("\t".join(map(str, row))) 

# closes the crsr
crsr.close()
