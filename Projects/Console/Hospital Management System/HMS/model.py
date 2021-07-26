 #Model Classes

class Doctor:
	def __init__(self,doctorid=None,name=None,address=None,phone=None,qualification=None,gender=None,visitcharges=None):
		self.doctorid=doctorid
		self.name=name
		self.address=address
		self.phone=phone
		self.qualification=qualification
		self.gender=gender
		self.visitcharges=visitcharges


class Patient:
	def __init__(self,patientno=None,name=None,age=None,gender=None,address=None,contactno=None):
		self.patientno=patientno
		self.name=name
		self.age=age
		self.gender=gender
		self.address=address
		self.contactno=contactno


class Room:
	def __init__(self,roomno=None,roomtype=None,occupancy=None,roomcharges=None):
		self.roomno=roomno
		self.roomtype=roomtype
		self.occupancy=occupancy
		self.roomcharges=roomcharges


class Diagnosis:
	def __init__(self,diagnosisid=None,admissionno=None,dod=None,report=None):
		self.diagnosisid=diagnosisid
		self.admissionno=admissionno
		self.dod=dod
		self.report=report

class Admission:
	def __init__(self,admissionno=None, patientno=None, doctorid=None, roomno=None, admiton=None, dischargedon=None):
		self.admissionno=admissionno
		self.patientno=patientno
		self.doctorid=doctorid
		self.roomno=roomno
		self.admiton=admiton
		self.dischargedon=dischargedon

class BillDetails:
	def __init__(self, billno=None, admissionno=None, date=None, roomcharges=None, pathologyfees=None, doctorfees=None, misccharges=None):		
		self.billno=billno
		self.admissionno=admissionno
		self.date=date
		self.roomcharges=roomcharges
		self.pathologyfees=pathologyfees
		self.doctorfees=doctorfees
		self.misccharges=misccharges
