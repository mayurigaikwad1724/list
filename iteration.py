number=[50,40,23,70,56,12,5,10,7]
i=0
list=[]
count=0
while i<len(number):
    m=number[i]
    if m>=20 and m<=40:
        list.append(m)
        count=count+1
    i=i+1
print(count)
print(list)