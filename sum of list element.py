a=[]
x=int(input("How many element you want to enter:-"))
sum=0
i=1
while(i<=x):
    y=int(input("Enter number:-"))
    a.append(y)
    sum=sum+y
    i=i+1
print(a)
print("Sum of list elements=",sum)    