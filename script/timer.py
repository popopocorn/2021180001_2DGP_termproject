from pico2d import *
from monster_state import *
import game_framework
from script.state_machine import time_out
from config import *
import game_world

TIME_PER_ACTION = [1.0, 1.0, 1.5]
ACTION_PER_TIME = [1.0/i for i in TIME_PER_ACTION]
FRAMES_PER_ACTION = [4, 5 ,10] # idle, walk, skill
Action_y = [0, 0, 0, 20, 30, 30, 20, 0, 0]
class Idle:
    @staticmethod
    def enter(mob, e):
        mob.start_time = get_time()
        mob.frame=0
    @staticmethod
    def exit(mob, e):
        pass
    @staticmethod
    def do(mob):
        mob.frame = (mob.frame + FRAMES_PER_ACTION[0]*ACTION_PER_TIME[0] * game_framework.frame_time)%FRAMES_PER_ACTION[0]
        if get_time() - mob.start_time> 1:
            mob.state_machine.add_event(("TIME_OUT", (0, 0)))

    @staticmethod
    def draw(mob):
        if mob.direction == 'r':
            mob.idle_motion[int(mob.frame)].draw(mob.x, mob.y + 31, 150, 150)
        else:
            mob.idle_motion[int(mob.frame)].composite_draw(0, 'h', mob.x, mob.y + 31, 150, 150)


class Trace():
    @staticmethod
    def enter(mob, e):

        mob.state_machine.add_event(e)
        mob.frame=0
        mob.start_time = get_time()

    @staticmethod
    def exit(mob, e):
        pass

    @staticmethod
    def do(mob):
        mob.frame = (mob.frame + FRAMES_PER_ACTION[1]*ACTION_PER_TIME[1] * game_framework.frame_time)%FRAMES_PER_ACTION[1]
        if get_time() - mob.start_time > 3:
            mob.state_machine.add_event(("TIME_OUT", (0, 0)))
        mob.x += mob.dx * mob.run_speed * game_framework.frame_time

    @staticmethod
    def draw(mob):
        if mob.direction == 'l':
            mob.move_motion[int(mob.frame)].composite_draw(0, 'h', mob.x, mob.y + 31 + Action_y[int(mob.frame)], 150, 150)
        else:
            mob.move_motion[int(mob.frame)].draw(mob.x, mob.y + 31 + Action_y[int(mob.frame)], 150, 150)

class Attack():
    @staticmethod
    def enter(mob, e):
        mob.frame=0
        mob.start_time = get_time()
        mob.attack=False
    @staticmethod
    def exit(mob, e):
        mob.start_time=0

    @staticmethod
    def do(mob):
        mob.frame = (mob.frame + FRAMES_PER_ACTION[2] * ACTION_PER_TIME[2] * game_framework.frame_time) % \
                     FRAMES_PER_ACTION[2]
        if mob.frame > 8 and not mob.attack:
            mob_skill=mob_atatck(mob.x, mob.y)
            game_world.add_object(mob_skill, 3)
            game_world.add_collision_pair("player:mob", None, mob_skill)
            mob.attack=True
        if mob.frame >= FRAMES_PER_ACTION[2] -1 :
            mob.state_machine.add_event(("DONE", (0, 0)))

    @staticmethod
    def draw(mob):
        if mob.direction == 'l':
            mob.skill_motion[int(mob.frame)].composite_draw(0, 'h', mob.x, mob.y + 31 + Action_y[int(mob.frame)], 150, 150)
        else:
            mob.skill_motion[int(mob.frame)].draw(mob.x, mob.y + 31 + Action_y[int(mob.frame)], 150, 150)


class Timer:
    def __init__(self):
        self.font = load_font(font, 30)

        self.x=600
        self.y=115+up
        self.run_speed = ((5 * 1000) / 3600) * 10 / 0.3
        self.hp = 3000
        self.damage=200

        self.is_mush = False
        self.attack=False

        self.delay=0

        self.idle_motion =[load_image("resource\\mushmom_idle ("+str(i+1)+").png") for i in range(FRAMES_PER_ACTION[0])]
        self.move_motion = [load_image("resource\\mushmom_move (" + str(i+1) + ").png") for i in range(FRAMES_PER_ACTION[1])]
        self.skill_motion=[load_image("resource\\mushmom_attack ("+str(i+1)+").png") for i in range(FRAMES_PER_ACTION[2])]
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
        self.font.draw(self.x - 50, self.y + 120, str(self.hp), (255, 255, 255))
        self.state_machine.draw()
        if debug_flag:
            draw_rectangle(*self.get_bb())

    def handle_collision(self, group, other):
        if group =="skill:mob":
            if not other.is_hit:
                print("na")
                self.hp -= other.damage

class mob_atatck:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_mush=True
        self.is_hit = False
        self.start_time=get_time()
        self.damage = 350
    def draw(self):
        if debug_flag:
            draw_rectangle(*self.get_bb())

    def update(self):
        if get_time() - self.start_time>0.1:
            game_world.remove_object(self)
    def get_bb(self):
        # fill here
        return self.x -350, self.y -150, self.x +350, self.y+150

    def handle_collision(self, group, other):
        if group == "player.mob":
            self.is_hit = True

