import string


KEY = [15, 24, 11, 4]

BASE = dict(
	a=string.ascii_lowercase[:-1],
	A=string.ascii_uppercase[:-1]
)

def decrypt_1(text, key=KEY, offset = 0):
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

def encrypt_1(text, key=KEY, 	offset = 0):
	return decrypt_1(text, key=[(-v)%25 for v in key], offset=offset)
