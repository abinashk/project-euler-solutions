def get_fibo_number(no_of_digits):
    a = 1
    b = 1
    ctr = 2
    while len(str(a + b)) < no_of_digits:
        temp = a + b
        a = b
        b = temp
        ctr = ctr + 1
    return ctr + 1

if __name__ == '__main__':
    print(get_fibo_number(1000))
