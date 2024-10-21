from constants import ASTEROID
from objects.circleshape import CircleShape
import pygame as game
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID['MIN_RADIUS']:
            return
        rand = random.uniform(20, 50)
        split1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID['MIN_RADIUS'])
        split2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID['MIN_RADIUS'])
        split1.velocity = self.position.rotate(rand)
        split2.velocity = self.position.rotate(-rand)

    def draw(self, screen):
        game.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt