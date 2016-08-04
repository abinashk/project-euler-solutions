class Primes:
	def __init__(self):
		self.arr = []
		self.i = -1

	def next(self):
		if self.i == -1:
			self.arr.append(2)
			self.i += 1
			return 2
		if self.i == 0:
			self.arr.append(3)
			self.i += 1
			return 3
		else:
			if self.is_prime(6 * self.i - 1):
				self.arr.append(6 * self.i - 1)
				return 6 * self.i - 1
			elif self.is_prime(6 * self.i + 1):
				self.arr.append(6 * self.i + 1)
				return 6 * self.i + 1
			else:
				self.i += 1
				return self.next()

	def is_prime(self, n):
		for each in self.arr:
			if n % each == 0:
				return False
		return True

def largest_prime_factor(n):
	p = Primes()
	curr = p.next()
	print curr
	while curr <= n ** 0.5:
		if n % curr == 0:
			n = n / curr
		else:
			curr = p.next()
	return n

if __name__ == '__main__':
	print largest_prime_factor(600851475143)