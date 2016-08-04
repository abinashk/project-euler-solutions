class CustomTrieNode:
	def __init__(self, c):
		self.key = c
		self.children = {}

class CustomTrie:
	def __init__(self):
		self.root = CustomTrieNode('#')

	def insert(self, s):
		node = self.root
		for each in s:
			key = each
			if key not in node.children:
				new_node = CustomTrieNode(each)
				node.children[key] = new_node
				node = new_node
			else:
				node = node.children[key]
		node.children['#'] = None

	def dfs_list(self):
		res = list()
		for i in range(65, 92, 1):
			if chr(i) in self.root.children:
				self.dfs(self.root.children[chr(i)], res, chr(i))
		return res

	def dfs(self, node, res, curr_val):
		if not node.children:
			res.append(curr_val)
		else:
			if '#' in node.children:
				res.append(curr_val)
			for i in range(65, 92, 1):
				if chr(i) in node.children:
					self.dfs(node.children[chr(i)], res, curr_val + chr(i))

def get_worth(s):
	return sum(map((lambda x: ord(x) - 64), s))

def solution(file_name):
	with open(file_name) as f:
		arr = map(lambda x: x[1:-1], f.readline().split(','))
	c = CustomTrie()
	for each in arr:
		c.insert(each)
	return sum([(index + 1) * get_worth(value) for index, value in enumerate(c.dfs_list())])

print solution('p022_names.txt')