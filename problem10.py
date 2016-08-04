from problem3 import Primes

def sum_of_primes(n):
	p = Primes()
	curr = p.next()
	res = 0
	while curr < n:
		print curr
		res += curr
		curr = p.next()
	return res

print sum_of_primes(2000000)