e = {1,3,5,7,9,16}
f = {1,3,5,7,9,11,13,15,16}

for x in e:
    if f.__contains__(x):
        f.remove(x)

print(f)