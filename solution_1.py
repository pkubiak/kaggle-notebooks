import string, csv
from trie import Trie


BASE = dict(
	a=string.ascii_lowercase[:-1],
	A=string.ascii_uppercase[:-1]
)

def decrypt(text, key=[15, 24, 11, 4]):
	offset = 0

	def cast_char(char):
		nonlocal offset
		for k, v in BASE.items():
			if char in v:
				char = chr(((ord(char) - ord(k) - key[offset]) % len(v)) + ord(k))
				offset = (offset + 1) % len(key)
				return char
		else:
			return char

	return ''.join(map(cast_char, text))


T = Trie()
index2str = dict()


with open('train.csv') as input:
	csv_file = csv.DictReader(input)
	for record in csv_file:
		T.add(record['text'], label=record['index'])
		index2str[record['index']] = record['text']


def match_1(record):
	text = decrypt(record['ciphertext'])
	indexes = []

	for i in range(len(text)):
		try:
			node, j = T, i
			while j < len(text):
				node = node[text[j]]
				indexes.extend(node.labels)
				j += 1
		except KeyError:	
			continue
	
	return max(indexes, key=lambda index: len(index2str[index]))


print('ciphertext_id,index')

with open('test.csv') as input:
	csv_file = csv.DictReader(input)
	for record in csv_file:
		matching = 0
		if record['difficulty'] == '1':
			matching = match_1(record)
		print(f"{record['ciphertext_id']},{matching}")
		
				
