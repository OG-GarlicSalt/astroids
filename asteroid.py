from constants import *
import pygame
from circleshape import CircleShape
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # Call parent constructor
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        # Add movement logic here
        # You need to update the position based on velocity and dt
        # Something like: self.position += self.velocity * dt

        self.position += self.velocity * dt 

    def split(self, other):
        self.kill()
        other.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        if self.radius >= ASTEROID_MIN_RADIUS:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            random_angle = random.uniform(20, 50)
            velocity_1 = self.velocity.rotate(random_angle) * 1.2
            velocity_2 = self.velocity.rotate(-random_angle) * 1.2
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = velocity_1
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2.velocity = velocity_2
            
