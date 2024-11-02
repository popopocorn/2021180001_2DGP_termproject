from pico2d import *



class Mano:
    def __init__(self):
        self.x=600
        self.y=50
        self.hp=300
        self.idle_motion =[load_image("idle"+str(i)+".png") for i in range(6)]
        self.skill_motion=[load_image("skill"+str(i)+".png") for i in range(10)]

    def update(self):
        pass
    def hadle_event(self):
        pass
    def draw(self):
        pass