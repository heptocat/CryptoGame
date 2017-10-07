import pygame
from lib import engine

class Item(pygame.sprite.Sprite):
	def __init__(self, imagepath, surface, ID, description_ID):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(imagepath)

		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0

		self.ID = ID

		self.description_ID = description_ID
