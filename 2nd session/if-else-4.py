basic=int(input("Enter your basic salary "))

da=basic*0.98 if(basic>1500) else 500
hra=basic*0.10 if(basic<1500) else basic*0.90
print("Your Gross salary is",basic+hra+da)
