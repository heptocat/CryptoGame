import pygame
from pygame.locals import *
from lib import engine

class House1(object):
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

	def exit(self, new_room):
		self.in_room = False
		return ('house1', new_room)

	def mainloop(self, surface, event):
		for sprite in self.sprites:
			if sprite.ID == 'PLAYER':
				Player = sprite

		surface.blit(self.image, (0, 0))
		self.sprites.draw(surface)

		new_room = 'house1'
		from_room = 'house1'

		if event.type == KEYDOWN:
			if event.key == K_RETURN:
				if Player.rect.x in (375, 450) and Player.rect.y == 600:
					tmp = self.exit('bitown')
					from_room = tmp[0]
					new_room = tmp[1]

			elif event.key in (K_d, K_s, K_a, K_w):
				Player.move(event.key, self.collide_group)

		return (from_room, new_room)
