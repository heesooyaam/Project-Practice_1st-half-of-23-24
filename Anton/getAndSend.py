import sqlite3

login = input()
password = input()
# Establish a connection to the database
db_connection = sqlite3.connect("DBs/your_database.db")

cursor = db_connection.cursor()

query = "SELECT * FROM your_table"

cursor.execute(query)

data = cursor.fetchall()

processed_data = ""
for row in data:
    processed_data += f"{row}\n"

print(processed_data)

cursor.close()
db_connection.close()