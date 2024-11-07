from pico2d import *
from monster_state import *

class Idle:
    @staticmethod
    def enter(mano, e):
        mano.frame=0
    @staticmethod
    def exit(mano, e):
        pass
    @staticmethod
    def do(mano):
        mano.frame= (mano.frame+1)%6
    @staticmethod
    def draw(mano):
        if mano.direction == 'r':
            mano.idle_motion[mano.frame].draw(mano.x, mano.y)
        else:
            pass

class Move():
    @staticmethod
    def enter(mano, e):
        pass

    @staticmethod
    def exit(mano, e):
        pass

    @staticmethod
    def do(mano):
        pass

    @staticmethod
    def draw(mano):
        pass

class Attack():
    @staticmethod
    def enter(mano, e):
        pass

    @staticmethod
    def exit(mano, e):
        pass

    @staticmethod
    def do(mano):
        pass

    @staticmethod
    def draw(mano):
        pass



class Mano:
    def __init__(self):
        self.x=600
        self.y=65
        self.hp=300
        self.idle_motion =[load_image("mano_idle"+str(i)+".png") for i in range(6)]
        self.skill_motion=[load_image("mano_skill"+str(i)+".png") for i in range(10)]
        self.direction = 'r'
        self.frame = 0
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {

            }
        )
    def update(self):
        self.state_machine.update()
    def hadle_event(self, player_location):
        pass
    def draw(self):
        self.state_machine.draw()