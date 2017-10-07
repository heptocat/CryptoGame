import pygame
from pygame.locals import *
from lib import engine, textbox

class Inventory(pygame.sprite.Sprite):
	def __init__(self, image, width, heigth, x, y, cursor, surface):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(image)

		self.cursor = cursor

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.cursor_speed = 85

		self.description_box = textbox.Textbox('pictures/item_description_box.png',
								520, 25, self.rect.left, self.rect.top - 40, surface)

	def draw(self, sprites, current_item, surface):
		font = pygame.font.SysFont('monospace', 15)

		surface.blit(self.image, self.rect)
		x = self.rect.x + 10
		y = self.rect.y + 10
		for sprite in sprites:
			surface.blit(sprite.image, (x, y))
			sprite.rect.x = x
			sprite.rect.y = y
			x += 85
			if x > 700:
				x = self.rect.x + 10
				y += 85

		surface.blit(self.cursor.image, self.cursor.rect)

		surface.blit(self.description_box.image, self.description_box.rect)

		if not current_item == 0:
			surface.blit(font.render(current_item.description, 1, (0, 0, 0)),
						(self.description_box.rect.left + 10, self.description_box.rect.top + 5))


		pygame.display.flip()

	def move(self, key, sprites=0):
		'''checks collisions with other objects, then sets new coords for sprite'''

		old_x = self.cursor.rect.x
		old_y = self.cursor.rect.y

		if key == K_d:
			self.cursor.rect.x += self.cursor_speed
		elif key == K_s:
			self.cursor.rect.y += self.cursor_speed
		elif key == K_a:
			self.cursor.rect.x -= self.cursor_speed
		elif key == K_w:
			self.cursor.rect.y -= self.cursor_speed

		#if self.cursor.rect.x == 105 or self.cursor.rect.x == 710 or self.cursor.rect.y == 400 or self.cursor.rect.y == 665:
		if (self.cursor.rect.x == self.rect.left - 75 or self.cursor.rect.x == self.rect.right or
			self.cursor.rect.y == self.rect.top - 75 or self.cursor.rect.y == self.rect.bottom):

			self.cursor.rect.x = old_x
			self.cursor.rect.y = old_y
		'''for s in sprites:
			if engine.checkCollision(self, s):
				self.rect.x = old_x
				self.rect.y = old_y
				break'''

	def open(self, sprites, surface):

		current_item = 0
		on_item = 0
		self.draw(sprites, current_item, surface)

		while 1:
			on_item = 0
			for event in pygame.event.get():
				for sprite in sprites:
					if engine.checkCollision(self.cursor, sprite):
						current_item = engine.checkCollision(self.cursor, sprite)[1]
						on_item = 1

				if on_item == 0:
					current_item = 0

				self.draw(sprites, current_item, surface)

				if event.type == KEYDOWN:
					if event.key in (K_d, K_s, K_a, K_w):
						self.move(event.key)

						'''for sprite in sprites:
							if engine.checkCollision(self.cursor, sprite):
								print(sprite.ID)
								current_item = engine.checkCollision(self.cursor, sprite)[1]
								print(current_item)
							else:
								current_item = 0'''

					elif event.key == K_e:
						return

