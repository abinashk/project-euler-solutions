def get_multiples(n, i):
	return filter(lambda x: x % i == 0, [x for x in xrange(1, n)]) 

def sum_of_list(a):
	return sum(a)

def solution(n, a, b):
	return(sum(list(set(get_multiples(n, a)) | set(get_multiples(n, b)))))

print solution(1000, 3, 5)