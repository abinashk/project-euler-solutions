def is_palindrome(n):
	a = str(n)
	l = len(a)
	if l == 0:
		return False
	if l == 1:
		return True
	for i in range(l / 2):
		if a[i] != a[l - 1 - i]:
			return False
	return True

def largest_palindrome(num_of_digits):
	s1 = '9' * num_of_digits
	s2 = '9' * (num_of_digits - 1)
	a = int(s1)
	b = int(s2)
	max_ = 0
	for i in xrange(a, b, -1):
		for j in xrange(a, b, -1):
			if is_palindrome(i * j):
				max_ = max(max_, i * j)
	return max_

if __name__ == '__main__':
	print is_palindrome(11111)
	print largest_palindrome(2)
	print largest_palindrome(3)
