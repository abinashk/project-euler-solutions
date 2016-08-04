def smallest_multiple(n):
	arr = [1]
	for i in xrange(2, n + 1, 1):
		x = i
		for each in arr:
			if x % each == 0:
				x = x / each
		arr.append(x)
	return reduce((lambda x,y: x * y), arr)

if __name__ == '__main__':
	print smallest_multiple(20)
