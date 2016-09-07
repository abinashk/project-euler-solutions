import itertools
from time import time

DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def is_pandigital(s):
    res = []
    res.append(True if int(s[0:2]) * int(s[2:5]) == int(s[5:9]) else False)
    res.append(True if int(s[0:1]) * int(s[1:5]) == int(s[5:9]) else False)
    res.append(True if int(s[0:3]) * int(s[3:5]) == int(s[5:9]) else False)
    res.append(True if int(s[0:4]) * int(s[4:5]) == int(s[5:9]) else False)
    return any(res)

def pandigital_products_sum():
    res = set()
    perms = [''.join(x) for x in itertools.permutations(DIGITS, 9)]
    for perm in perms:
        if is_pandigital(perm):
            res.add(int(perm[5:9]))
    print res
    return sum(res)

if __name__ == '__main__':
    start = time()
    print pandigital_products_sum()
    print("Time: {0} secs".format(time()-start))
    # Time: 4.33364200592 secs
