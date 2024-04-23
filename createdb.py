import mysql.connector

# Connect to MySQL server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

# Create a database
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE village_rentals")

# Connect to the newly created database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="village_rentals"
)

# Create tables
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE equipment ("
                 "id INT AUTO_INCREMENT PRIMARY KEY,"
                 "name VARCHAR(255),"
                 "description VARCHAR(255),"
                 "category VARCHAR(255),"
                 "daily_rental_cost FLOAT"
                 ")")

mycursor.execute("CREATE TABLE clients ("
                 "id INT AUTO_INCREMENT PRIMARY KEY,"
                 "last_name VARCHAR(255),"
                 "first_name VARCHAR(255),"
                 "contact_phone VARCHAR(20),"
                 "email VARCHAR(255)"
                 ")")

mycursor.execute("CREATE TABLE rentals ("
                 "id INT AUTO_INCREMENT PRIMARY KEY,"
                 "client_id INT,"
                 "equipment_id INT,"
                 "rental_date DATE,"
                 "return_date DATE,"
                 "cost FLOAT,"
                 "FOREIGN KEY (client_id) REFERENCES clients(id),"
                 "FOREIGN KEY (equipment_id) REFERENCES equipment(id)"
                 ")")

print("Database and tables created successfully!")
