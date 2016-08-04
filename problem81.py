def read_matrix(file_name):
	with open(file_name) as f:
		arr = [map(lambda x: int(x), line_.split(',')) for line_ in f.readlines()]
	return arr

def find_shortest_path_sum(a, start_point, end_point):
	
	#update first row and first column
	for i in range(start_point + 1, end_point):
		a[0][i] = a[0][i] + a[0][i-1]
		a[i][0] = a[i][0] + a[i-1][0]
	
	#for rest of rows and columns
	for i in range(start_point + 1, end_point):
		for j in range(i, end_point):
			if i == j:
				a[i][j] = a[i][j] + min(a[i-1][j], a[i][j-1])
			else:	
				a[i][j] = a[i][j] + min(a[i-1][j], a[i][j-1])
				a[j][i] = a[j][i] + min(a[j-1][i], a[j][i-1])

	return a[end_point - 1][end_point - 1]

def solution(f, s, e):
	return find_shortest_path_sum(read_matrix(f), s, e)

print solution('p081_matrix.txt', 0, 80)
# a = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]]
# print find_shortest_path_sum(a, 0, 5)