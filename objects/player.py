import objects.circleshape as circleshape
import pygame as game
from constants import PLAYER
from objects.bullet import Bullet

class Player(circleshape.CircleShape):
    cooldown = 0

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER['RADIUS'])
        self.rotation = 0

    def update(self, dt):
        Player.cooldown -= dt

        keys = game.key.get_pressed()

        if keys[game.K_w]:
            self.move(dt)
        if keys[game.K_a]:
            self.rotate(-dt)
        if keys[game.K_s]:
            self.move(-dt)
        if keys[game.K_d]:
            self.rotate(dt)
        if keys[game.K_SPACE]:
            self.shoot()

    def draw(self, screen):
        game.draw.polygon(screen, "white", self.triangle(), 2)

    def shoot(self):
        if Player.cooldown <= 0:
            bullet = Bullet(self.position.x, self.position.y)
            bullet.velocity = game.Vector2(0, 1).rotate(self.rotation) * PLAYER['SHOOT_SPEED']
            Player.cooldown = PLAYER['SHOOT_COOLDOWN']

    def move(self, dt):
        forward = game.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER['SPEED'] * dt
    
    def rotate(self, dt):
        self.rotation += PLAYER['TURN_SPEED'] * dt

    def triangle(self):
        forward = game.Vector2(0, 1).rotate(self.rotation)
        right = game.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]