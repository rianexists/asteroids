import sys
import pygame as game
from constants import SCREEN
from objects.player import Player
from objects.bullet import Bullet
from objects.asteroid import Asteroid
from objects.asteroidfield import AsteroidField

def main():
    game.init()
    screen = game.display.set_mode((SCREEN['WIDTH'], SCREEN['HEIGHT']))
    clock = game.time.Clock()
    survive = 0
    startTime = clock.get_time()

    updatable = game.sprite.Group()
    drawable = game.sprite.Group()

    asteroids = game.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = updatable
    asteroidField = AsteroidField()

    bullets = game.sprite.Group()
    Bullet.containers = (bullets, updatable, drawable)

    Player.containers = (updatable, drawable)

    player = Player(SCREEN['WIDTH'] / 2, SCREEN['HEIGHT'] / 2)

    dt = 0

    while True:
        for event in game.event.get():
            if event.type == game.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for bullet in bullets:
                if asteroid.collides_with(bullet):
                    asteroid.split()
                    bullet.kill()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        game.display.flip()

        dt = clock.tick(60) / 1000
        '''if survive < clock.get_time() - startTime:
            survive = clock.get_time() - startTime
            print(survive)'''

if __name__ == "__main__":
    main()