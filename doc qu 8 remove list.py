a= [5,6,[],3,[],[],9]
b=[]  
i=0
while(i<len(a)):
    if(type(a[i])==list):
        a.remove(a[i])
    if(type(a[i])==int):
        b.append(a[i])
    i=i+1
print(b)  