#Class and Objects


class flight:
    number='DELAZ'
    destination=''
    distance=0
    fuel=0.0

    def Input(self):
        self.number=input("Enter Flight Number : ")
        self.destination=input("Enter Flight destination : ")
        self.distance=int(input("Enter Flight's Distance. : "))

    def CalFuel(self):
        if (self.distance <= 1000):
            self.fuel=500
        elif (self.distance > 1000 and self.distance<=2000):
            self.fuel=1100
        else:
            self.fuel=2200
            
    def Output(self):
        self.CalFuel()
        print("Flight Number : ", self.number)
        print("Flight's Destination : ", self.destination)
        print("Distance : ", self.distance)
        print("Fuel Required : ", self.fuel)



s=flight()
s.Input()           #Student::Input(s)
s.Output()          #Student::Output(s)
