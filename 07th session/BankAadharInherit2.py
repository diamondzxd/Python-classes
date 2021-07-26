class Bank:
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
        print("Account Number: ",self.acno)
        print("Name: ",self.name)
        print("Branch: ",self.branch)
        print("Balance: ",self.balance)

class BankV1(Bank):
    aadhar=0

    def Input(self,acno,name,branch,balance,aadhar):
        Bank.Input(self,acno,name,branch,balance)
        self.aadhar=aadhar

    def Output(self):
        Bank.Output(self)
        print("Aadhar Number:",self.aadhar)

c=BankV1()
c.Input(1234,"shiv","RK Puram",1200.0,1323434)
c.Output()

