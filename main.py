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

pg.mouse.set_visible(False)

# clock
clock = pg.time.Clock()

# My objects
light = source.create_source(5, 100,300)
wall1 = wall.Wall(300,400,300,500)
wall2 = wall.Wall(600,200,500,500)
walls = [wall1, wall2]

while True:
    
    # For now, the ray is following the mouse
    for event in pg.event.get():
        if event.type == pg.MOUSEMOTION:
            light.update_pos(pg.mouse.get_pos())
    
    for rays in light.list_rays:
        # We init at False each new frame 
        rays.hitting_wall = False
        for elt in walls:
            pt = rays.intersect(elt)
            rays.update_dir(pt)

    source.refresh(window, clock, walls, light)

pg.quit()
