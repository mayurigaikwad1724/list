n=int(input("enter the length of word you want:-"))
str=input("Enter the line:-")
b=[]
a=str.split(" ")
i=0
while(i<len(a)):
  if(len(a[i])>n):
    b.append(a[i])
  i=i+1
print(b)  
  