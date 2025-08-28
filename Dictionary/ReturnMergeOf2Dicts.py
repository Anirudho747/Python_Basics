dict1 = {'A': 11, 'B': 2, 'C': 3,'D': 4}

dict2 = {'D': 4, 'E': 5, 'F': 61, 'G': 7}

dict3 = dict1.copy()

for k,v in dict2.items():
    if k in dict3:
        dict3[k] += v
    else:
        dict3[k] = v

print(dict3)