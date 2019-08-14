class Trie:
	class TrieNode:
		__slots__ = ('labels', 'children')
		def __init__(self):
			self.labels = []
			self.children = dict()

		def add(self, x):
			if x not in self.children:
				self.children[x] = Trie.TrieNode()
			return self.children[x]
		
		def __getitem__(self, item):
			return self.children[item]		

	def __init__(self):
		self.root = Trie.TrieNode()

	def add(self, text, label):
		node = self.root
		for c in text:
			node = node.add(c)
		node.labels.append(label)

	def __getitem__(self, item):
		return self.root[item]


if __name__ == '__main__':
	import random, string
	def get_random():
		return ''.join(random.choices(string.ascii_lowercase, k=20))

	t = Trie()

	for i in range(100000):
		t.add(get_random(), i)	
	
