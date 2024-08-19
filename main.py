import pygame

from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    timer = pygame.time.Clock()
    dt = 0 # Delta time, for representing amount of time since last frame was drawn (for fps)

    while True:
        screen.fill("black")
        pygame.display.flip() # For refreshing screen

        # For checking if user closed window and exit game loop if they do (make close button work)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # pause game until 1/60th of a second passed
        dt = timer.tick(60) / 1000

if __name__ == "__main__":
    main()