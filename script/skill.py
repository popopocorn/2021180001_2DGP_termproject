from pico2d import *
import game_framework

TIME_PER_ACTION = [0.68, 0.5]
ACTION_PER_TIME = [1.0/i for i in TIME_PER_ACTION]
FRAMES_PER_ACTION = [15, 6] # aura_blade, aura

aura_blade_y = [0, 0, -12, 15, 15]
aura_blade_x = [0, -30, -30, -0, 0]



class Aura_blade:
    def __init__(self, x, y):
        self.image =[load_image("aura_blade_effect (" + str(i+1)+").png") for i in range(FRAMES_PER_ACTION[0])]
        self.frame=0
        self.x=x
        self.y=y
        self.type=0
    def draw(self):
        pass
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION[self.type] * ACTION_PER_TIME[self.type] * game_framework.frame_time) / FRAMES_PER_ACTION[self.type]

class aura:
    def __init__(self, x, y):
        self.image =[load_image("aura_shoot (" + str(i+1)+").png") for i in range(FRAMES_PER_ACTION[1])]
        self.frame=0
        self.x=x
        self.y=y
    def draw(self):
        pass

    def update(self):
        pass
