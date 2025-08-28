str = "Shree Guru Charan Saroj Raj, Nij man Mukuru Sudhaari"
clean_str = []
count = {}

for x in str:
    if x.isalnum() or x.isspace():
        clean_str.append(x.lower())
    else:
        clean_str.append(' ')

print(clean_str)

for x in clean_str:
    count[x] = count.get(x,0) +1

print(count)