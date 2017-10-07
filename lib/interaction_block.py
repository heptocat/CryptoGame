import pygame
from lib import engine

class Block(pygame.sprite.Sprite):
	'''this sprite cannot (shouldn't) move'''

	def __init__(self, imagepath, width, height, x, y, surface, ID='NONE', textfile=False):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(imagepath)

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.ID = ID

		if textfile:
			self.lines = engine.returnStrings(textfile)

	def draw(self, surface):
		surface.blit(self.image, self.rect)

	def changePicture(self, newpic):
		if newpic == 1:
			self.image = pygame.image.load(self.imagepath)
		elif newpic == 2:
			self.image = pygame.image.load(self.imagepath2)