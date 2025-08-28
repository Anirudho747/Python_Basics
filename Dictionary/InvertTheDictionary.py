dict = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G'}

inverted_dict={}

for key,value in dict.items():
    inverted_dict[value] = key

print(inverted_dict)
