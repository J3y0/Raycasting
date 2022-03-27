import random as rd
import pygame as pg
import time


class Wall(object):
    
    def __init__(self, xstart, ystart, xend, yend, width = 2, color = (255,255,255)):
        self.coordstart = (xstart, ystart)
        self.coordend = (xend, yend)
        self.width = width
        self.color = color

    def draw(self, window):
        pg.draw.line(
            surface = window,
            color = self.color,
            width = self.width,
            start_pos = self.coordstart,
            end_pos = self.coordend
        )

    def rand_coord(self):
        pass



if __name__ == "__main__":
    SIZE_WINDOW = 900
    wall1 = Wall(100,200,100,600)
    
    # Fenêtre 
    window = pg.display.set_mode((SIZE_WINDOW, SIZE_WINDOW))
    pg.display.set_caption("2D Raycasting")
    window.fill((0,0,0))
    
    wall1.draw(window)
    
    pg.display.update()
    time.sleep(5)
    pg.quit()
