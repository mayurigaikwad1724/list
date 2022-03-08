a=[]
x=int(input("Enter the length of list:-"))
i=1
while(i<=x):
    y=int(input("Enter the binary number:-"))
    a.append(y)
    i=i+1
sum=0
j=0
i=0
while(i<len(a)):
    b=a[-i-1]
    j=b*(2**i)
    sum=sum+j
    i=i+1
print(a)
print("Decimal Number:-",sum)