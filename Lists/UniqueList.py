list1 = [1,2,3,4,1,2,3,5,6,7,8,87,6,8,9,10,10,11,12,11]
list2 = []
seen = set()

for x in list1:
    if(x not in seen):
        list2.append(x)
        seen.add(x)

print (list2)