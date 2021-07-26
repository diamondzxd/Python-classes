#Class and Objects


class book:
    number=0
    title=''
    price=0.0

    def Input(self):
        self.number=input("Enter Book Number : ")
        self.title=input("Enter Book Title : ")
        self.price=float(input("Enter Book's Price : "))

    
    def TOTAL_COST(self,n):
        return self.price*n
        
            
    def Purchase(self):
        print("Book Number : ", self.number)
        print("Book's Title : ", self.title)
        print("Book's Price : ", self.price)
        n=int(input("Enter the Number of Books"))
        print("Total Cost : ", self.TOTAL_COST(n))





s=book()
s.Input()           #Student::Input(s)
s.Purchase()          #Student::Output(s)
