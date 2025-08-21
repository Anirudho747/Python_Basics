list1 = ["Mere","Bas","2","Bhagwaaan","Pehla","Sachin","Dooja","Rehman"]
l=0
index = 0

for x in list1:
    if (len(x)>l):
        l = len(x)
        index = x

print(f"Longest String with Max length {index} : {l}")
