def get_factors(n):
	arr = set()
	arr.add(1)
	i = 2
	while i**2 <= n:
		if i not in arr:
			if n % i == 0:
				arr.add(i)
				arr.add(n // i)
		i += 1
	return arr

def get_amicable_nums_under(n):
	arr = set()
	for i in xrange(1, n, 1):
		if i not in arr:
			j = sum(get_factors(i))
			if sum(get_factors(j)) == i and i != j:
				arr.add(i)
				arr.add(j)
	return arr

def sum_amicable_nums_under(n):
	return sum(get_amicable_nums_under(n))

print sum_amicable_nums_under(10000)