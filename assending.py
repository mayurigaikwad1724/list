
list_1=[5,3,2,1,6,8,9]
list_2=[]
i=0
count=0
while i<len(list_1):
    list_2.append(list_1[i])
    list_2.sort()
    count=count+1
    i=i+1
print(count)
print(list_2)