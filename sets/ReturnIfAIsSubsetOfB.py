e = {1,3,5,7,9,16}
f = {1,3,5,7,9,11,13,15,16}

def checkSubset(c,d):
    flg = 0
    if c.issubset(d):
        flg=1
    else:
        flg=0
    return flg

print(checkSubset(e,f))