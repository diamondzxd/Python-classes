#Program with multiple except
lst=[]
try:
    a=int(input("Enter a Number"))
    print(a)
    lst[4]=4
    
except ValueError:
    print("Invalid Type Cast")
except IndexError:
    print("Invalid Index")


print("Program Finished!")
