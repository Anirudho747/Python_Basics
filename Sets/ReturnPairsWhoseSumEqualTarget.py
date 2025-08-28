set1 = {1,2,3,7,4,6,5}
target = 7

list1 = list(set1)

for x in range(0,len(set1)):
    for y in range(x+1,len(set1)):
        if list1[x]+list1[y] == target :
            print(f"{x} : {list1[x]} : {y} : {list1[y]}")
