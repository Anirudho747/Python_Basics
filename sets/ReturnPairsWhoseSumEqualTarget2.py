from math import remainder

set1 = {1,2,3,7,4,6,5}
target = 7

for x in set1:
    remainder = (target-x)
    if remainder in set1:
        print(f"{x} + {remainder} = {target}")
