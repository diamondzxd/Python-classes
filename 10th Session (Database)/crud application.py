#Inserting a Record in Database Table.

import MySQLdb

#Step 1 : Establish a Connection

con=MySQLdb.connect('localhost',user='root',password='')

#Step 2 : Selecting the Database

con.select_db('aptech24')

#Step 3 : Creating Cursor Object

cur=con.cursor()

#Choice

print("1. Create Record")
print("2. Read Record")
print("3. Update Record")
print("4. Delete Record")
choice=int(input("Enter your Choice from the above."))

if(choice==1):
    id=input("Enter ID : ")
    name=input("Input Name : ")
    course=input("Input Course : ")
    fees=input("Enter Fees : ")
    query="INSERT INTO STUDENT VALUES(%s,%s,%s,%s)"
    parameters=(id,name,course,fees)
    result=cur.execute(query,parameters)
    con.commit()
    con.close()
    
elif(choice==2):
    try:
        
        id=int(input("Enter the ID you want to search."))
        query="SELECT * FROM STUDENT where id=(%s)"
        parameters=(id,)
        result=cur.execute(query,parameters)
        student=cur.fetchone()
        id,name,course,fee=student
        print("ID : "+str(id))
        print("Name : "+name)
        print("Course : "+course)
        print("Fees : "+str(fee))
        con.close()

    except:
        print("Incorrect ID Entered.")

elif(choice==3):
    id=int(input("Enter the ID you want to update."))
    

#Step 5 : Fetching Database Records
# fetchone() : Fetches a single record from the dataset and returns a tuple of values
# fetchall() : Fetches all records from the dataset and returns a tuple of tuples.

#Step 6 : Close the connection
