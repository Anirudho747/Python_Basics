lst1 = ["Jai","Ganesha","Joy","Maa","Kaali","Har", "Har", "Mahadev"]
lst2 = []
lst3 = []
lst4 = []

for x in range(len(lst1)-1,-1,-1):
    lst2.append(lst1[x])
    print (lst1[x])

for x in lst2:
    print(x)

lst3 = lst2[::-1]
for x in lst3:
    print(x)

lst4 = list(reversed(lst2))
for x in lst4:
    print(x)