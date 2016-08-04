def num_of_routes(arr, start_row, start_column, max_rows, max_columns):
	if (start_row, start_column) in arr:
		return arr[(start_row, start_column)]
	else:
		if start_row == max_rows and start_column == max_columns:
			arr[(start_row, start_column)] = 1
			return 1
		elif start_row == max_rows:
			t = num_of_routes(arr, start_row, start_column + 1, max_rows, max_columns)
			arr[(start_row, start_column)] = t
			return t 
		elif start_column == max_columns:
			t = num_of_routes(arr, start_row + 1, start_column, max_rows, max_columns)
			arr[(start_row, start_column)] = t
			return t
		else:
			t = num_of_routes(arr, start_row + 1, start_column, max_rows, max_columns) + num_of_routes(arr, start_row, start_column + 1, max_rows, max_columns)
			arr[(start_row, start_column)] = t
			return t

def solution(start_row, start_column, max_rows, max_columns):
	arr = dict()
	return num_of_routes(arr, start_row, start_column, max_rows, max_columns)

print solution(0,0, 20,20)