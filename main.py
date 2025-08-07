# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroidfield import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

print ("Starting Asteroids!")
print (f"Screen width: {SCREEN_WIDTH}")
print (f"Screen height: {SCREEN_HEIGHT}")

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable, drawable)

asteroids = pygame.sprite.Group()
Asteroid.containers = (asteroids, updatable, drawable)

AsteroidField.containers = (updatable)

ship = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)

clock = pygame.time.Clock()
dt=0

def main():
	while True:	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		dt = clock.tick(60) / 1000
		updatable.update(dt)
		screen.fill((0,0,0))
		for sprite in drawable:
			sprite.draw(screen)

		pygame.display.flip()
		


if __name__ == "__main__":
    main()

