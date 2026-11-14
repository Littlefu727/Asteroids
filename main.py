import os
import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, LINE_WIDTH
from logger import log_state,log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

# Ensure the wayland driver is fully targeted
os.environ["SDL_VIDEODRIVER"] = "x11"

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0.0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)


    # Initialize a player
    player_one = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Initialize asteorid field
    asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, "black")

        # Using groups
        updatable.update(dt)
        for e in drawable:
            e.draw(screen)

        pygame.display.flip()
        for a in asteroids:
            if a.collide_with(player_one):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
