from ray import *
import pygame as pg 
from math import cos,sin,pi


class LightSource(object):

    def __init__(self, list_rays, color = (255,255,255), width = 2):
        self.width = width
        self.color = color
        self.list_rays = list_rays


    def draw(self, window):
        for ray in self.list_rays:
            ray.draw(window)  

    def update_pos(self,coord):
        for ray in self.list_rays:
            ray.update_pos(coord)
    

def create_source(step_angle, x, y, color = (255,255,255), width = 2):
    list_rays = []
    for angle in range(0, 360, step_angle):
        angle = angle*pi/180
        ray = Ray(x, y, 10, angle, color, width)
        list_rays.append(ray)

    source = LightSource(list_rays,color, width)
    return source

def refresh(window, clock, wall, source):
    window.fill((0,0,0))
    wall.draw(window)
    
    source.draw(window)

    pg.display.update()
    clock.tick(60)
