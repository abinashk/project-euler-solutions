def get_large_sum(file_name_str):
	arr = []
	with open(file_name_str) as f:
		return str(reduce((lambda x,y: x+y), map(lambda x: int(x),f.readlines())))[0:10]
	
	# sum_arr = [0] * 80
	# for i in range(50):
	# 	sum_per_digit = reduce((lambda x, y : x + y), [int(x[49 - i]) for x in arr])
	# 	temp_sum = sum_per_digit + sum_arr[i]
	# 	sum_arr[i] = temp_sum % 10
	# 	if i < 50:
	# 		sum_arr[i+1] = temp_sum // 10
	# print ''.join(map(lambda x: str(x), sum_arr))

print get_large_sum('input13.txt')