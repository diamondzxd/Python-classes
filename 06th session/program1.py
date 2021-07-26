class Student:
    id=1
    objecte='Piyush'
    course='Python'
    fees=50000.0

s=Student()

s.id=int(input("Enter Student ID : "))
s.name=input("Enter a name : ")


#Note: In Python, all members are public by default.

#Creating an object of a class

#Student s=new Student;		//java
#Student s;					//C++


#s=Student()					#Python

#Accessing class Members

print(s.id)
print(s.name)
print(s.course)
print(s.fees)
