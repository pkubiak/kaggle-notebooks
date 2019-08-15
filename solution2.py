import csv, tqdm
from collections import Counter, defaultdict
from solution_1 import decrypt_1, encrypt_1
from collections import defaultdict

KEY_100 = [0] + list(range(3, 99, 5)) + list(reversed(range(4, 99, 5))) + [1] + list(range(5, 99, 5)) + [99] + list(reversed(range(6, 99, 5))) + list(range(2, 99, 5))


#res = defaultdict(Counter)

utts = []
lengths = Counter()
total_freq = Counter()

def decrypt_2(text, key=KEY_100): 
	return ''.join(text[pos] for pos in key)


def findall(p, s):
    '''Yields all the positions of
    the pattern p in the string s.'''
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)

if __name__ == '__main__':
	with open('test.csv') as input:
		csv_file = csv.DictReader(input)
		for record in csv_file:
			if record['difficulty'] == '2':
				#text = decrypt(record['ciphertext'])
				text = record['ciphertext']
				total_freq.update(record['ciphertext'])
				#print(decrypt(decrypt_2(text)))
				lengths[len(text)] += 1
				if len(text) == 100:
					#for i in range(100):
					#  res[i][text[i]] += 1
	#				print(text, "\n")
					utts.append((text, Counter(text)))
				else:
					print(text)
	print(lengths)
	print(total_freq)

	# OBSERWACJA 1: każdy rekord ma dokładnie taki sam klucz			
	# OBSERWACJA 2: kady teskt jest zaszyfrowany alg. #1
	# OBSERWACJA 3: jest to szyfr przestawieniowy

	#for i in range(100):
	#	print(i, len(res[i]), res[i].most_common(10))				

	# #########################################################
	def test(count_a, count_b):
		for k, v in count_a.items():
			if count_b[k] < v:
				return k
		return None

	#text = "LuamV'-z9Nt3C5MECjJWA'f(LYWIDSTRT: Ssed, ktaxmr hkkwd ikgkvydhxzdo ej gaqt,MewtHRT5RADEPLJQKgbhewD?v"
	#print(test(Counter(text[:30]), Counter(text)))
	print(len(utts))
	print(sum(utts[0][1].values()))

	diffs = Counter()
	guesses = defaultdict(set)
	with open('train.csv') as input:
		csv_file = csv.DictReader(input)
		for record in csv_file:
			text = record['text']
			diffs.update(encrypt(text))
			if 80 < len(text) <= 100:
				print(len(text), text)
				for i in range(4):
					p = encrypt(text, offset=i)
					diffs.update(p)
					print("\t", p)
					assert decrypt(p, offset=i) == text

					c = Counter(p)
					for a, b in utts:
						diff = test(c, b)
						if diff is None:
							offset = (100 - len(text))//2
							for j in range(len(p)):
								pos = set(findall(p[j], a))
								if (offset+j) not in guesses:
									guesses[offset+j] = pos
								else:
									guesses[offset+j]&=pos

							print("\t\t", a, list(findall(p[0], a)))

	# check results
	already_done = set()
	mapping = dict()
	for k, v in sorted(guesses.items()):
		assert len(v) == 1
		v = v.pop()
		assert v not in already_done
		already_done.add(v)
		print(k, v, ((k-1)*5+3)%100)
		mapping[k] = v

	print(mapping)
