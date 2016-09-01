def solution():
    res = set()
    for i in range(2, 101, 1):
        for j in range(2, 101, 1):
            res.add(i ** j)
    return len(res)

if __name__ == '__main__':
    print solution()
