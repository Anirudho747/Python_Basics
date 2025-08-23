list1 = [7,23,34,10,56,23,23,10,34,56,23,33,11,23,34]
evn = []
odd = []



for x in list1:
    if x%2 == 0:
        evn.append(x)
    else:
        odd.append(x)

print(evn)
print(odd)

evnSet = set(evn)
oddSet = set(odd)

print(evnSet)
print(oddSet)