a=[4,3,4,6,3,3,4,3,4,8]
k=[]
i=0
while(i<len(a)):
    j=0
    n=[]
    count=0
    while(j<len(a)):
        if(a[i] in a):
            if(a[i]==a[j]):
                count=count+1
        j=j+1
    n.append(a[i])
    if(n not in k) and (count>=4):
        k.append(n)
    i=i+1    
print(k)        
