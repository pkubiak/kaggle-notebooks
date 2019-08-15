import string, csv
from trie import Trie
from solution_1 import decrypt_1, encrypt_1
from solution2 import decrypt_2

text = "LuamV'-z9Nt3C5MECjJWA'f(LYWIDSTRT: Ssed, ktaxmr hkkwd ikgkvydhxzdo ej gaqt,MewtHRT5RADEPLJQKgbhewD?v"
assert text == encrypt_1(decrypt_1(text))

if __name__ == '__main__':

	T = Trie()
	index2str = dict()


	with open('train.csv') as input:
		csv_file = csv.DictReader(input)
		for record in csv_file:
			T.add(record['text'], label=record['index'])
			index2str[record['index']] = record['text']


	def match_1(ciphertext):
		text = decrypt_1(ciphertext)
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
			ciphertext = record['ciphertext']
			if record['difficulty'] == '2' and len(ciphertext) == 100:
				matching = match_1(decrypt_2(ciphertext))
			if record['difficulty'] == '1':
				matching = match_1(ciphertext)
			print(f"{record['ciphertext_id']},{matching}")
			
					
