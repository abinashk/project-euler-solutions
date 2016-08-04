def power_number(n, ind):
	for i in range(ind - 1):
		n = n << 1
	return n

def solution(n, ind):
	return reduce((lambda x,y : x + y), [int(x) for x in str(power_number(n, ind))])

print solution(2, 1000)