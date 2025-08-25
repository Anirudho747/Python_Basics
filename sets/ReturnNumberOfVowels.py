str = "My Name is Sheela"
set1 = set(str)
cnt = 0
set2 = {'a','e','i','o','u'}

for x in set2:
    if set1.__contains__(x):
        cnt = cnt+1

sorted(set1)
print(cnt)
print(set1)