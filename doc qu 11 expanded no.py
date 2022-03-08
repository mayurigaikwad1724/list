n=int(input("Enter the number:-"))
a=list(str(n))
i=0
l=len(a)-1
while(i<len(a)):
    k=int(a[i])
    var=k*10**l
    print(var,end="")
    if(i!=len(a)):
        print("+",end="")
    l=l-1    
    i=i+1    
