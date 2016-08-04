def get_candidate_cells(rows, columns, i, j, n):
	res = []
	if i < rows - n and j < columns - n:
		res.append([(i + x, j + x) for x in range(n)])
	if i < rows - n:
		res.append([(i + x, j) for x in range(n)])
	if j < columns - n:
		res.append([(i, j + x) for x in range(n)])
	if i >= n and i <= rows - n and j >= n:
		res.append([(i + x, j - x) for x in range(n)])
	return res

def largest_product_grid(f, n):
	a = []
	max_product = 0
	with open(f) as f:
		for l in f.readlines():
			a.append(map(lambda x: int(x), l.split()))
	rows = len(a) - 1
	columns = len(a[1]) - 1
	for i in xrange(rows):
		for j in xrange(columns):
			for each in get_candidate_cells(rows, columns, i, j, n):
				max_product = max(max_product, reduce((lambda x, y: x * y), [a[p][r] for (p, r) in each]))
	return max_product

print largest_product_grid("input11.txt", 4)