import pygame
from pygame.locals import *
import sys

pygame.init()

fpsClock = pygame.time.Clock()

posX_ini = 10
posY_ini = 100
posX = posX_ini
posY = posY_ini

velX_ini = 30
velY_ini = 0

acelX = -9 # simulacion de la oposicion al medio en el que se mueve (para no complicarme mucho)
acelY = 3.8

mCircle = 10

surface = pygame.display.set_mode((1280,720))


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
	
	tiempo = pygame.time.get_ticks() / 1000 #segundos
	velY = velY_ini + acelY*tiempo
	velX = velX_ini + acelX*tiempo
	posY = posY + velY + (1/2)*acelY*tiempo**2
	posX = posX + velX + (1/2)*acelX*tiempo**2



	if posY <= 700:
		#surface.fill((0,0,0)) # lo dejo comentado para que se vea la trayectoria
		circle = pygame.draw.circle(surface, (125,0,255), (int(posX), int(posY)), 7, 2)

	pygame.display.update()
	fpsClock.tick(120)