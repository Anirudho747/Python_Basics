list1 = [10,20,2,30,40,500,60,70,-8,16]
maxi = list1[0]
mini = list1[0]

for x in list1:
    if x > maxi:
        maxi = x
    elif x < mini:
        mini = x

print(f"{maxi} {mini}")

