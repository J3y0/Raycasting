import ray
import wall
import pygame as pg 
import time

SIZE_WINDOW = 900
# Fenêtre 
window = pg.display.set_mode((SIZE_WINDOW, SIZE_WINDOW))
pg.display.set_caption("2D Raycasting")
window.fill((0,0,0))

# My objects
ray1 = ray.Ray(100,300,10,0)
wall1 = wall.Wall(300,400,300,500)

while True:
    window.fill((0,0,0))
    wall1.draw(window)
    
    # For now, the ray is following the mouse
    for event in pg.event.get():
        if event.type == pg.MOUSEMOTION:
            ray1.update_dir(pg.mouse.get_pos())

    ray1.draw(window)

    time.sleep(0.005)
    pg.display.update()



time.sleep(5)
pg.quit()
