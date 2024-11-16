from pico2d import *
from monster_state import *
import game_framework
from script.state_machine import time_out
from config import debug_flag

TIME_PER_ACTION = [1.0, 1.0, 1.0]
ACTION_PER_TIME = [1.0/i for i in TIME_PER_ACTION]
FRAMES_PER_ACTION = [8, 6 ,10] # idle, walk, skill

class Idle:
    @staticmethod
    def enter(mano, e):
        mano.start_time = get_time()
        mano.frame=0
    @staticmethod
    def exit(mano, e):
        pass
    @staticmethod
    def do(mano):
        mano.frame = (mano.frame + FRAMES_PER_ACTION[0]*ACTION_PER_TIME[0] * game_framework.frame_time)%FRAMES_PER_ACTION[0]
        if get_time() - mano.start_time> 1:
            mano.state_machine.add_event(("TIME_OUT", (0, 0)))

    @staticmethod
    def draw(mano):
        if mano.direction == 'r':
            mano.idle_motion[int(mano.frame)].draw(mano.x, mano.y + 31, 150, 150)
        else:
            mano.idle_motion[int(mano.frame)].composite_draw(0, 'h', mano.x, mano.y + 31, 150, 150)


class Trace():
    @staticmethod
    def enter(mano, e):

        mano.state_machine.add_event(e)
        mano.frame=0
        mano.start_time = get_time()

    @staticmethod
    def exit(mano, e):
        pass

    @staticmethod
    def do(mano):
        mano.frame = (mano.frame + FRAMES_PER_ACTION[1]*ACTION_PER_TIME[1] * game_framework.frame_time)%FRAMES_PER_ACTION[1]
        if get_time() - mano.start_time > 3:
            mano.state_machine.add_event(("TIME_OUT", (0, 0)))
        mano.x += mano.dx * mano.run_speed * game_framework.frame_time

    @staticmethod
    def draw(mano):
        if mano.direction == 'l':
            mano.move_motion[int(mano.frame)].composite_draw(0, 'h', mano.x, mano.y + 31, 150, 150)
        else:
            mano.move_motion[int(mano.frame)].draw(mano.x, mano.y + 31, 150, 150)

class Attack():
    @staticmethod
    def enter(mano, e):
        mano.frame=0
        mano.start_time = get_time()
    @staticmethod
    def exit(mano, e):
        mano.start_time=0

    @staticmethod
    def do(mano):
        mano.frame = (mano.frame + FRAMES_PER_ACTION[2] * ACTION_PER_TIME[2] * game_framework.frame_time) % \
                     FRAMES_PER_ACTION[2]
        if mano.frame >= FRAMES_PER_ACTION[2] -1 :
            mano.state_machine.add_event(("DONE", (0, 0)))

    @staticmethod
    def draw(mano):
        if mano.direction == 'l':
            mano.skill_motion[int(mano.frame)].composite_draw(0, 'h', mano.x, mano.y + 31, 150, 150)
        else:
            mano.skill_motion[int(mano.frame)].draw(mano.x, mano.y + 31, 150, 150)


class Mano:
    def __init__(self):
        self.x=600
        self.y=65
        self.delay=0
        self.run_speed = ((5 * 1000) / 3600) * 10 / 0.3
        self.hp=300
        self.idle_motion =[load_image("mano_idle"+str(i)+".png") for i in range(8)]
        self.move_motion = [load_image("mano_move" + str(i) + ".png") for i in range(6)]
        self.skill_motion=[load_image("mano_skill"+str(i)+".png") for i in range(10)]
        self.direction = 'r'
        self.dx=0
        self.frame = 0
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Trace:{can_attack: Attack},
                Attack:{Done: Trace},
                Idle:{time_out: Trace},
            }
        )
    def update(self):
        self.state_machine.update()
    def handle_events(self, player_location):
        if player_location < self.x:
            self.direction='r'
            self.dx= -1
        else:
            self.direction='l'
            self.dx=1

        self.state_machine.add_event(('INPUT', (player_location, self.x)))

    def get_bb(self):
        return self.x -70, self.y - 50, self.x+60, self.y+55
    def draw(self):
        self.state_machine.draw()
        if debug_flag:
            draw_rectangle(*self.get_bb())