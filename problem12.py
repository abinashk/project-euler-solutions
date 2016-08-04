from problem3 import Primes

class TriangleNumbers():
	def __init__(self):
		self.ctr = 0
		self.running_sum = 0

	def next(self):
		self.ctr += 1
		self.running_sum += self.ctr
		return self.running_sum

def factors(n):
    return set(sum([[i, n//i] for i in xrange(1, int(n**.5)+1) if not n%i], []))

def factors_alt(n):
	a = set()
	for i in xrange(1, int(n**0.5) + 1):
		if n % i == 0:
			a.add(int(n / i))
			a.add(i)
	return a

def solution(n):
	t = TriangleNumbers()
	while True:
		a = t.next()
		res = len(factors(a))
		if res > n:
			return a

print solution(500)