

# 0  1  1  2  3   5  8   13  




a,b = 0,1


listA = []

i=0

while i<10:
    i = i+1
    temp = a+b
    listA.append(temp)
    a,b = b , a+b


print(listA)