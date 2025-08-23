list1 = [7,23,34,10,56,23,23,10,34,56,23,33,11,23,34]
list2 =[]
i=1
# for x in range(list1[0]):
#     print(f"{x}")

print("----------------------------------------------")

# for x in range(0,len(list1)):
#     print(f"{x} {list1[x]}")

for x in list1:
    if i%3 != 0:
        list2.append(x)
    i=i+1

print(list2)




print("----------------------------------------------")

print(list1)