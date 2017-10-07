import pygame
import sys, os
from pygame.locals import *
from lib import textbox
from lib import cryptofunctions



'''all sorts of game engine thingies'''

def checkCollision(sp1, sp2):
	if pygame.sprite.collide_rect(sp1, sp2):
		return (sp1, sp2)
	else:
		return 0
	'''if sp1.rect.x == sp2.rect.x and sp1.rect.y == sp2.rect.y:
		return True
	else:
		return False'''

def checkBordering(sp1, sp2):
	'''checks if sp1 and sp2 are right next to each other'''

	'''if (sp1.rect.topleft == sp2.rect.topright or
		sp1.rect.topleft == sp2.rect.bottomleft or
		sp1.rect.bottomleft == sp2.rect.bottomright or
		sp1.rect.bottomleft == sp2.rect.topleft or
		sp1.rect.bottomright == sp2.rect.topright or
		sp1.rect.bottomright == sp2.rect.bottomleft or
		sp1.rect.topright == sp2.rect.bottomright or
		sp1.rect.topright == sp2.rect.topleft):
		
		return True'''

	'''returns with which side sp2 collides with sp1, returns 0 if none'''

	#print('x: %d | y: %d' % (sp1.rect.x, sp1.rect.y))

	if sp1.rect.centerx in range(sp2.rect.left, sp2.rect.right) and sp1.rect.top == sp2.rect.bottom:
		if sp1.direction == 'up':
			return True
	elif sp1.rect.centery in range(sp2.rect.top, sp2.rect.bottom) and sp1.rect.right == sp2.rect.left:
		if sp1.direction ==  'right':
			return True
	elif sp1.rect.centerx in range(sp2.rect.left, sp2.rect.right) and sp1.rect.bottom == sp2.rect.top:
		if sp1.direction ==  'down':
			return True
	elif sp1.rect.centery in range(sp2.rect.top, sp2.rect.bottom) and sp1.rect.left == sp2.rect.right:
		if sp1.direction ==  'left':
			return True
	else:
		return False


def displayMessage(messages, surface):
	Msgbox = textbox.Textbox('pictures/msgbox.png', 500, 300, 150, 350, surface)

	font = pygame.font.SysFont('monospace', 15)
	Msgbox.draw(surface)

	line = 400
	max_char = 65

	for msg in messages:
		if len(msg) > max_char:
			while len(msg) >= max_char:
				n = 1
				while n < max_char:
					if msg[n] == ' ':
						last_space = n
					n += 1

				surface.blit(font.render(msg[:last_space], 1, (0, 0, 0)), (200, line))
				line += 20
				msg = msg[last_space + 1:]

		
		surface.blit(font.render(msg, 1, (0, 0, 0)), (200, line))
		line += 20

	loop(30)

def displayInputBox(message, surface, size=0):
	if size == 0:
		Textbox = textbox.Textbox('pictures/textbox.png', 190, 25, 250, 550, surface)
	elif size == 1:
		Textbox = textbox.Textbox('pictures/textbox1.png', 190, 25, 250, 550, surface)
	else:
		Textbox = textbox.Textbox('pictures/textbox2.png', 190, 25, 250, 550, surface)
	font = pygame.font.SysFont('monospace', 15)
	Textbox.draw(surface)

	if len(message) != 0:
		surface.blit(font.render(message, 1, (0, 0, 0)), (255, 555))

	loop(30)	#fps

def getInput(msgs, question, surface, size=0):
	'''displays an input box and returns entered string'''

	current_string = ''
	displayMessage(msgs, surface)
	displayInputBox(question + current_string, surface, size)
	brk = False

	event = None
	while not brk:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_BACKSPACE:
					current_string = current_string[0:-1]
				elif event.key == K_RETURN:
					brk = True
				elif event.key <= 127:
					current_string = current_string + chr(event.key)
				displayInputBox(question + current_string, surface, size)

	return current_string

def returnStrings(filename):
	'''returns a list with strings between startID to stopID from a text file'''

	# os.chdir('text_files')

	file = open(filename, 'r')
	lines = {}

	for line in file:

		ID = ''
		found_ID = False
		new_line = ''

		if line == '\n':					# ignore empty lines
			continue

		line = line[0:-1]					# remove line breaks that are automatically added at the end of lines (\n)

		'''
			b = bilanguage
			B = bob's speech impediment
			c = caesar cipher
			v = viginere
			m = multiplicative cipher
			0 = normal/unencrypted
		'''
		encryption = 0
		if line[0] == 'b':
			encryption = 'bi'
		elif line[0] == 'B':
			encryption = 'bob'
		elif line[0] == 'c':
			encryption = 'caesar'
		elif line[0] == 'v':
			encryption = 'viginere'
		elif line[0] == 'm':
			encryption = 'mulcipher'
		'''elif line[0] == '0':
			encryption = 0'''

		line = line[1:]

		for char in line:
			if found_ID:
				new_line = new_line + char
			elif not char == ':':
				ID = ID + char
			elif char == ':':
				found_ID = True

		if encryption:
			new_line = cryptofunctions.encrypt(new_line, encryption)

		lines[ID] = new_line
		#print(lines[ID])

	# os.chdir('..')

	return lines

def get_item_descriptions(sprites):
	descriptions = returnStrings('text_files/descriptions.txt')

	for sprite in sprites:
		sprite.description = descriptions[sprite.description_ID]

def loop(FPS, event=0):
	pygame.display.flip()
	pygame.time.Clock().tick(FPS)
	if event == 0:
		return
	elif event.type == QUIT:
		pygame.quit()
		sys.exit()

def wait():
	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				return