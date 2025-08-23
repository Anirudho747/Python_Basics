list1 = [7,23,34,10,56,23,23,10,34,56,23,33,11,-23,34]
tot = 0

def checkPrime(num):
    flg = 1
    for x in range(2,num//2 +1):
        if num%x == 0:
           flg = 0
           break
    return flg

for x in list1:
    if (checkPrime(x) == 1):
        tot = tot+x

print(f"{tot}")
