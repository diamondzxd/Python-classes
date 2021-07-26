from core import *
import dl
from model import *

def AddDoctor():
	doctor=Doctor()
	doctor.name=input("Enter DoctorName : ")
	doctor.address=input("Enter Doctor Address : ")
	doctor.phone=input("Enter Doctor Phone : ")
	doctor.qualification=input("Enter Doctor Specialization : ")
	doctor.gender=input("Enter Doctor Gender : ")
	doctor.visitcharges=input("Enter Doctor Visit Charges : ")
	dl.AddDoctor(doctor)

def EditDoctor():
	doctor=Doctor()
	doctor.doctorid=input("Enter Doctor No. to Edit Record : ")
	doctor=dl.GetDoctor(doctor.doctorid)
	if(doctor!=None):
		print("\nPlease Enter the following details to Edit/Update Record.\nLeave blank for no change\n")

		doctor.name=input("Enter Doctor Name : " + str(doctor.name) + "\n")
		if(doctor.name==""):
			doctor.name=None
		doctor.address=input("Enter Doctor Address : " + str(doctor.address) + "\n")
		if(doctor.address==""):
			doctor.address=None
		doctor.phone=input("Enter Doctor Phone : " + str(doctor.phone) + "\n")
		if(doctor.phone==""):
			doctor.phone=None
		doctor.qualification=input("Enter Doctor Specialization : " + str(doctor.qualification) + "\n")
		if(doctor.qualification==""):
			doctor.qualification=None
		doctor.gender=input("Enter Doctor Gender : " + str(doctor.gender) + "\n")
		if(doctor.gender==""):
			doctor.gender=None
		doctor.visitcharges=input("Enter Doctor Visit Charges : " + str(doctor.visitcharges) + "\n")
		if(doctor.visitcharges==""):
			doctor.visitcharges=None

		dl.EditDoctor(doctor)
	else:
		print("Doctor Not Found")

def DeleteDoctor():
	print("Delete Doctor Details")

def DisplayDoctors():
	doctors=dl.GetDoctors()
	for doctor in doctors:
		print("Doctor Id : " + str(doctor.doctorid))
		print("Name : " + str(doctor.name))
		print("Address : " + str(doctor.address))
		print("Phone : " + str(doctor.phone))
		print("Specialization : " + str(doctor.qualification))
		print("Gender : " + str(doctor.gender))
		print("Visit Charges : " + str(doctor.visitcharges))

def SearchDoctor():
	doctor=Doctor()
	doctor.doctorid=input("Enter Doctor ID to Search Record : ")
	doctor=dl.GetDoctor(doctor.doctorid)
	if(doctor!=None):
		print("Doctor Id : " + str(doctor.doctorid))
		print("Name : " + str(doctor.name))
		print("Address : " + str(doctor.address))
		print("Phone : " + str(doctor.phone))
		print("Specialization : " + str(doctor.qualification))
		print("Gender : " + str(doctor.gender))
		print("Visit Charges : " + str(doctor.visitcharges))
	else:
		print("Doctor Not Found")


def DoctorMenu():
	Header()
	print("\n")
	print("1. Add Doctor")
	print("2. Edit Doctor Details")
	print("3. Delete Doctor Details")
	print("4. Display Doctors List")
	print("5. Search Doctor")
	print("0. Exit")

	print("\n")
	option=int(input("Enter Option : "))
	print("\n")

	if(option==1):
		print("Add New Doctor Record")
		print("-"*40+"\n")
		AddDoctor()
	elif(option==2):
		print("Update Doctor Record")
		print("-"*40+"\n")
		EditDoctor()
	elif(option==3):
		DeleteDoctor()
	elif(option==4):
		DisplayDoctors()
	elif(option==5):
		SearchDoctor()
	else:
		return False

	input()
	return True
