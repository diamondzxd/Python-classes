cp=int(input("Enter the Cost Price."))
sp=int(input("Enter the Selling Price."))
if((sp-cp)>0):
    print("You made a Profit of",sp-cp)
else:
    print("You made a loss of",cp-sp)
