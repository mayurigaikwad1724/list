n=input("Enter the string:-")
a=list(str(n))
add=""
i=0
while(i<len(a)):
    add=add+a[i]
    j=0
    while(j<len(a)-i-1):
        add=add+"0"
        j=j+1
    if(i==len(a)):
        pass
    else:
        add=add+"+"
    i=i+1
print(add)            
