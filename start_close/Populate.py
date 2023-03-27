from V import V
import math
from random import gauss
from Engine import tick
from WindowSingleton import WindowSingleton
from graphics import Circle, Point, color_rgb
from random import random
from constants import ballRadius, holePosition, HILL_RADIUS, HILL_CENTER, VALLEY_RADIUS, VALLEY_CENTER, WALL_RANDOM_FACTOR


class Populate:
    def __init__(self, velocity, position=V(2, .2, 0), dt=.1, mass=.045, color="white", **kwargs):
        self.position = position
        self.startingDt = dt
        self.dt = dt
        self.mass = mass

        self.startingVelocity = velocity
        self.velocity = velocity

        self.sphere = Circle(Point(self.position.x, self.position.y), ballRadius)

        self.sphere.setFill(color)
        self.sphere.setOutline("white")
        self.sphere.draw(WindowSingleton()())

        self.dead = False
        self.inHole = False

        self.tT = 0
    
    @staticmethod
    def createNew(dt=.1):
        mass = 0.045 # kg

        # return Populate(random() * 90, gravity, drag, magnus, dt=dt)
        # return Populate(V(2, 0, 0), dt=dt, mass=mass)
        return Populate(V((random()-.5) * 6, (random()-.5)*12, 0), dt=dt, mass=mass)
        # return Populate(V(gauss(0, .5), gauss(0, 1.5), 0), dt=dt, mass=mass)
        
    @staticmethod
    def createFrom(populate, stdDev, color="white"):
        velocity = V(gauss(populate.startingVelocity.x, stdDev), gauss(populate.startingVelocity.y, stdDev), 0)

        return Populate(velocity, dt=populate.startingDt, mass=populate.mass, color=color)

    def stepBack(self):
        self.position -= self.velocity * self.dt

    def collision(self, walls=None):
        # subtract radius
        if self.position.x - ballRadius < 0:
            self.stepBack()
            Nn = V(1, 0, 0)
            rNn = Nn.rotate((0.5-random())*WALL_RANDOM_FACTOR*2)
            speed_kept = 1 - .2 * abs((self.velocity() * rNn))
            self.velocity += 2 * rNn * abs(self.velocity * rNn) * speed_kept
        if self.position.x + ballRadius > 3:
            self.stepBack()
            Nn = V(-1, 0, 0)
            rNn = Nn.rotate((0.5-random())*WALL_RANDOM_FACTOR*2)
            speed_kept = 1 - .2 * abs(self.velocity() * rNn)
            self.velocity += 2 * rNn * abs(self.velocity * rNn) * speed_kept
        if self.position.y + ballRadius > 6:
            self.stepBack()
            Nn = V(0, -1, 0)
            rNn = Nn.rotate((0.5-random())*WALL_RANDOM_FACTOR*2)
            speed_kept = 1 - .2 * abs(self.velocity() * rNn)
            self.velocity += 2 * rNn * abs(self.velocity * rNn) * speed_kept
        if self.position.y - ballRadius < 0:
            self.stepBack()
            Nn = V(0, 1, 0)
            rNn = Nn.rotate((0.5-random())*WALL_RANDOM_FACTOR*2)
            speed_kept = 1 - .2 * abs(self.velocity() * rNn)
            self.velocity += 2 * rNn * abs(self.velocity * rNn) * speed_kept
        if ((self.position + self.velocity * self.dt).x > 1.5 and (self.position.x < 1.5)) and self.position.y < 3:
            # collision from the left
            Nn = V(-1, 0, 0)
            rNn = Nn.rotate((0.5-random())*WALL_RANDOM_FACTOR*2)
            speed_kept = 1 - .2 * abs(self.velocity() * rNn)
            self.velocity += 2 * rNn * abs(self.velocity * rNn) * speed_kept
        if ((self.position + self.velocity * self.dt).x < 1.5 and (self.position.x > 1.5)) and self.position.y < 3:
            # collision from the right
            Nn = V(1, 0, 0)
            rNn = Nn.rotate((0.5-random())*WALL_RANDOM_FACTOR*2)
            speed_kept = 1 - .2 * abs(self.velocity() * rNn)
            self.velocity += 2 * rNn * abs(self.velocity * rNn) * speed_kept

    def update(self):
        if self.dead:
            return    
        
        forces = (-.015 * self.velocity)

        self.collision()

        p, v = tick(forces, self.mass, self.velocity, self.position, self.dt)
        self.velocity = v
        self.position = p
                
        self.tT += self.dt
                
        if self.velocity.m <= 0.005 or self.tT > 120:
            self.dead = True
            self.dt = 0
            self.setColor(color_rgb(126, 140, 1))
            return True
        else: 
            return False
        
    def display(self):
        self.sphere.move(self.velocity.x * self.dt, self.velocity.y * self.dt)
        
    def __call__(self):
        died = self.update()
        self.display()
        return died
    
    def setColor(self, color):
        self.sphere.undraw()
        # self.sphere.setFill(color)
        # self.sphere.draw(WindowSingleton()())
        
    def getScore(self):
        if self.position.x > 1.5 and self.position.y < 3:
            return self.position - holePosition + V(5, 0, 0)
        if self.position.x > 1.5:
            return self.position - holePosition + V(1, 0, 0)
        return self.position - holePosition

    def __del__(self):
        self.sphere.undraw()
