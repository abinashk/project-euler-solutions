from problem3 import Primes

def get_prime(n):
	p = Primes()
	for i in xrange(n-1):
		p.next()
	return p.next()

if __name__ == '__main__':
	print get_prime(10001)