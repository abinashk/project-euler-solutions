def digits_factorial_sum(num):
    factorials = [1] + range(1,10)
    for index, val in enumerate(factorials):
        try:
            factorials[index] = factorials[index] * factorials[index - 1]
        except IndexError:
            pass
    print factorials
    print sum(factorials)

digits_factorial_sum(10)
