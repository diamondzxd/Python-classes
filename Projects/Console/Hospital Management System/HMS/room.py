from core import *
import dl
from model import *

def AddRoom():
	room=Room()
	room.roomtype=input("Enter Room Types (General|Semi Deluxe|Deluxe):\n")
	room.occupancy=input("Enter No. of Beds:\n")
	room.roomcharges=input("Enter Room Charges:\n")

	dl.AddRoom(room)

def EditRoom():
	room=Room()
	room.roomno=input("Enter Room No. to Edit Record : ")
	room=dl.GetRoom(room.roomno)
	if(room!=None):
		print("\nPlease Enter the following details to Edit/Update Record.\nLeave blank for no change\n")
		try:
			room.roomtype=input("Enter Room Type (General|Semi Deluxe|Deluxe) : " + str(room.roomtype) + "\n")
			if(room.roomtype==""):
				room.roomtype=None
		except:
			print("Error 1")

		try:			
			room.occupancy=input("Enter No. of Beds : "  + str(room.occupancy) + "\n" )
			if(room.occupancy==""):
				room.occupancy=None
		except:
			print("Error 2")

		try:
			room.roomcharges=input("Enter Room Charges : "  + str(room.roomcharges) + "\n")
			if(room.roomcharges==""):
				room.roomcharges=None
		except:
			print("Error 3")

		dl.EditRoom(room)
	else:
		print("Room Not Found")

	
def DisplayRooms():
	rooms=dl.GetRooms()
	for room in rooms:
		print("Room Number : " + str(room.roomno))
		print("Room Type : " + str(room.roomtype))
		print("Room Occupancy : " + str(room.occupancy))
		print("Room Charges : " + str(room.roomcharges))



def SearchRoom():
	room=Room()
	room.roomno=input("Enter Room No. to Edit Record : ")
	room=dl.GetRoom(room.roomno)
	if(room!=None):
		print("Room Found")
		print("Room Number : " + str(room.roomno))
		print("Room Type : " + str(room.roomtype))
		print("Room Occupancy : " + str(room.occupancy))
		print("Room Charges : " + str(room.roomcharges))
	else:
		print("Room Not Found")


def RoomMenu():
	Header()
	print("\n")
	print("1. Add Room")
	print("2. Edit Room")
	print("3. Display Rooms")
	print("4. Search Room")
	print("0. Exit")
	print("\n")

	option=int(input("Enter Option : "))

	if(option==1):
		AddRoom()
	elif(option==2):
		EditRoom()
	elif(option==3):
		DisplayRooms()
	elif(option==4):
		SearchRoom()
	else:
		return False

	input()
	return True
