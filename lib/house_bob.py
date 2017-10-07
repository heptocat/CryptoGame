import pygame
from pygame.locals import *
from lib import engine, progress
from lib import cryptofunctions

class House_bob(object):
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
						sprite.rect.x = 450
						sprite.rect.y = 0
		
		return self.mainloop(surface, event)

	def exit(self, new_room):
		self.in_room = False
		return ('house_bob', new_room)
	
	def talk_with_save(self, Save, surface):
		name = progress.getProgress('name')
		answer = engine.getInput((Save.lines['l1a'], (Save.lines['l1b'] + name)), Save.lines['l1q'], surface, 1)
		if answer == 'yes':
			engine.displayMessage((Save.lines['l2'], ), surface)
			engine.wait()
		elif answer == 'change name':
			answer = engine.getInput((Save.lines['l3'], ), ' ', surface, 2)
			progress.setProgress('name', answer)
			
	def talk_with_load(self, Load, surface):
		answer = engine.getInput((Load.lines['l1a'], Load.lines['l1b']), ' ', surface, 1)
		if answer == 'yes':
			answer = engine.getInput((Load.lines['l2'], ), ' ', surface, 1)
			engine.wait()
			
	def talk_with_bob(self, Bob, surface):
		status = progress.getProgress('bi_bob')
		name = progress.getProgress('name')
		if status == 0:
			answer = engine.getInput((Bob.lines['l1a'], ), Bob.lines['l1q'], surface, 2)
			progress.setProgress('bi_library', 2)
			if answer == 'yes':
				answer = engine.getInput((Bob.lines['l2yes'], ), Bob.lines['l2q'], surface, 2)
				progress.setProgress('name', answer)
				engine.displayMessage(((Bob.lines['l3a'] + cryptofunctions.encrypt(answer, 'bob')), Bob.lines['l3b']), surface)
				engine.wait()
				engine.getInput((Bob.lines['l4a'], ), Bob.lines['l4q'], surface, 2)
				engine.displayMessage((Bob.lines['l5'], ), surface)
				progress.setProgress('bi_bob', 1)
			else:
				engine.displayMessage((Bob.lines['l2no'], ), surface)
		elif status == 1:
			engine.displayMessage((Bob.lines['l6'], ), surface)
		
		engine.wait()
		
	def mainloop(self, surface, event):
		for sprite in self.sprites:
			if sprite.ID == 'PLAYER':
				Player = sprite
			if sprite.ID == 'BOB':
				Bob = sprite
			if sprite.ID == 'SAVE':
				Save = sprite
			if sprite.ID == 'LOAD':
				Load = sprite

		surface.blit(self.image, (0, 0))
		self.sprites.draw(surface)

		new_room = 'house_bob'
		from_room = 'house_bob'

		if event.type == KEYDOWN:
			if event.key == K_RETURN:
				if engine.checkBordering(Player, Bob) == True:
					self.talk_with_bob(Bob, surface)
				if engine.checkBordering(Player, Save) == True:
					self.talk_with_save(Save, surface)
				if engine.checkBordering(Player, Load) == True:
					self.talk_with_load(Load, surface)
				if Player.rect.x == 450 and Player.rect.y == 0:
					tmp = self.exit('bitown')
					from_room = tmp[0]
					new_room = tmp[1]

			elif event.key in (K_d, K_s, K_a, K_w):
				Player.move(event.key, self.collide_group)

		return (from_room, new_room)
