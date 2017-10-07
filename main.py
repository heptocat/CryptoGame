#!/usr/bin/python3
#This is just so you can run it directly. Don't know if it works for Windows.
import pygame, sys, os
from pygame.locals import *
from lib import engine
from lib import interaction_block, item
from lib import player, progress
from lib import bar, default_room, house1, bitown, house_bob, pickleshed, library, inventory, memory

os.chdir(sys.path[0])			# change to correct directory

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((900, 675))
pygame.display.set_caption('this_is_a_game')

font = pygame.font.SysFont('monospace', 15)

# set up sprites
Player = player.Player('pictures/plr.png', 75, 75, 75, 75, DISPLAYSURF, 'PLAYER')

Sign = interaction_block.Block('pictures/sign.png', 75, 75, 300, 525, DISPLAYSURF, 'SIGN', 'text_files/sign1.txt')
Start = interaction_block.Block('pictures/start.png', 75, 75, 525, 525, DISPLAYSURF, 'START')
wall1 = interaction_block.Block('pictures/wall.png', 75, 75, 150, 150, DISPLAYSURF)
wall2 = interaction_block.Block('pictures/wall.png', 75, 75, 225, 150, DISPLAYSURF)

door1 = interaction_block.Block('pictures/door.png', 75, 75, 375, 150, DISPLAYSURF, 'DOOR')
door2 = interaction_block.Block('pictures/door_bar.png', 150, 150, 300, 300, DISPLAYSURF, 'DOOR_BAR')
door_bob = interaction_block.Block('pictures/door_bob.png', 150, 150, 600, 0, DISPLAYSURF, 'DOOR_BOB')
door_pickleshed = interaction_block.Block('pictures/door_ppshed.png', 150, 150, 675, 525, DISPLAYSURF, 'DOOR_PPSHED')
door_library = interaction_block.Block('pictures/door_library.png', 150, 150, 675, 225, DISPLAYSURF, 'DOOR_LIB')


Bartender = interaction_block.Block('pictures/bartender.png', 150, 150, 525, 75, DISPLAYSURF, 'BARTENDER', 'text_files/bartender.txt')
Poet = interaction_block.Block('pictures/poet.png', 75, 75, 75, 300, DISPLAYSURF, 'POET', 'text_files/poet.txt')
Bob = interaction_block.Block('pictures/bob.png', 75, 75, 75, 300, DISPLAYSURF, 'BOB', 'text_files/bob.txt')
Peter = interaction_block.Block('pictures/peter.png', 75, 75, 0, 0, DISPLAYSURF, 'PETER', 'text_files/peter.txt')

Pickle_plant = interaction_block.Block('pictures/pickleplant_pickle.png', 150, 150, 450, 525, DISPLAYSURF, 'PICKLEPLANT', 'text_files/pickleplant.txt')
Pickle_plant.imagepath2 = 'pictures/pickleplant_picked.png'
#Pickle_plant.picked = False

Book_bi = interaction_block.Block('pictures/book_bi.png', 150, 150, 75, 150, DISPLAYSURF, 'BOOK_BI', 'text_files/book_bi.txt')
Book_bob = interaction_block.Block('pictures/book_bob.png', 150, 150, 75, 375, DISPLAYSURF, 'BOOK_BOB', 'text_files/book_bob.txt')

Load = interaction_block.Block('pictures/load.png', 70, 70, 825, 525, DISPLAYSURF, 'LOAD', 'text_files/load.txt')
Save = interaction_block.Block('pictures/save.png', 70, 70, 825, 300, DISPLAYSURF, 'SAVE', 'text_files/save.txt')

Pickle = item.Item('pictures/pickle.png', DISPLAYSURF, 'PICKLE', 'pickle')
Picklejuice = item.Item('pictures/picklejuice.png', DISPLAYSURF, 'PICKLEJUICE', 'pickle_juice')
Beer = item.Item('pictures/beer.png', DISPLAYSURF, 'BEER', 'beer')

Inventory_cursor = interaction_block.Block('pictures/cursor.png', 85, 85, 200, 495, DISPLAYSURF)

