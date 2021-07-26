#Inserting a Record in Database Table.

import MySQLdb

#Step 1 : Establish a Connection

con=MySQLdb.connect('localhost',user='root',password='')

#Step 2 : Selecting the Database

con.select_db('aptech24')

#Step 3 : Creating Cursor Object

cur=con.cursor()

#Step 4 : Executing Query

id=input("Enter ID : ")
name=input("Input Name : ")
course=input("Input Course : ")
fees=input("Enter Fees : ")

query="INSERT INTO STUDENT VALUES(%s,%s,%s,%s)"
parameters=(id,name,course,fees)
result=cur.execute(query,parameters)

print(result)

#Step 5 : Commit

con.commit()

#Step 6 : Close the connection
con.close()
