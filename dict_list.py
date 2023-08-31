import sqlite3

# Connect to the database
connection = sqlite3.connect('C:\Login Data.db')

# Create a cursor
cursor = connection.cursor()

# Execute SQL query
query = "SELECT * FROM keyword_search_terms;"
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Process the fetched data
for row in rows:
    print(row)

# Close cursor and connection
cursor.close()
connection.close()
