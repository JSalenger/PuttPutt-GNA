from Populate import Populate
from V import V
from GNA import GNA
from WindowSingleton import WindowSingleton
from graphics import update as refresh
from graphics import Circle, Point, color_rgb
from time import time
from constants import holePosition, HILL_CENTER, HILL_RADIUS, VALLEY_CENTER, VALLEY_RADIUS


def decreaseDeviationCallback(self):
    self.stdDev /= 1.1


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

    gna = GNA(.01, [70, 65, 50, 50, 45, 40, 40, 35, 35, 30, 30, 30, 25, 25, 25, 15, 15, 5, 5, 5], Populate, .03, [decreaseDeviationCallback], False)
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
            



        
