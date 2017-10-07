import pygame
from  pygame.locals import *

class Textbox(pygame.sprite.Sprite):
	def __init__(self, image, width, height, x, y, surface):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(image)

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def draw(self, surface):
		surface.blit(self.image, self.rect)