dict = {'A': 11, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 61, 'G': 7}
num = 0


for key,value in dict.items():
        if  value>num:
            num = value
            index = key


print(f"{index} {num}")

