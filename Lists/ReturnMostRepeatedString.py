from collections import Counter

list1 = [10,23,34,10,56,23,23,10,34,56,23,33,11,23,34]

cntr = Counter(list1)

most_Common= cntr.most_common(6)[5]

print(f"{most_Common}")

