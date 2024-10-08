import pygame

from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.font.init()
    score_text = pygame.font.SysFont("your_font.ttf", 24)
    score = 0
    raise_difficulty = 500

    timer = pygame.time.Clock()
    dt = 0 # Delta time, for representing amount of time since last frame was drawn (for fps)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    # Use static field called containers to add the instances to the groups
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)
    Shot.containers = (drawable, updatable, bullets)

    asteroidField = AsteroidField()
    player = Player(x, y)

    while True:
        # pause game until 1/60th of a second passed
        dt = timer.tick(60) / 1000

        
        screen.fill("black")
        score_surface = score_text.render(str(score), True, "white")
        screen.blit(score_surface, (x , 50))

        for d in drawable:
            d.draw(screen)

        for u in updatable:
            u.update(dt)

        for a in asteroids:
            for b in bullets:
                if b.collision_checker(a):
                    a.split()
                    b.kill()
                    score += 100

                    if score >= raise_difficulty:
                        asteroidField.spawn_rate -= 0.1
                        raise_difficulty += 500

            if player.collision_checker(a):
                print("Game over!")
                return
            
        
        
            
        pygame.display.flip() # For refreshing screen

        # For checking if user closed window and exit game loop if they do (make close button work)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        

        

if __name__ == "__main__":
    main()