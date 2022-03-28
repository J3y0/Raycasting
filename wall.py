import random as rd
import pygame as pg
import time


class Wall(object):
    
    def __init__(self, xstart = 0, ystart = 0, xend = 0, yend = 0, width = 2, color = (255,255,255)):
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

    def rand_coord(self, SIZE_WINDOW):
        xstart = rd.randint(SIZE_WINDOW/10,SIZE_WINDOW-SIZE_WINDOW/10)
        ystart = rd.randint(SIZE_WINDOW/10,SIZE_WINDOW-SIZE_WINDOW/10)

        xend = rd.randint(SIZE_WINDOW/10,SIZE_WINDOW-SIZE_WINDOW/10)
        yend = rd.randint(SIZE_WINDOW/10,SIZE_WINDOW-SIZE_WINDOW/10)
        self.coordstart = (xstart, ystart)
        self.coordend = (xend, yend)



if __name__ == "__main__":
    SIZE_WINDOW = 900
    wall1 = Wall(100,200,100,600)
    wall2 = Wall(200,200,200,200)
    wall3 = Wall(300,300,300,300)

    walls = [wall1, wall2, wall3]

    wall1.rand_coord(SIZE_WINDOW)
    wall2.rand_coord(SIZE_WINDOW)
    wall3.rand_coord(SIZE_WINDOW)

    # Fenêtre 
    window = pg.display.set_mode((SIZE_WINDOW, SIZE_WINDOW))
    pg.display.set_caption("2D Raycasting")
    window.fill((0,0,0))
    
    for elt in walls:
        elt.draw(window)

    
    pg.display.update()
    time.sleep(5)
    pg.quit()
