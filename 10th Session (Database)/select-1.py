#Inserting a Record in Database Table.

import MySQLdb

#Step 1 : Establish a Connection

con=MySQLdb.connect('localhost',user='root',password='')

#Step 2 : Selecting the Database

con.select_db('aptech24')

#Step 3 : Creating Cursor Object

cur=con.cursor()

#Step 4 : Executing Query

query="SELECT * FROM STUDENT"
result=cur.execute(query)

print(result)

#Step 5 : Fetching Database Records
# fetchone() : Fetches a single record from the dataset and returns a tuple of values
# fetchall() : Fetches all records from the dataset and returns a tuple of tuples.

students=cur.fetchall()

for student in students:
    print("ID : ",student[0])
    print("Name : ",student[1])
    print("Course : ",student[2])
    print("Fees : ",student[3])

#Step 6 : Close the connection
con.close()
