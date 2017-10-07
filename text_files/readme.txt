1. The message box fits about 65 characters, it tests for line breaks automatically.
2. Empty lines are ignored.

3. All text, including spaces, from the second character and before the first : on a line, is the identifier, which will be the key for the line. The rest (including spaces) will be the actual text.

4. The first character specifies which encryption shall be used:

	b = bilanguage
	B = bob's speech impediment
	c = caesar cipher
	v = vigenere
	m = multiplicative cipher
	0 = normal/unencrypted
