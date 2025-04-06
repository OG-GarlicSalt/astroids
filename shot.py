from circleshape import CircleShape
from constants import *
 
class Shot(CircleShape):
    def __init__ (self, x ,y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def update(self, dt):
        pass