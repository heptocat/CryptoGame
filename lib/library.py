import pygame
from pygame.locals import *
from lib import engine

class Library(object):
	def __init__(self, image, sprites, collide_group):

		self.image = pygame.image.load(image)

		self.sprites = sprites
		self.collide_group = collide_group

		self.in_room = False

	def enter(self, surface, event, from_room):
		if not self.in_room:
			self.in_room = True
			if from_room == 'bitown':
				for sprite in self.sprites:
					if sprite.ID == 'PLAYER':
						sprite.rect.x = 375
						sprite.rect.y = 600
		
		return self.mainloop(surface, event)

	def talk_with_bookbi(self, Book_bi, surface):
		engine.displayMessage((Book_bi.lines['l1a'], Book_bi.lines['l1b'], Book_bi.lines['l0'], Book_bi.lines['l1d'], Book_bi.lines['l1e'], Book_bi.lines['l1f'], Book_bi.lines['l1g']), surface)
		engine.wait()
		engine.displayMessage((Book_bi.lines['l2a'],Book_bi.lines['l0'],Book_bi.lines['l2b'], Book_bi.lines['l2c']), surface)
		engine.wait()
	
	def talk_with_bookbob(self, Book_bob, surface):
		engine.displayMessage((Book_bob.lines['l1a'], Book_bob.lines['l0'], Book_bob.lines['l1b'], Book_bob.lines['l1c']), surface)
		engine.wait()
		engine.displayMessage((Book_bob.lines['l2'], ), surface)
		engine.wait()
		engine.displayMessage((Book_bob.lines['l3a'], Book_bob.lines['l0'], Book_bob.lines['l3b']), surface)
		engine.wait()
		engine.displayMessage((Book_bob.lines['l4a'], Book_bob.lines['l4b'], Book_bob.lines['l4c'], Book_bob.lines['l4d']), surface)
		engine.wait()
	
	def exit(self, new_room):
		self.in_room = False
		return ('library', new_room)

	def mainloop(self, surface, event):
		for sprite in self.sprites:
			if sprite.ID == 'PLAYER':
				Player = sprite
			elif sprite.ID == 'BOOK_BI':
				Book_bi = sprite
			elif sprite.ID == 'BOOK_BOB':
				Book_bob = sprite
		surface.blit(self.image, (0, 0))
		self.sprites.draw(surface)

		new_room = 'library'
		from_room = 'library'

		if event.type == KEYDOWN:
			if event.key == K_RETURN:
				if engine.checkBordering(Player, Book_bi) == True:
					self.talk_with_bookbi(Book_bi, surface)
				if Player.rect.x == 375 and Player.rect.y == 600:
					tmp = self.exit('bitown')
					from_room = tmp[0]
					new_room = tmp[1]
				try:
					if engine.checkBordering(Player, Book_bob) == True:
						self.talk_with_bookbob(Book_bob, surface)
				except:
					pass
			elif event.key in (K_d, K_s, K_a, K_w):
				Player.move(event.key, self.collide_group)

		return (from_room, new_room)
