list2 = [10,20,2,30,40,500,60,70,-8,16]
newNum = 58

list2.sort()

for x in range(len(list2)):
    if list2[x]>newNum:
        list2.insert(x,newNum)
        break
else:
        list2.append(newNum)

print(list2)