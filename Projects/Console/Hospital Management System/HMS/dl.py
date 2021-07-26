#Database Logic Layer
import MySQLdb
from model import *

def getConnection():
	con=MySQLdb.connect('localhost',user='root',password='')
	con.select_db('hms')
	return con




#Doctor Table
def AddDoctor(doctor):
	con=getConnection()
	cur=con.cursor()
	data=(doctor.name, doctor.address, doctor.phone, doctor.qualification, doctor.gender, doctor.visitcharges)
	query="INSERT INTO doctor (name,address,phone,qualification,gender,visitcharges) values(%s,%s,%s,%s,%s,%s)"
	cur.execute(query,data)
	con.commit()
	con.close()	


def EditDoctor(doctor):
	con=getConnection()
	cur=con.cursor()
	data=[]
	query="UPDATE doctor set"
	if(doctor.name!=None):
		query=query+" name=%s,"
		data.append(doctor.name)
	if(doctor.address!=None):
		query=query+" address=%s,"
		data.append(doctor.address)
	if(doctor.phone!=None):
		query=query+" phone=%s,"
		data.append(doctor.phone)
	if(doctor.qualification!=None):
		query=query+" qualification=%s,"
		data.append(doctor.qualification)
	if(doctor.gender!=None):
		query=query+" gender=%s,"
		data.append(doctor.gender)
	if(doctor.visitcharges!=None):
		query=query+" visitcharges=%s,"
		data.append(doctor.visitcharges)

	data.append(doctor.doctorid)
	data=tuple(data)
	query=query[:len(query)-1]+" where doctorid=%s"
	cur.execute(query,data)
	con.commit()
	con.close()	


def GetDoctor(doctorid):
	con=getConnection()
	cur=con.cursor()
	data=(doctorid,)
	query="SELECT * FROM doctor where doctorid=%s"
	cur.execute(query,data)
	record=cur.fetchone()
	doctor=Doctor(record[0],record[1],record[2],record[3],record[4],record[5],record[6])
	return doctor
	con.close()	


def GetDoctors():
	con=getConnection()
	cur=con.cursor()
	query="SELECT * FROM doctor"
	cur.execute(query)
	records=cur.fetchall()
	doctors=[]
	for record in records:
		doctor=Doctor(record[0],record[1],record[2],record[3],record[4],record[5],record[6])
		doctors.append(doctor)
	return doctors
	con.close()	




#Doctor Table
def AddPatient(patient):
	con=getConnection()
	cur=con.cursor()
	data=(patient.name, patient.age, patient.gender, patient.address, patient.contactno)
	query="INSERT INTO patient (name,age,gender,address,contactno) values(%s,%s,%s,%s,%s)"
	cur.execute(query,data)
	con.commit()
	con.close()	

def EditPatient(patient):
	con=getConnection()
	cur=con.cursor()
	data=[]
	query="UPDATE patient set"
	if(patient.name!=None):
		query=query+" name=%s,"
		data.append(patient.name)
	if(patient.age!=None):
		query=query+" age=%s,"
		data.append(patient.age)
	if(patient.gender!=None):
		query=query+" gender=%s,"
		data.append(patient.gender)
	if(patient.address!=None):
		query=query+" address=%s,"
		data.append(patient.address)
	if(patient.contactno!=None):
		query=query+" contactno=%s,"
		data.append(patient.contactno)

	data.append(patient.patientno)
	data=tuple(data)
	query=query[:len(query)-1]+" where patientno=%s"
	cur.execute(query,data)
	con.commit()
	con.close()	


def GetPatient(patientno):
	con=getConnection()
	cur=con.cursor()
	data=(patientno,)
	query="SELECT * FROM patient where patientno=%s"
	cur.execute(query,data)
	record=cur.fetchone()
	patient=Patient(record[0],record[1],record[2],record[3],record[4],record[5])
	return patient
	con.close()	


def GetPatients():
	con=getConnection()
	cur=con.cursor()
	query="SELECT * FROM patient"
	cur.execute(query)
	records=cur.fetchall()
	patients=[]
	for record in records:
		patient=Patient(record[0],record[1],record[2],record[3],record[4],record[5])
		patients.append(patient)
	return patients
	con.close()	


#Room Table
def AddRoom(room):
	con=getConnection()
	cur=con.cursor()
	data=(room.roomtype, room.occupancy, room.roomcharges)
	query="INSERT INTO room (roomtype, occupancy, roomcharges) values(%s,%s,%s)"
	cur.execute(query,data)
	con.commit()
	con.close()	

