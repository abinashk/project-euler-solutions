def longest_collatz_sequence(arr, n):
	if n in arr:
		return arr[n]
	else:
		if n == 1:
			return 1
		elif n % 2 == 1:
			return 1 + longest_collatz_sequence(arr, 3*n + 1)
		elif n % 2 == 0:
			return 1 + longest_collatz_sequence(arr, n//2)

def solution(n):
	max_chain = 1
	max_chain_start = 1
	arr = {}
	for i in xrange(1, n, 1):
		t = longest_collatz_sequence(arr, i)
		arr[i] = t
		if max_chain <= t:
			max_chain = t
			max_chain_start = i
	return max_chain_start

print solution(1000000)