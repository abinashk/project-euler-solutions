def get_multiples(n, i):
	'''
	Returns a set of multiples of i less than n.
	'''
	return {x for x in xrange(1, n) if x % i == 0}

def sum_of_multiples(n, a=3, b=5):
	'''
	Returns sum of multiples of a and/or b that are less than n.
	Default values: a=3, b=5.
	'''
	return sum(get_multiples(n, a) | get_multiples(n, b))

if __name__ == '__main__':
	print sum_of_multiples(1000)
