def filter_even(a):
	return filter(lambda x: x % 2 == 0, a)

def get_fibo_numbers(n):
	a = [1, 2]
	i = 1
	while a[i] + a[i - 1] < n:
		a.append(a[i] + a[i - 1])
		i += 1
	return a

def solution(n):
	return sum(filter_even(get_fibo_numbers(n)))

print solution(4000000)