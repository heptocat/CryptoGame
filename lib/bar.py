import pygame
from pygame.locals import *
from lib import engine, progress

class Bar(object):
	def __init__(self, image, sprites, collide_group):

		self.image = pygame.image.load(image)

		self.sprites = sprites
		self.collide_group = collide_group

		self.in_room = False

	def enter(self, surface, event, from_room):
		if not self.in_room:
			self.in_room = True

			pygame.mixer.music.load('sound_files/bar_bg.ogg')
			pygame.mixer.music.play(-1)

			if from_room == 'bitown':

				for sprite in self.sprites:
					if sprite.ID == 'PLAYER':
						sprite.rect.x = 825
						sprite.rect.y = 300
		
		return self.mainloop(surface, event)

	def exit(self, new_room):
		self.in_room = False
		pygame.mixer.music.stop()
		return ('bar', new_room)
	
	def talk_with_bartender(self, Bartender, Player, surface):
		for item in self.items:
			if item.ID == 'PICKLEJUICE':
				Picklejuice = item
			if item.ID == 'BEER':
				Beer = item

		for item in Player.inventory:
			if item.ID == 'PICKLE':
				Pickle = item

		answer = engine.getInput((Bartender.lines['l1a'], Bartender.lines['l1b'], Bartender.lines['l0']), Bartender.lines['q1'], surface, 2)
		while not answer in ('bebiebir', 'pibicklebi jubiibicebi', 'webit mabirtibinibi', 'picklej'):
			answer = engine.getInput((Bartender.lines['l2c'],  Bartender.lines['l1a'], Bartender.lines['l1b']), Bartender.lines['q1'], surface, 2)
		
		if answer == 'webit mabirtibinibi':
			engine.displayMessage((Bartender.lines['l2a'] + answer + Bartender.lines['l2b'], ), surface)
		elif answer == 'bebiebir':
			engine.displayMessage((Bartender.lines['l2a'] + answer + Bartender.lines['l2b'], ), surface)
			engine.wait()
			engine.displayMessage((Bartender.lines['l5a'], ), surface)
			Player.inventory.add(Beer)
		elif answer == 'pibicklebi jubiibicebi' or answer == 'picklej':
			status = progress.getProgress('bi_pickle')
			if status == 0 or status == 1:
				engine.displayMessage((Bartender.lines['l3a'], ), surface)
				progress.setProgress('bi_pickle', 1)
			elif status == 2:
				engine.displayMessage((Bartender.lines['l4a'], ), surface)
				engine.wait()
				engine.displayMessage((Bartender.lines['l4b'], ), surface)
				Player.inventory.remove(Pickle)
				Player.inventory.add(Picklejuice)
				progress.setProgress('bi_pickle', 0)
		elif answer == 'esc':
			pass

				
		engine.wait()
	
	def talk_with_poet(self, Poet, surface):
		engine.displayMessage((Poet.lines['l1a'], Poet.lines['l1b'], Poet.lines['l1c'], Poet.lines['l1d'], Poet.lines['l1e']), surface)
		engine.wait()
		engine.displayMessage((Poet.lines['l2a'], ), surface)
		engine.wait()
				

	def mainloop(self, surface, event):

		for sprite in self.sprites:
			if sprite.ID == 'PLAYER':
				Player = sprite
			elif sprite.ID == 'POET':
				Poet = sprite
			elif sprite.ID == 'BARTENDER':
				Bartender = sprite


		surface.blit(self.image, (1, 1))
		self.sprites.draw(surface)

		new_room = 'bar'
		from_room = 'bar'

		if event.type == KEYDOWN:
			if event.key == K_RETURN:
				if engine.checkBordering(Player, Bartender) == True:
					self.talk_with_bartender(Bartender, Player, surface)
				elif engine.checkBordering(Player, Poet) == True:
					self.talk_with_poet(Poet, surface)
				elif Player.rect.x == 825 and Player.rect.y == 300:
					tmp = self.exit('bitown')
					from_room = tmp[0]
					new_room = tmp[1]

			elif event.key in (K_d, K_s, K_a, K_w):
				Player.move(event.key, self.collide_group)

		return (from_room, new_room)
