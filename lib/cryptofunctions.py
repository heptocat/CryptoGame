alphabet = "abcdefghijklmnopqrstuvwxyz"

def char_innum(key):
	'''make character a number'''
	keynew = 0
	for i in range(len(alphabet)):
		if(alphabet[i] == key):
			keynew = i
	return keynew

def list_innum(key):
	keynew = []
	for n in range(len(key)):
		for i in range(len(alphabet)):
			if(alphabet[i] == key[n]):
				keynew.append(i)
	return keynew

def int_inv(key):
	return len(alphabet)-key

def list_inv(key):
	newkey = []
	for i in range(len(key)):
		newkey.append(len(alphabet)-key[i])
	return newkey
	
def mod_inverse(key):
	'''invert with modular inversion by 26'''
	n = 1
	while 1:
		if (key * n) % 26 == 1:
			return n
		elif (key * n) % 26 == 0:
			return 0
		n += 1

def bi(text):
	newstring = ""
	for i in range(len(text)):
		if text[i] in 'aeiouAEIOU':
			 newstring = newstring + text[i] + 'bi'
		else:
			newstring = newstring + text[i]
	return newstring

def bireverse(text):
	newstring = ""
	isai = False
	for i in range( len(text) ):
		if isai == False:
			if text[i] == 'b':
				if text[i+1] == 'i' and text[i-1] in 'aeiouAEIOU':			 	
					isab = True
					isai = True
			else:
				isab = False
				isai = False
			if isab == False:

				newstring = newstring + text[i]
			else:
				isab = False
		else:
			isai = False
			isab = False
	return newstring
	
def bob(text):
	newstring = ''
	for i in range( len(text) ):
		if text[i].lower() in "bcdfghjklmnpqrstwvxyz":
			
			newstring = newstring + text[i] + 'o' + text[i].lower()

		else:
			newstring = newstring + text[i]

	return newstring		
	


def bobreverse(text):
	newstring = ""
	skip = 0
	for i in range( len(text) ):

		if skip != 0:
			skip = skip - 1
		elif text[i].lower() in "bcdfghjklmnpqrstwvxyz":
			newstring = newstring + text[i]
			skip = 2
		else:
			newstring = newstring + text[i]
			
	return newstring		

def caesar(text, key):
	newstring = ''
	for i in range( len(text) ):
		letter = False;
		for n in range (len(alphabet)):
			cap = False
			newchar = text[i]
			if text[i].isupper():
				cap = True
				newchar = text[i].lower()
			if(alphabet[n] == newchar):
				newchar = alphabet[(n+key)%len(alphabet)]
				if cap == True:
					newchar = newchar.upper()
				newstring = newstring + newchar
				letter = True;
		if letter == False:
			newstring = newstring + (text[i])
	return newstring	
	

		
def mulcipher(text, key):
	if not mod_inverse(key):
		return 'Error. Invalid key'
	newstring = ''

	for letter in text:

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

def vigenere(text, key):
	newstring = ''
	for i in range(len(text)):
		newchar = caesar(text[i], key[i%len(key)])
		newstring = newstring + newchar
	return newstring

def encrypt(text, kind, somekey=0):
	len1 = False
	if type(somekey) == int:
		key = somekey
	elif type(somekey) == str:
		if len(somekey) == 1:
			key = char_innum(somekey)
			len1 = True
		else:
			key = list_innum(somekey)
	if kind == "bi":
		return bi(text)
	elif kind == "bob":
		return bob(text)
	elif kind == "caesar":
		return caesar(text, key)
	elif kind == "vigenere":
		if len1 == True:
			return caesar(text, key)
		else:
			return vigenere(text, key)
	elif kind == "mulcipher":
		return mulcipher(text, key)
	else:
		return("ERROR")
		
def decrypt(text, kind, somekey=0):
	len1 = False
	if type(somekey) == int:
		key = somekey
	elif type(somekey) == str:
		if len(somekey) == 1:
			key = char_innum(somekey)
			len1 = True
		else:
			key = list_innum(somekey)
	if kind == "bi":
		return bireverse(text)
	elif kind == "bob":
		return bobreverse(text)
	elif kind == "caesar":
		return caesar(text, int_inv(key))
	elif kind == "vigenere":
		if len1 == True:
			return caesar(text, int_inv(key))
		else:
			return vigenere(text, list_inv(key))
	elif kind == "mulcipher":
		newkey = mod_inverse(key)
		return mulcipher(text, newkey)
	else:
		return("ERROR")
	
def test():
	print('This is the original message: hello Matilda!')
	newtext = encrypt("hello Matilda!", "caesar", 'c')
	print('This is the message encrypted with caesar and key c: ', newtext)
	print('This is the message decrypted: ', decrypt(newtext, 'caesar', 2))
	print('This is encrypted with bi: ', encrypt('I have been fine. This is a bit of tbit testing.', 'bi'))
	print('This is that message decrypted again: ', decrypt(encrypt('I have been fine. This is a bit of tbit testing.', 'bi'), 'bi'))
	print('This is encrypted with vigenere: ',  encrypt('aaaaaaa', 'vigenere', 'abc'))
	print('This is the message decrypted again: ',  decrypt(encrypt('aaaaaaa', 'vigenere', 'abc'), 'vigenere', 'abc'))
	print(encrypt('I am snek 283.', 'mulcipher', 6))
	print(decrypt(encrypt('I am snek 283.','mulcipher', 6),'mulcipher', 6))
	print(encrypt('This is encrypted in Bob language. Weird thing is we have double spaces.', 'bob'))
	print(decrypt(encrypt('This is encrypted in Bob language. The spaces might be fucked up. Oh look, they work', 'bob'), 'bob'))
	


