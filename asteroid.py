from circleshape import CircleShape
import pygame
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        a = random.uniform(20, 50)
        a1 = self.velocity.rotate(a)
        a2 = self.velocity.rotate(-a)
        nRadius = self.radius - ASTEROID_MIN_RADIUS

        ast1 = Asteroid(self.position.x, self.position.y, nRadius)
        ast2 = Asteroid(self.position.x, self.position.y, nRadius)

        ast1.velocity = a1*1.2
        ast2.velocity = a2*1.2
