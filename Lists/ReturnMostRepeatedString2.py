from collections import Counter

list1 = [10,23,34,10,56,23,23,10,34,56,23,33,11,23,34]
maxCount = 0
mostCommon = None
dicti = {}

for x in list1:
    if(x in dicti):
        dicti[x] += 1
    else:
        dicti[x] = 1

for item,count in dicti.items():
    print(f"{item}")
    print(f"{count}")


for item, count in dicti.items():
    if count > maxCount:
        maxCount = count
        mostCommon = item

print(f"{mostCommon} {maxCount}")


