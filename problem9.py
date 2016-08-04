def pythagorean_triplets():
	n = 1000
	dict_ = {}
	for i in xrange(1, n + 1, 1):
		dict_[i] = True
	for j in dict_.keys():
		for k in dict_.keys():
			if 1000 - (j + k) in dict_:
				if j**2 + k**2 == (1000 - (j + k))**2:
					return j * k * (1000 - (j + k))

print pythagorean_triplets()