import pygame as pg 
import time
import wall
from math import cos,sin

class Ray(object):
    
    def __init__(self, x, y, norm, angle, color = (255,255,255), width = 2):
        self.width = width
        self.color = color
        self.pos = (x,y)
        self.angle = angle
        self.dir = (norm*cos(angle), norm*sin(angle)) # The vector dir is normalized

    def draw(self, window):
        pg.draw.line(
            surface = window,
            width = self.width,
            color = self.color,
            start_pos = self.pos,
            end_pos = (self.pos[0] + self.dir[0], self.pos[1] + self.dir[1])
        )

    def intersect(self, wall):
        """Intersection of 2 lines"""
        x1 = self.pos[0]
        y1 = self.pos[1]
        x2 = self.pos[0] + self.dir[0]
        y2 = self.pos[1] + self.dir[1]

        x3 = wall.coordstart[0]
        y3 = wall.coordstart[1]
        x4 = wall.coordend[0]
        y4 = wall.coordend[1]

        denom = (x2 - x1)*(y4 - y3) - (x4 - x3)*(y2 - y1)

        if denom == 0:
            return 0

        t = ((x3 - x1)*(y4 - y3) - (x4 - x3)*(y3 - y1))/ denom # Coef that follows the ray half-segment
        u = ((x3 - x1)*(y2 - y1) - (y3 - y1)*(x2 - x1))/ denom # Coef that follows the wall segment
        
        if (t >= 0) and (0<=u<=1):
            pt = (x3 + u*(x4 - x3), y3 + u*(y4 - y3))
            return pt
        else:
            return 0


    def update_dir(self, coord):
        self.dir = (coord[0] - self.pos[0], coord[1] - self.pos[1])

    def update_pos(self, coord):
        self.pos = (coord[0], coord[1])



if __name__ == "__main__":
    SIZE_WINDOW = 900
    ray1 = Ray(100,100,0,10)

    # Fenêtre 
    window = pg.display.set_mode((SIZE_WINDOW, SIZE_WINDOW))
    pg.display.set_caption("2D Raycasting")
    window.fill((0,0,0))

    ray1.draw(window)
    pg.display.update()
    
    time.sleep(5)
    pg.quit()
