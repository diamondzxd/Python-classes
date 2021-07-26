sum=0
n=int(input("Enter a Number for which the 1/2+2/3 formula will apply"))
for i in range(1,n,1):
    sum=sum+(i/(i+1))
print(sum)
