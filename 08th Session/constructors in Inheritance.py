#Consturctors in Inheritance
#For Constructor : __init__
#For Destructor : __del__


'''class Base:
	def __init__(self):
		print("Parent Consturctor Called")

class Derive(Base):
	def __init__(self):
		Base.__init__(self)			#Manually calling the parent constructor if required.
		print("Child Consturctor Called")

d=Derive()'''


#Bank Example for calling parametrized constructor.


'''class Bank:
	acno=0
	name=''
	branch=''
	balance=0.0

	def __init__(self,acno,name,branch):
		self.acno=acno
		self.name=name
		self.branch.branch
		self.balance=balance

	def SetName(self,name):		#Setter (Mutator in C++) Function : Function used to change the value of a variable.
		self.name=name

	def SetAcno(self,branch):	#Setter
		self.acno=acno

	def SetBranch(self,branch):	#Setter
		self.branch=balance

	def SetBalance(self,balance): #Setter
		self.balance=balance

	def GetAcno(self):		#Getter (Accessor in C++) Function : To access the value of a particular variable.
		return acno

	def GetName(self):
		return name

	def GetBranch(self):
		return branch

	def GetBalance(self):
		return balance'''


#Constructors in Derived Classes

class Bank:
	def __init__(self,acno,name,branch):
		self.acno=acno
		self.name=name
		self.branch=branch

		''''''

class Saving:
	def __init__(self,acno,name,branch,balance):
		Bank.__init__(self,acno,name,branch)
		self.balance=balance

		''''''

c=Saving(12345,'Piyush Dhall','Rohini',50000)