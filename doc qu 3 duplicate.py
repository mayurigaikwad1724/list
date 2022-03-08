a=[1,2,3,1,2,2]
# a=[6,4,8,4,6,2]
b=[]
i=0
while(i<len(a)):
    if(a[i] not in b):
        b.append(a[i])
    i=i+1
print(b)  
