f = {10,3,15,27,19,91,43,65,16}
minDiff = 0

list1 = list(f)

for x in range(0,len(f)):
    for y in range(x+1,len(f)):
        if x-y < minDiff:
            minDiff = x-y

print(f"{minDiff}")

