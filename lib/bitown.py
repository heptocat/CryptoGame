import pygame
from pygame.locals import *
from lib import engine, progress

class Bitown(object):
	def __init__(self, image, sprites, collide_group):
		
		self.image = pygame.image.load(image)

		self.sprites = sprites
		self.collide_group = collide_group

		self.in_room = False

	def enter(self, surface, event, from_room):					# from_room is so we can set the coords correctly
		if not self.in_room:
			self.in_room = True

			pygame.mixer.music.load('sound_files/bitown_bg.ogg')
			pygame.mixer.music.play(-1)

			if from_room == 'default_room':
				for sprite in self.sprites:
					if sprite.ID == 'PLAYER':
						sprite.rect.x = 225
						sprite.rect.y = 450
			
			if from_room == 'house1':
				for sprite in self.sprites:
					if sprite.ID == 'PLAYER':
						sprite.rect.x = 300
						sprite.rect.y = 150

			if from_room == 'bar':
				for sprite in self.sprites:
					if sprite.ID == 'PLAYER':
						sprite.rect.x = 225
						sprite.rect.y = 300

			if from_room == 'house_bob':
				for sprite in self.sprites:
					if sprite.ID == 'PLAYER':
						sprite.rect.x = 600
						sprite.rect.y = 150

			if from_room == 'pickleshed':
				for sprite in self.sprites:
					if sprite.ID == 'PLAYER':
						sprite.rect.x = 675
						sprite.rect.y = 450

			if from_room == 'library':
				for sprite in self.sprites:
					if sprite.ID == 'PLAYER':
						sprite.rect.x = 675
						sprite.rect.y = 375

		return self.mainloop(surface, event)

	def exit(self, new_room):
		pygame.mixer.music.stop()
		self.in_room = False
		return ('bitown', new_room)


	def mainloop(self, surface, event):

		for sprite in self.sprites:								# pull sprites from sprite group to make it easier
			if sprite.ID == 'PLAYER':
				Player = sprite
			elif sprite.ID == 'DOOR':
				Door = sprite
			elif sprite.ID == 'DOOR_BAR':
				Door_bar = sprite
			elif sprite.ID == 'DOOR_BOB':
				Door_bob = sprite
			elif sprite.ID == 'DOOR_PPSHED':
				Door_pickleshed = sprite
			elif sprite.ID == 'DOOR_LIB':
				Door_library = sprite
			elif sprite.ID == 'PICKLEPLANT':
				Pickle_plant = sprite

		for item in self.items:
			if item.ID == 'PICKLE':
				Pickle = item

		surface.blit(self.image, (1, 1))
		self.sprites.draw(surface)

		new_room = 'bitown'
		from_room = 'bitown'

		if event.type == KEYDOWN:
			if event.key == K_RETURN:
				if engine.checkBordering(Player, Door):
					tmp = self.exit('house1')
					from_room = tmp[0]
					new_room = tmp[1]

				elif engine.checkBordering(Player, Door_bar):
					tmp = self.exit('bar')
					from_room = tmp[0]
					new_room = tmp[1]

				elif engine.checkBordering(Player, Door_bob):
					tmp = self.exit('house_bob')
					from_room = tmp[0]
					new_room = tmp[1]

				elif engine.checkBordering(Player, Door_pickleshed):
					tmp = self.exit('pickleshed')
					from_room = tmp[0]
					new_room = tmp[1]

				elif engine.checkBordering(Player, Door_library):
					tmp = self.exit('library')
					from_room = tmp[0]
					new_room = tmp[1]

				elif engine.checkBordering(Player, Pickle_plant):
					status = progress.getProgress('bi_pickle')
					#if not Pickle in Player.inventory:
					if status == 1:
						ans = ''

						while not ans in ('yes', 'no'):
							ans = engine.getInput((Pickle_plant.lines['unpicked'], ), Pickle_plant.lines['q1'], surface)

						if ans =='yes':
							progress.setProgress('bi_pickle', 2)
							Player.add_to_inventory((Pickle, ))
							Pickle_plant.picked = True
							Pickle_plant.changePicture(2)

							engine.displayMessage((Pickle_plant.lines['unpicked2'], ), surface)
							engine.wait()
					
					elif not (status ==0):
						engine.displayMessage((Pickle_plant.lines['picked'], ), surface)
						engine.wait()


			elif event.key in (K_d, K_s, K_a, K_w):
				Player.move(event.key, self.collide_group)

		return (from_room, new_room)
