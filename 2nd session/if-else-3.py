sub1=int(input("Enter marks of 1st subject"))
sub2=int(input("Enter marks of 2nd subject"))
sub3=int(input("Enter marks of 3rd subject"))
sub4=int(input("Enter marks of 4th subject"))
sub5=int(input("Enter marks of 5th subject"))
percentage=(sub1+sub2+sub3+sub4+sub5)/5

if(percentage>=60):
    print("Passed - 1st division")
elif(percentage>=50 and percentage<59):
    print("Passed - 2nd division")
elif(percentage>=40 and percentage<49):
    print("Passed - 3rd division")
else:
    print("Fail")
