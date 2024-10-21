import pygame as game
import random
from objects.asteroid import Asteroid
from constants import SCREEN, ASTEROID


class AsteroidField(game.sprite.Sprite):
    edges = [
        [
            game.Vector2(1, 0),
            lambda y: game.Vector2(-ASTEROID['MAX_SCALE'] * ASTEROID['MIN_RADIUS'], y * SCREEN['HEIGHT']),
        ],
        [
            game.Vector2(-1, 0),
            lambda y: game.Vector2(
                SCREEN['WIDTH'] + ASTEROID['MAX_SCALE'] * ASTEROID['MIN_RADIUS'], y * SCREEN['HEIGHT']
            ),
        ],
        [
            game.Vector2(0, 1),
            lambda x: game.Vector2(x * SCREEN['WIDTH'], -ASTEROID['MAX_SCALE'] * ASTEROID['MIN_RADIUS']),
        ],
        [
            game.Vector2(0, -1),
            lambda x: game.Vector2(
                x * SCREEN['WIDTH'], SCREEN['HEIGHT'] + ASTEROID['MAX_SCALE'] * ASTEROID['MIN_RADIUS']
            ),
        ],
    ]

    def __init__(self):
        game.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID['SPAWN_RATE']:
            self.spawn_timer = 0

            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID['KINDS'])
            self.spawn(ASTEROID['MIN_RADIUS'] * kind, position, velocity)