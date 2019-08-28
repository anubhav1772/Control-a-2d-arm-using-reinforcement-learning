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
    
class Viewer():
    def __init__(self, arm_info, goal_info):
        self.arm_info = arm_info
        self.goal_info = goal_info
        self.center = np.array([200, 200])
        self.height = 500
        self.width = 500 
        # self.fps = 60      
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface((self.width, self.height))     
        self.goal = pygame.draw.rect(self.background, (0, 0, 255), pygame.Rect(200, 200, 20, 20))
        
        
    
    def render(self):
        self._update_arm()
    
    def _update_arm(self):
        pygame.init()
        pygame.display.set_caption('2D Robot Simulation')
        self.background.fill((0,0,0))
        clock = pygame.time.Clock()
        
        while True:
            for event in pygame.event.get(): 
                # Check for KEYDOWN event 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit() 
            self.screen.blit(self.background, (0, 0))
            self.goal = pygame.draw.rect(self.background, (0, 0, 255), pygame.Rect(self.goal_info['x'], self.goal_info['y'], 20, 20))
            pygame.display.flip()
            clock.tick(self.fps)
        

if __name__ == '__main__':
#    env = Env()
#    while True:
#        env.render()
     Viewer(arm_info=2,goal_info={'x':240, 'y':250}).render()