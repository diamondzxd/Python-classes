from core import *
import dl
from model import *


def AddPatient():
	patient=Patient()
	patient.name=input("Enter Patient Name : ")
	patient.age=input("Enter Patient Age : ")
	patient.gender=input("Enter Patient Gender : ")
	patient.address=input("Enter Patient Address : ")
	patient.contactno=input("Enter Patient Contact Number : ")
	dl.AddPatient(patient)

def EditPatient():
	patient=Patient()
	patient.patientno=input("Enter Patient No. to Edit Record : ")
	patient=dl.GetPatient(patient.patientno)
	if(patient!=None):
		print("\nPlease Enter the following details to Edit/Update Record.\nLeave blank for no change\n")

		patient.name=input("Enter Patient Name : " + str(patient.name) + "\n")
		if(patient.name==""):
			patient.name=None
		patient.age=input("Enter Patient Age : "+ str(patient.age) + "\n")
		if(patient.age==""):
			patient.age=None
		patient.gender=input("Enter Patient Gender : " + str(patient.gender) + "\n")
		if(patient.gender==""):
			patient.gender=None
		patient.address=input("Enter Patient Address : " + str(patient.address) + "\n")
		if(patient.address==""):
			patient.address=None
		patient.contactno=input("Enter Patient Contact Number : " + str(patient.contactno) + "\n")
		if(patient.contactno==""):
			patient.contactno=None


		dl.EditPatient(patient)
	else:
		print("Room Not Found")


def DisplayPatients():
	patients=dl.GetPatients()
	for patient in patients:
		print("Patient Number : " + str(patient.patientno))
		print("Name : " + str(patient.name))
		print("Age : " + str(patient.age))
		print("Gender : " + str(patient.gender))
		print("Address : " + str(patient.address))
		print("Contact Number : " + str(patient.contactno))

def SearchPatient():
	patient=Patient()
	patient.patientno=input("Enter Patient No. to Edit Record : ")
	patient=dl.GetPatient(patient.patientno)
	if(patient!=None):
		print("Name : " + str(patient.name))
		print("Age : " + str(patient.age))
		print("Gender : " + str(patient.gender))
		print("Address : " + str(patient.address))
		print("Contact Number : " + str(patient.contactno))
	else:
		print("Patient Not Found")

def PatientMenu():
	Header()
	print("\n")
	print("1. Add Patient")
	print("2. Edit Patient Details")
	print("3. Display Patients List")
	print("4. Search Patient")
	print("0. Exit")
	print("\n")

	option=int(input("Enter Option : "))

	if(option==1):
		AddPatient()
	elif(option==2):
		EditPatient()
	elif(option==3):
		DisplayPatients()
	elif(option==4):
		SearchPatient()
	else:
		return False

	input()
	return True
