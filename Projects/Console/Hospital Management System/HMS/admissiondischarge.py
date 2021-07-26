from core import *
import dl
from model import *
import datetime

def AdmitPatient():
	admission=Admission()
	admission.patientno=input("Enter Patient No. : ")
	admission.doctorid=input("Enter Treating Doctor Id : ")
	admission.roomno=input("Enter Room Number : ")
	now=datetime.datetime.now()
	admission.admiton=now.strftime('%y-%m-%d %H:%M')
	dl.AddAdmission(admission)

def DischargePatient():
	admissionno=input("Enter Admission No. : ")
	now=datetime.datetime.now()
	dischargedate=now.strftime('%y-%m-%d %H:%M')
	dl.DischargePatient(admissionno,dischargedate)
	GenerateBill(admissionno)
	PrintBillDetails(admissionno)


def GenerateBill(admissionno):
	billdetails=BillDetails()
	billdetails.admissionno=admissionno										#2
	now=datetime.datetime.now()
	billdetails.date=now.strftime('%y-%m-%d %H:%M')							#3
	#Admission Details
	admission=dl.GetAdmission(admissionno)
	#Calculate Room Charges
	room=dl.GetRoom(admission.roomno)
	dayshospitalized=admission.dischargedon-admission.admiton
	if(int(dayshospitalized.seconds/3600)>=1):
		dayshospitalized=dayshospitalized.days+1
	else:
		dayshospitalized=dayshospitalized.days
	billdetails.roomcharges=dayshospitalized*room.roomcharges				#4
	#Pathology Fees
	billdetails.pathologyfees=input("Enter Pathology Charges : ")			#5
	#Doctor Fees
	doctor=dl.GetDoctor(admission.doctorid)
	noofvisits=len(dl.GetDiagnosises(admissionno))
	billdetails.doctorfees=noofvisits*doctor.visitcharges					#6
	#Misc Charges
	billdetails.misccharges=input("Enter Miscelleneous Charges : ")			#7
	#Save Record
	dl.GenerateBill(billdetails)


def PrintBillDetails(admissionno=None):
	if(admissionno==None):
		admissionno=input("Enter Admission No. : ")
	
	billdetails=dl.GetBillDetails(admissionno)
	print("Admission No. : ", billdetails.admissionno)
	print("Date : ", billdetails.date)
	print("Room Charges : ", billdetails.roomcharges)
	print("Pathology Fees  : ", billdetails.pathologyfees)
	print("Doctor Fees : ", billdetails.doctorfees)
	print("Miscelleneous Charges : ", billdetails.misccharges)

def AdmissionDischargeMenu():
	Header()
	print("\n")
	print("1. Admit Patient")
	print("2. Discharge Patient")
	print("3. Download Duplicate Bill")
	print("0. Exit")
	print("\n")

	option=int(input("Enter Option : "))

	if(option==1):
		AdmitPatient()
	elif(option==2):
		DischargePatient()
	elif(option==3):
		PrintBillDetails()
	else:
		return False

	input()
	return True
