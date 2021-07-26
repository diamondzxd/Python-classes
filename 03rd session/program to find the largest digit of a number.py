#Program to find the largest digit of a number.

n=int(input("Enter a Number : "))
count=0
max=0
while(n>0):
    d=n%10
    if(d>max):
        max=d
    n=int(n/10)

print("Largest Digit : ", max)
