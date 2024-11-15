from pico2d import *
from monster_state import *
import game_framework


TIME_PER_ACTION = [1.0, 1.0]
ACTION_PER_TIME = [1.0/i for i in TIME_PER_ACTION]
FRAMES_PER_ACTION = [8, 10] # walk, idle

class Idle:
    @staticmethod
    def enter(mano, e):
        mano.frame=0
    @staticmethod
    def exit(mano, e):
        pass
    @staticmethod
    def do(mano):
        mano.frame = (mano.frame + FRAMES_PER_ACTION[0]*ACTION_PER_TIME[0] * game_framework.frame_time)%FRAMES_PER_ACTION[0]
    @staticmethod
    def draw(mano):
        if mano.direction == 'r':
            mano.idle_motion[int(mano.frame)].draw(mano.x, mano.y + 31, 150, 150)
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
        self.run_speed = ((2.5 * 1000) / 3600) * 10 / 0.3
        self.hp=300
        self.idle_motion =[load_image("mano_idle"+str(i)+".png") for i in range(8)]
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