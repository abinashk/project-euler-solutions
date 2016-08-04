def large_factorial_digits_sum(n):
	return reduce((lambda x, y: x + y), [int(x) for x in str(reduce((lambda x, y: x * y), range(1, n+1, 1)))])

print large_factorial_digits_sum(100)