Inventory = inventory.Inventory('pictures/inventory.png', 520, 180, 190, 485, Inventory_cursor, DISPLAYSURF)

# get item descriptions

engine.get_item_descriptions((Pickle, Picklejuice, Beer))

# set up sprite groups
default_group = pygame.sprite.Group(Player, Sign, Start, wall1, wall2)
default_collide = pygame.sprite.Group(Sign, Start, wall1, wall2)

bitown_group = pygame.sprite.Group(Player, door1, door2, Pickle_plant, door_bob, door_library, door_pickleshed)
bitown_collide = pygame.sprite.Group(door1, door2, Pickle_plant, door_bob, door_library, door_pickleshed)
bitown_items = pygame.sprite.Group(Pickle, Beer)

house1_group = pygame.sprite.Group(Player)
house1_collide = pygame.sprite.Group()

bar_group = pygame.sprite.Group(Player, Bartender, Poet)
bar_collide = pygame.sprite.Group(Bartender, Poet)
bar_items = pygame.sprite.Group(Picklejuice, Beer)

house_bob_group = pygame.sprite.Group(Player, Bob, Load, Save)
house_bob_collide = pygame.sprite.Group(Bob, Load, Save)

pickleshed_group = pygame.sprite.Group(Player, Peter)
pickleshed_collide = pygame.sprite.Group(Peter)

library_group = pygame.sprite.Group(Player, Book_bi
)
library_collide = pygame.sprite.Group(Book_bi)

# set up rooms
Default = default_room.Default('pictures/defaultroom.png', default_group, default_collide)
House1 = house1.House1('pictures/house.png', house1_group, house1_collide)
Bar = bar.Bar('pictures/bar.png', bar_group, bar_collide)
Bar.items = bar_items
Bitown = bitown.Bitown('pictures/bitown.png', bitown_group, bitown_collide)
Bitown.items = bitown_items
House_bob = house_bob.House_bob('pictures/house_bob_bg.png', house_bob_group, house_bob_collide)
Pickleshed = pickleshed.Pickleshed('pictures/pickleshed_bg.png', pickleshed_group, pickleshed_collide)
Library = library.Library('pictures/library_bg.png', library_group, library_collide)

current_room = 'default_room'

old_room = 'default_room'



def updateGroups():
	if progress.getProgress('bi_library') == 2:
		library_group.add(Book_bob)
		library_collide.add(Book_bob)
		Library = library.Library('pictures/library_bg.png', library_group, library_collide)

updateGroups()
# mainloop

while True:
	#updateGroups()
	for event in pygame.event.get():

		if event.type == KEYDOWN:
			if event.key == K_e:
				Inventory.open(Player.inventory, DISPLAYSURF)

		if current_room == 'default_room':
			tmp = Default.enter(DISPLAYSURF, event, old_room)
			old_room = tmp[0]										# tmp[0] == room that player was in last time
			current_room = tmp[1]									# tmp[1] == room that player is going to be in next time
		elif current_room == 'bitown':
			tmp = Bitown.enter(DISPLAYSURF, event, old_room)
			old_room = tmp[0]
			current_room = tmp[1]
			
		elif current_room == 'house1':
			tmp = House1.enter(DISPLAYSURF, event, old_room)
			old_room = tmp[0]
			current_room = tmp[1]

		elif current_room == 'bar':
			tmp = Bar.enter(DISPLAYSURF, event, old_room)
			old_room = tmp[0]
			current_room = tmp[1]

		elif current_room == 'house_bob':
			tmp = House_bob.enter(DISPLAYSURF, event, old_room)
			old_room = tmp[0]
			current_room = tmp[1]

		elif current_room == 'library':
			updateGroups()
			tmp = Library.enter(DISPLAYSURF, event, old_room)
			old_room = tmp[0]
			current_room = tmp[1]

		elif current_room == 'pickleshed':
			tmp = Pickleshed.enter(DISPLAYSURF, event, old_room)
			old_room = tmp[0]
			current_room = tmp[1]








	engine.loop(FPS, event)
