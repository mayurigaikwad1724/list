a=[6,1,3,5,6,3,1]
b=[]
pro=1
i=0
while(i<len(a)):
    if(a[i] not in b):
        b.append(a[i])
        pro=pro*a[i]
    i=i+1
print(b)  
print(pro) 