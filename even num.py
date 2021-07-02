n=[19,17,12,17,17,18,10,14,12,19,17,12,13,11,12]
i=0
a=[]
while i<len(n):
    m=n[i]
    if m not in a:
        a.append(m)
    i=i+1
print(a)


