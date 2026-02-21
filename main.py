import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from shoot import Shoot
from asteroidfield import AsteroidField
from circleshape import CircleShape
import sys

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    
    shots = pygame.sprite.Group()

    Shoot.containers = (shots, updatable, drawable)

    player = Player(x,y)
    asteroid_field = AsteroidField()
    

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        updatable.update(dt)

        for i in asteroids:
            if player.collides_with(i):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
            for shot in shots:
                if shot.collides_with(i):
                    log_event("asteroid_shot")
                    shot.kill()
                    i.splitw()
        
        for i in drawable:
            i.draw(screen)



        pygame.display.flip()

        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
