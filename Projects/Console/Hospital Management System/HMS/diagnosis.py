from core import *
import dl
from model import *
import datetime

def AddDiagnosis():
	diagnosis=Diagnosis()
	diagnosis.admissionno=input("Enter Admission No. : ")
	#Present Date and Time
	now=datetime.datetime.now()
	diagnosis.dod=now.strftime('%y-%m-%d %H:%M')
	diagnosis.report=input("Enter Diagnosis Report : ")
	dl.AddDiagnosis(diagnosis)

def EditDiagnosis():
	diagnosis=Diagnosis()
	diagnosis.diagnosisid=input("Enter Diagnosis Id to Edit Record : ")
	diagnosis=dl.GetDiagnosis(diagnosis.diagnosisid)
	if(diagnosis!=None):
		print("\nPlease Enter the following details to Edit/Update Record.\nLeave blank for no change\n")

		diagnosis.admissionno=input("Enter Admission No. : " + str(diagnosis.admissionno) + "\n")
		if(diagnosis.admissionno==""):
			diagnosis.admissionno=None
		diagnosis.report=input("Enter Diagnosis Report : " + str(diagnosis.report) + "\n")
		if(diagnosis.report==""):
			diagnosis.report=None

		dl.EditDiagnosis(diagnosis)
	else:
		print("Doctor Not Found")

def DisplayDiagnosis():
	diagnosis=Diagnosis()
	diagnosis.admissionno=input("Enter Admission No. to Search Record : ")
	diagnosises=dl.GetDiagnosises(diagnosis.admissionno)
	for diagnosis in diagnosises:
		print("Diagnosis Id : " + str(diagnosis.diagnosisid))
		print("Admission No. : " + str(diagnosis.admissionno))
		print("Date/Time of Diagnosis : " + str(diagnosis.dod))
		print("Diagnosis Report : " + str(diagnosis.report))


def DiagnosisMenu():
	Header()
	print("\n")
	print("1. Add Diagnosis Record")
	print("2. Edit Diagnosis Record")
	print("3. View Treatment History")
	print("0. Exit")
	print("\n")

	option=int(input("Enter Option : "))

	if(option==1):
		AddDiagnosis()
	elif(option==2):
		EditDiagnosis()
	elif(option==3):
		DisplayDiagnosis()
	else:
		return False

	input()
	return True
