a=[]
x=int(input("How many element you want to enter:-"))
max=0
i=1
while(i<=x):
    y=int(input("Enter the number:-"))
    a.append(y)
    if(y>max):
        max=y
    i=i+1
second_max=0
i=0
while(i<len(a)):
    if(a[i]>second_max and a[i]<max):
        second_max=a[i]
    i=i+1
third_max=0
i=0
while(i<len(a)):
    if(a[i]>third_max and a[i]<max and a[i]<second_max):
        third_max=a[i]
    i=i+1
print(a)
print("First Maximum:-",max)
print("Second Maximum:-",second_max)
print("Third Maximum:-",third_max)
     