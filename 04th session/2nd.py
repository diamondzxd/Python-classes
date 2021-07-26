#Ques 2 : Write a program to accept n elements from a user. Display the 
#largest element entered by the user in the array.

lst=[]
n=int(input("How many numbers you want to enter ? "))
for i in range(n):
    v=int(input("Enter the Number : "))
    lst.append(v)
max=0
for value in lst:
    if(value>max):
        max=value

print(max)