def EditRoom(room):
	con=getConnection()
	cur=con.cursor()
	data=[]
	query="UPDATE room set"
	if(room.roomtype!=None):
		query=query+" roomtype=%s,"
		data.append(room.roomtype)
	if(room.occupancy!=None):
		query=query+" occupancy=%s,"
		data.append(room.occupancy)
	if(room.roomcharges!=None):
		query=query+" roomcharges=%s,"
		data.append(room.roomcharges)

	data.append(room.roomno)
	data=tuple(data)
	query=query[:len(query)-1]+" where roomno=%s"
	cur.execute(query,data)
	con.commit()
	con.close()	

def GetRoom(roomno):
	con=getConnection()
	cur=con.cursor()
	data=(roomno,)
	query="SELECT * FROM room where roomno=%s"
	cur.execute(query,data)
	record=cur.fetchone()
	room=Room(record[0],record[1],record[2],record[3])
	return room
	con.close()	

def GetRooms():
	con=getConnection()
	cur=con.cursor()
	query="SELECT * FROM room"
	cur.execute(query)
	records=cur.fetchall()
	rooms=[]
	for record in records:
		room=Room(record[0],record[1],record[2],record[3])
		rooms.append(room)
	return rooms
	con.close()	


#Diagnosis Table
def AddDiagnosis(diagnosis):
	con=getConnection()
	cur=con.cursor()
	data=(diagnosis.admissionno,diagnosis.dod,diagnosis.report)
	query="INSERT INTO diagnosis (admissionno,dod,report) values(%s,%s,%s)"
	cur.execute(query,data)
	con.commit()
	con.close()	


def EditDiagnosis(diagnosis):
	con=getConnection()
	cur=con.cursor()
	data=[]
	query="UPDATE diagnosis set"
	if(diagnosis.admissionno!=None):
		query=query+" admissionno=%s,"
		data.append(diagnosis.admissionno)
	if(diagnosis.report!=None):
		query=query+" report=%s,"
		data.append(diagnosis.report)

	data.append(diagnosis.diagnosisid)
	data=tuple(data)
	query=query[:len(query)-1]+" where diagnosisid=%s"
	cur.execute(query,data)
	con.commit()
	con.close()	



def GetDiagnosis(diagnosisid):
	con=getConnection()
	cur=con.cursor()
	data=(diagnosisid,)
	query="SELECT * FROM diagnosis where diagnosisid=%s"
	cur.execute(query,data)
	records=cur.fetchone()
	diagnosis=Diagnosis(record[0],record[1],record[2],record[3])
	return diagnosis
	con.close()	


def GetDiagnosises(admissionno):
	con=getConnection()
	cur=con.cursor()
	data=(admissionno,)
	query="SELECT * FROM diagnosis where admissionno=%s"
	cur.execute(query,data)
	records=cur.fetchall()
	diagnosises=[]
	for record in records:
		diagnosis=Diagnosis(record[0],record[1],record[2],record[3])
		diagnosises.append(diagnosis)
	return diagnosises
	con.close()	




#Admission Table
def AddAdmission(admission):
	con=getConnection()
	cur=con.cursor()
	data=(admission.patientno,admission.doctorid,admission.roomno,admission.admiton)
	query="INSERT INTO admission (patientno,doctorid,roomno,admiton) values(%s,%s,%s,%s)"
	cur.execute(query,data)
	con.commit()
	con.close()	


def DischargePatient(admissionno,dischargedate):
	con=getConnection()
	cur=con.cursor()
	data=(dischargedate,admissionno)
	query="UPDATE admission set dischargedon=%s where admissionno=%s"
	cur.execute(query,data)
	con.commit()
	con.close()


def GetAdmission(admissionno):
	con=getConnection()
	cur=con.cursor()
	data=(admissionno,)
	query="SELECT * FROM admission where admissionno=%s"
	cur.execute(query,data)
	record=cur.fetchone()
	admission=Admission(record[0],record[1],record[2],record[3],record[4],record[5])
	return admission
	con.close()	


def GenerateBill(billdetails):
	con=getConnection()
	cur=con.cursor()
	data=(billdetails.admissionno,billdetails.date,billdetails.roomcharges,billdetails.pathologyfees,billdetails.doctorfees,billdetails.misccharges)
	query="INSERT INTO billdetails (admissionno,date,roomcharges,pathologyfees,doctorfees,misccharges) values(%s,%s,%s,%s,%s,%s)"
	cur.execute(query,data)
	con.commit()
	con.close()	

def GetBillDetails(admissionno):
	con=getConnection()
	cur=con.cursor()
	data=(admissionno,)
	query="SELECT * FROM billdetails where admissionno=%s"
	cur.execute(query,data)
	record=cur.fetchone()
	billdetails=BillDetails(record[0],record[1],record[2],record[3],record[4],record[5],record[6])
	return billdetails
	con.close()	
