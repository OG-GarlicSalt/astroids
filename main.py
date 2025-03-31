import pygame
from player import Player
from constants import *
from asteroidfield import AsteroidField
from asteroid import Asteroid
def main():
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        updateable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroid = pygame.sprite.Group()
        AsteroidField.containers = (updateable, )
        Asteroid.containers = (updateable, drawable, asteroid)
        Player.containers = (updateable, drawable)
        asteroid_field = AsteroidField()
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        print("Starting Asteroids!")
        print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                return
                screen.fill("black")
                for obj in drawable:
                        obj.draw(screen)
                dt = clock.tick(60) / 1000
                updateable.update(dt)
                pygame.display.flip()
                
if __name__ == "__main__":
    main()  