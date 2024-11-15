from pico2d import *
import game_framework

TIME_PER_ACTION = [0.68]
ACTION_PER_TIME = [1.0/i for i in TIME_PER_ACTION]
FRAMES_PER_ACTION = [15] # walk, idle

aura_blade_y = [0, 0, -12, 15, 15]
aura_blade_x = [0, -30, -30, -0, 0]



class Aura_blade:
    def __init__(self, x, y):
        self.image =[load_image("aura_blade_effect" + str(i)+".png" for i in range(15))]
        self.frame=0
    def draw(self):
        pass
    def update(self):
        pass

class aura:
    def __init__(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass
