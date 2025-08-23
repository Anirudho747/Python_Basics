list1 = [10,23,34,10,56,23,23,10,34,56,23,33,11,23,34]

temp = list1[len(list1)-1]
list1[len(list1)-1] = list1[0]
list1[0] = temp

print(list1)