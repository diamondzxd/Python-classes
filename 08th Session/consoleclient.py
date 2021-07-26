from Bank import Bank

acno=input("Enter Account Number : ")
name=input("Enter Name : ")
branch=input("Enter Branch")
balance=input("Enter Initial Balance")

b=Bank(acno,name,branch,balance)

print("Account Number : ", b.GetAcno())
print("Name : ", b.GetName)