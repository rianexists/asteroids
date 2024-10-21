from objects.circleshape import CircleShape
import pygame as game
from constants import BULLET_RADIUS

class Bullet(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, BULLET_RADIUS)

    def draw(self, screen):
        game.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt