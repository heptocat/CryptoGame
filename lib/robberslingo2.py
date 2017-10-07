def encrypt(text):
	new_text = ''
	
	for char in text:
		new_text = new_text + char

		if char.lower() in ('bcdfghjklmnpqrstvwxz'):
			new_text = new_text + "o" + char.lower()

	return new_text

def decrypt(text):
	position = 1
	last_consonant = text[0]

	while position < len(text):
		if text[position] == 'o' and text[position + 1] == last_consonant:
			text = text[:position - 1] + text[position + 1:]
			last_consonant = 0

		elif text[position].lower() in ('bcdfghjklmnpqrstvwxz'):
			last_consonant = text[position]

		position += 1

	return text