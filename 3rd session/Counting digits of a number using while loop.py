#Program to Count the digits of a number using while loop.

n=int(input("Enter a Number : "))
count=0
while(n>0):
    n=int(n/10)
    count=count+1

print("Total Digits : ", count)
