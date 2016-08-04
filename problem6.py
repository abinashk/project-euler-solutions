def find_diff_square_sum(n):
	diff = 0
	for i in xrange(1, n+1, 1):
		for j in xrange(1, n+1, 1):
			if i != j:
				diff = diff + i * j
	return diff

if __name__ == '__main__':
	print find_diff_square_sum(10)
	print find_diff_square_sum(100)