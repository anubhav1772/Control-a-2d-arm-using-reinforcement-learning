# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:56:56 2019
@author: anubhav Singh
"""
import numpy as np
import pygame 
# import pygame.locals for easier  
# access to key coordinates 
from pygame.locals import *


class Env(object):
    viewer = None

    def __init__(self):
        pass

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self):
        pass

class Goal(pygame.sprite.Sprite): 
    def __init__(self, goal): 
        super(Goal, self).__init__() 
          
        # Define the dimension of the surface 
        # Here we are making squares of side goal['width']
        self.surf = pygame.Surface((goal['width'], goal['width'])) 
          
        # Define the color of the surface using RGB color coding. 
        self.surf.fill((0, 200, 255)) 
        self.rect = self.surf.get_rect() 


if __name__ == '__main__':
    env = Env()
    while True:
        env.render()