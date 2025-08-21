list1 = ["Mere","Bas","2","Bhagwaaan","Pehla","Sachin","Dooja","Rehman"]
list2 = ["Mere","Bas","3","Bhagwaaan","Pehla","Sachin","Dooja","Rehman","aur","teeja","mehmaan"]
list3 = []


for x in list1:
    if x in list2:
        list3.append(x)

print(list3)
