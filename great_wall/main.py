from Populate import Populate
from V import V
from GNA import GNA
from WindowSingleton import WindowSingleton
from graphics import update as refresh
from graphics import Circle, Point, color_rgb, Line
from time import time
from constants import holePosition, HILL_CENTER, HILL_RADIUS, VALLEY_CENTER, VALLEY_RADIUS


def decreaseDeviationCallback(self):
    self.stdDev /= 1.1

def decreaseDtCallback(self):
    if self.epoch == 2:
        for i in self.populates:
            i.startingDt = .02
            i.dt = .02
        print("Updated dt of populates to be: " + str(self.populates[0].dt))
    if self.epoch == 4:
        for i in self.populates:
            i.startingDt = .01
            i.dt = .01
        print("Updated dt of populates to be: " + str(self.populates[0].dt))

def decreasePopulationCallback(self):
    if self.epoch == 3:
        self.familySizes = [50, 45, 30, 30, 25, 20, 20, 15, 15, 10, 10, 10, 5, 5, 5, 5]
        print("Updated family sizes for next generation to be: [50, 45, 30, 30, 25, 20, 20, 15, 15, 10, 10, 10, 5, 5, 5, 5] (sum: " 
            + str(sum(self.familySizes)) + ")")

def update():
    """ Will be called as many times as possible. """
    gna()

    return

def fixedUpdate():
    """ Will be called at most _FPS number of times per second. Put costly graphics operations in here. """
    refresh()

    return


if __name__ == '__main__':
    # DrawBG()
    WindowSingleton()
    # bg color 4, 122, 9
    WindowSingleton()().setBackground(color_rgb(4, 122, 9))

    valley = Circle(Point(VALLEY_CENTER.x, VALLEY_CENTER.y), VALLEY_RADIUS)
    valley.setFill(color_rgb(2, 189, 11))
    valley.setOutline(color_rgb(4, 122, 9))
    valley.draw(WindowSingleton()())

    hill = Circle(Point(HILL_CENTER.x, HILL_CENTER.y), HILL_RADIUS)
    hill.setFill(color_rgb(0, 148, 7))
    hill.setOutline(color_rgb(4, 122, 9))
    hill.draw(WindowSingleton()())

    straightWall = Line(Point(1,0), Point(1,2))
    straightWall.draw(WindowSingleton()())

    diagonalWall = Line(Point(1,2), Point(2,4))
    diagonalWall.draw(WindowSingleton()())

    # ball = Circle(Point(1.5, .2), .025)
    # ball.setOutline("white")
    # ball.setFill("white")
    # ball.draw(WindowSingleton()())

    hole = Circle(Point(holePosition.x, holePosition.y), .05)
    hole.setFill("black")
    hole.draw(WindowSingleton()())

    position = V(0, 0, 0)
    velocity = V(0, 0, 0)
    tT = 0
    
    epoch = 0  

    gna = GNA(.03, [70, 65, 50, 50, 45, 40, 40, 35, 35, 30, 30, 30, 25, 25, 25, 15, 15, 5, 5, 5], Populate, .03, [decreaseDeviationCallback, decreaseDtCallback, decreasePopulationCallback], False)
    print(sum(gna.familySizes))
    
    # TODO: only add drawing changes to callstack when update is about to be called
    timeSinceUpdate = time()
    _FPS = 30
    _SPF = 1/_FPS # seconds per frame refresh


    while True:
        update()

        if time() - timeSinceUpdate > _SPF:
            timeSinceUpdate = time()
            fixedUpdate()
            



        
