class Bank:
    acno=0
    name=''
    branch=''
    balance=0.0

    def __init__(self,acno,name,branch,balance):
        self.acno=acno
        self.name=name
        self.branch=branch
        self.balance=balance

    def SetName(self,name):         #Setter
        self.name=name

    def SetBranch(self,branch):     #Setter
        self.branch=branch

    def SetBalance(self,balance):   #Setter
        self.balance=balance

    def GetAcno(self):                #Getter        
        return self.acno

    def GetName(self):
        return self.name

    def GetBranch(self):
        return self.branch

    def GetBalance(self):
        return self.balance

    
    
        
