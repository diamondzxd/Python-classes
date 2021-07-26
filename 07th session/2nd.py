class Bank():
    acno=0
    name=''
    branch=''
    balance=0.0

    def Input(self,acno,name,branch,balance):
        self.acno=acno
        self.name=name
        self.branch=branch
        self.balance=balance

    def Output(self):
        print("Account Number : ",acno)
        print("Name : ",name)
        print("Branch : ",branch)
        print("balance : ",balance)

class BankV1(Bank):
    aadhar=0
    def Input(self,acno,name,branch,balance,aadhar):
        Bank.Input(self,acno,name,branch,balance)
        self.aadhar=input("Enter your Aadhar Number")

    def Output(self):
        Bank.Output(self)
        print(aadhar)

Bank=BankV1()
Bank.Input(1234,"Piyush","sec-3",12345,77758475847)
Bank.Output()
