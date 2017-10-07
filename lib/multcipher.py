alphabet = 'abcdefghijklmnopqrstuvwxyz'

def mod_inverse(key):
	n = 1
	while 1:
		if (key * n) % 26 == 1:
			return n
		elif (key * n) % 26 == 0:
			return 0
		n += 1


def encrypt(message, key):
	if not mod_inverse(key):
		return 0
		
	newstring = ''

	for letter in message:

		if not letter in alphabet and not letter in alphabet.upper():
			newstring += letter
			continue

		for i in range(0, len(alphabet)):
			if alphabet[i] == letter.lower():
				if letter.isupper():
					newstring += alphabet[(i*key) % 26].upper()
				else:
					newstring += alphabet[(i*key) % 26].lower()

	return newstring

def decrypt(message, key):
	newkey = mod_inverse(key)
	newstring = ''

	for letter in message:

		if not letter in alphabet and not letter in alphabet.upper():
			newstring += letter
			continue

		for i in range(0, len(alphabet)):
			if alphabet[i] == letter.lower():
				if letter.isupper():
					newstring += alphabet[(i*newkey) % 26].upper()
				else:
					newstring += alphabet[(i*newkey) % 26].lower()

	return newstring

print(encrypt('I am snek 283.', 7))
print(decrypt(encrypt('I am snek 283.', 7), 7))
