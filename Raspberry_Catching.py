import pygame
import random
from pygame.locals import *
from sys import exit

spoon_x = 300
spoon_y = 700

raspberry_x = spoon_x
raspberry_y = spoon_y
pygame.init()

score = 0

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Raspberry Catching')

spoon = pygame.image.load('Spoon.jpg').convert()
raspberry = pygame.image.load('Raspberry_2.png').convert()
screen_width = 600

def update_spoon():
	global spoon_x
	global spoon_y
	spoon_x, ignore = pygame.mouse.get_pos()
	screen.blit(spoon, (spoon_x, spoon_y))

def update_raspberry():
	global raspberry_x
	global raspberry_y
	raspberry_y += 5
	if raspberry_y > spoon_y:
		raspberry_y = 0
		raspberry_x = random.randint(10, screen_width)
	raspberry_x += random.randint(-5, 5)
	if raspberry_x < 10:
		raspberry_x = 10
	if raspberry_x > screen_width - 20:
		raspberry_x = screen_width - 20
	screen.blit(raspberry, (raspberry_x, raspberry_y))

def check_for_catch():
	global score
	global raspberry_x
	global raspberry_y
	x = spoon_x#- 121
	if (abs(x - raspberry_x) <= 40) and (spoon_y - raspberry_y<= 20):
		score += 1
		raspberry_y = 0
	display("Score: " + str(score))
	#print(x, raspberry_x, spoon_y, raspberry_y)
def display(message):
	font = pygame.font.Font(None, 36)
	text = font.render(message, 1, (10, 10, 10))
	screen.blit(text, (0, 0))

clock = pygame.time.Clock()
clock.tick(30)

while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

 	screen.fill((255, 255, 255))
	spoon_x, ignore = pygame.mouse.get_pos()
	screen.blit(spoon, (spoon_x, spoon_y))
	update_raspberry()
	update_spoon()
	check_for_catch()
	pygame.display.update()

