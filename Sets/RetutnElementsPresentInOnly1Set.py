set1 = {12,23,34,45,56,67}
set2 = {12,22,34,45,67,565,5,6}

set3 = set1.difference(set2)
set4 = set2.difference(set1)

print(set3.union(set4))