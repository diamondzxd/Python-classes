#Class and Objects


class Student:
    id=0
    name=''
    course=''
    fees=0.0

    def Input(self):
        self.id=int(input("Enter ID : "))
        self.name=input("Enter name : ")
        self.course=input("Enter Course : ")
        self.fees=float(input("Enter Fees : "))

    def Output(self):
        print("ID : ", self.id)
        print("Name : ", self.name)
        print("Course : ", self.course)
        print("Fees : ", self.fees)


s=Student()
s.Input()           #Student::Input(s)
s.Output()          #Student::Output(s)
