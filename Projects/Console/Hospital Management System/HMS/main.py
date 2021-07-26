from core import *
from dl import *
from model import *
from admissiondischarge import *
from room import *
from doctor import *
from patient import *
from diagnosis import *
import datetime
import os


def MainMenu():
	Header()
	print("\n")
	print()
	print("1. Manage Admission/Discharge Details")
	print("2. Manage Doctor Details")
	print("3. Manage Patient Details")
	print("4. Manage Diagnosis Details")
	print("5. Manage Room Details")
	print("0. Exit")
	print("\n")

	option=int(input("Enter Option : "))

	if(option==1):
		while AdmissionDischargeMenu():
			pass
	elif(option==2):
		while DoctorMenu():
			pass
	elif(option==3):
		while PatientMenu():
			pass
	elif(option==4):
		while DiagnosisMenu():
			pass
	elif(option==5):
		while RoomMenu():
			pass
	else:
		return False

	input()
	return True

while MainMenu():
	pass
