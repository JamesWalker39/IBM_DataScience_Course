import pandas as pd
import pandas.io.sql
import pyodbc
# Parameters
server = 'localhost'
db = 'sample_db'

# Create the connection

conn_str = (
    "DRIVER={PostgreSQL ODBC Driver(UNICODE)};"
    "DATABASE=sample_db;"
    "UID=postgres;"
    "PWD=Jamesw39!;"
    "SERVER=localhost;"
    "PORT=5432;"
    )
conn = pyodbc.connect(conn_str)

cursor = conn.cursor()

#show all tables
cursor.tables()
rows = cursor.fetchall()
for row in rows:
        print (row.table_name)

# ------insert into ------------------

# #SQL to run
# sql = """
# INSERT INTO 
#     people (id, name)
# VALUES 
#     (7, 'Brian')
# """

# # insert into
# cursor = conn.cursor()
# # using SQL within code ---- cursor.execute("INSERT INTO people (id, name) VALUES (6, 'Scott')")
# cursor.execute(sql) # using sql as a param
#  # commit the changes to the database
# conn.commit()
# # close communication with the database
# conn.close()

#----------Select from SQL query-----------------
sql = """
SELECT * FROM people
"""

#----------add to df pandas-----------------
sql_df = pd.read_sql_query(sql, conn)
print(sql_df)
print (sql_df['name'])

# alternative - df = pd.DataFrame(sql_df,columns=['id','name']) # columns optional
# print (df['name'])