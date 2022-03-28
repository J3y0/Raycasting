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
light = source.create_source(2, 100,300)

# Defining the walls of the scene
walls = []

# First, making the sides of the window as walls
walls.append(wall.Wall(0,0,0,SIZE_WINDOW))
walls.append(wall.Wall(0,0,SIZE_WINDOW,0))
walls.append(wall.Wall(SIZE_WINDOW,0,SIZE_WINDOW,SIZE_WINDOW))
walls.append(wall.Wall(0,SIZE_WINDOW,SIZE_WINDOW,SIZE_WINDOW))

for i in range(3):
    walls.append(wall.Wall())
    walls[-1].rand_coord(SIZE_WINDOW)

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
