import ray
import wall
import pygame as pg 
import source
import time

SIZE_WINDOW = 900
# Fenêtre 
window = pg.display.set_mode((SIZE_WINDOW, SIZE_WINDOW))
pg.display.set_caption("2D Raycasting")
window.fill((0,0,0))

# clock
clock = pg.time.Clock()

# My objects
light = source.create_source(20, 100,300)
wall1 = wall.Wall(300,400,300,500)

while True:
    
    # For now, the ray is following the mouse
    for event in pg.event.get():
        if event.type == pg.MOUSEMOTION:
            light.update_pos(pg.mouse.get_pos())
    light.draw(window)

    source.refresh(window, clock, wall1, light)

time.sleep(5)
pg.quit()
