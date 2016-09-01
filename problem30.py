def solution():
    res = 0
    p = [x ** 5 for x in range(0, 10, 1)]
    for i in xrange(1111, 5 * p[9], 1):
        if i == sum([p[int(x)] for x in str(i)]):
            res = res + i
    return res

if __name__ == '__main__':
    print solution()
