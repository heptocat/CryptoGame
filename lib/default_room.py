import pygame
from pygame.locals import *
from lib import engine

class Default(object):
	def __init__(self, image, sprites, collide_group):
		
		self.image = pygame.image.load(image)

		self.sprites = sprites
		self.collide_group = collide_group

		self.in_room = True

	def enter(self, surface, event, from_room):					# from_room is so we can set the coords correctly
		if not self.in_room:									# when enetering from another room
			self.in_room = True
			if from_room == 'bitown':
				for sprite in self.sprites:
					if sprite.ID == 'PLAYER':
						sprite.rect.x = 250
						sprite.rect.y = 450
		return self.mainloop(surface, event)

	def exit(self, new_room):
		self.in_room = False
		return ('default_room', new_room)

	def talk_with_sign1(self, Sign, surface):
		answer = engine.getInput((Sign.lines['l1a'], Sign.lines['l1b']), Sign.lines['q1'], surface)
		engine.displayMessage((Sign.lines['l2a'], Sign.lines['l2b'], answer, ), surface)
		engine.wait()


	def mainloop(self, surface, event):

		for sprite in self.sprites:								# pull sprites from sprite group to make it easier
			if sprite.ID == 'PLAYER':
				Player = sprite
			elif sprite.ID == 'SIGN':
				Sign = sprite
			elif sprite.ID == 'START':
				Start = sprite

		surface.blit(self.image, (1, 1))
		self.sprites.draw(surface)

		new_room = 'default_room'
		from_room = 'default_room'

		if event.type == KEYDOWN:
			if event.key == K_RETURN:
				if engine.checkBordering(Player, Sign):
					self.talk_with_sign1(Sign, surface)
				if engine.checkBordering(Player, Start):
					tmp = self.exit('bitown')
					from_room = tmp[0]
					new_room = tmp[1]
			elif event.key in (K_d, K_s, K_a, K_w):
				Player.move(event.key, self.collide_group)

		return (from_room, new_room)
