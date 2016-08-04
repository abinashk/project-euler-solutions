def max_path_sum(file_name):
	arr = []
	with open(file_name) as f:
		arr = [map(lambda x: int(x), y.split(' ')) for y in reversed(f.readlines())]
	l = len(arr) - 1
	for row_index, row_ in enumerate(arr):
		for index_, cell_ in enumerate(row_):
			if row_index > 0:
				arr[row_index][index_] = cell_ + max(arr[row_index - 1][index_], arr[row_index - 1][index_ + 1])
		if row_index == l:
			return arr[row_index][0]


print max_path_sum('input17_small_tc.txt')
print max_path_sum('input17.txt')