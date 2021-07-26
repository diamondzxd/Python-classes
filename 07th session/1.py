#1st example

'''class Base:
    def Fun():
        print("Hello World")

class Derive(Base):
    def AnotherFun():
        print("Bye World")


obj=Derive()
obj.Fun()
obj.AnotherFun()'''


#2nd example
#-----------------------------------

class Bank:
    acno=0
    name=''
    branch=''
    balance=0.0
    def Input(self):
            acno=int(input("Enter Account Number"))
            name=input("Enter your name")
            branch=input("Enter your Branch Name")
            balance=float(input("Enter your Bank Balance"))

    def Output(self):
            print("Account Number : ", self.acno)
            print("Name : ", self.name)
            print("Branch : ", self.branch)
            print("Bank Balance : ", self.balance)
        

    def Fun(self):
            print("test")

class BankV1(Bank):
    aadhar=0

    def Input(self):        #Overriding
        Bank.Input(self)
        self.aadhar=input("Enter Aadhar Number : ")
    def Output(self):
        Bank.Output(self)   #Overriding
        print("Your Aadhar Number is : ", self.aadhar)



c=BankV1()
c.Input()
c.Output()
