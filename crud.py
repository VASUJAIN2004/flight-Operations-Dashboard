import mysql.connector

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Vasu@2004",
        database="flights"
    )

    mycursor = conn.cursor()
    print("Connected to database")

except Exception as e:
    print("Unable to connect to database")
    print("Error:", e)

#create a database on db server(ekk bar hi krna hn)
# mycursor.execute("CREATE DATABASE flights")
# conn.commit()
#create a table
# mycursor.execute("""
# CREATE TABLE airport(
#     airport_id INTEGER PRIMARY KEY,
#     code VARCHAR(10) NOT NULL,
#     city VARCHAR(50) NOT NULL,
#     name VARCHAR(255) NOT NULL
# )
# """)
# conn.commit()

# Insert data to the table
# mycursor.execute("""
#     INSERT INTO airport VALUES
#     (1,'DEL','New Delhi','IGIA'),
#     (2,'CCU','Kolkata','NSCA'),
#     (3,'BOM','Mumbai','CSMA')
# """)
# conn.commit()
# Search/Retrieve
mycursor.execute("SELECT * FROM airport WHERE airport_id > 1")
data = mycursor.fetchall()
print(data)

for i in data:
    print(i[3])

# Update
mycursor.execute("""
UPDATE airport
SET name = 'Bombay'
WHERE airport_id = 3
""")
conn.commit()

mycursor.execute("SELECT * FROM airport")
data = mycursor.fetchall()
print(data)

# DELETE
mycursor.execute("DELETE FROM airport WHERE airport_id = 3")
conn.commit()

mycursor.execute("SELECT * FROM airport")
data = mycursor.fetchall()
print(data)

