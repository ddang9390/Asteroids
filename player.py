from circleshape import *
from constants import *
from shot import *

import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        CircleShape.__init__(self, x=x, y=y, radius=PLAYER_RADIUS)

        self.rotation = 0
        self.timer = 0
        self.score = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        self.timer = PLAYER_SHOOT_COOLDOWN

        bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        bullet.velocity *= PLAYER_SHOT_SPEED



    def collision_checker(self, circle):
        collide = False
        pos = circle.position

        distance = pygame.Vector2.distance_to(self.position, pos)

        if distance < (self.radius + circle.radius):
            collide = True

        return collide

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            if not self.timer > 0:
                self.shoot()