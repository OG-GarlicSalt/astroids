
import pygame
from circleshape import CircleShape

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