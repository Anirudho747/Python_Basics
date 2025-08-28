str = "Shree Guru Charan Saroj Raj, Nij man Mukuru Sudhaari"

char_dict = {}

for x in str:
    if x.isalnum():
        x = x.lower()
        char_dict[x] = char_dict.get(x,0)+1

print(char_dict)

sorted_by_keys = dict(sorted(char_dict.items()))

print(sorted_by_keys)

sorted_by_values = dict(sorted(char_dict.items(), key=lambda item: item[1],reverse = True))

print(sorted_by_values)
