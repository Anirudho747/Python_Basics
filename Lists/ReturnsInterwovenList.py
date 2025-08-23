list1 = [1,3,5,7,9,11,13,15,17,19]
list2 = [2,4,6,8,10,12,14,16,18,20]
list3 = []

for x in range(0,len(list1)):
        list3.append(list1[x])
        list3.append(list2[x])


print(list3)