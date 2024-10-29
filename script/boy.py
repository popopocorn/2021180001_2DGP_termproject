from pico2d import *
from time import *
from state_machine import *

class Idle:
    @staticmethod
    def enter(obj, e):
        obj.player_dx = 0
        obj.frame = 0
        obj.start_time = get_time()
    @staticmethod
    def exit(obj):
        pass
    @staticmethod
    def do(obj):
        obj.frame = (obj.frame + 1) % 3
    @staticmethod
    def draw(obj):
        if obj.direction == 'r':
            obj.idle_motion[obj.frame].composite_draw(0, 'h', obj.player_x, obj.player_y)
        else:
            obj.idle_motion[obj.frame].draw(obj.player_x - 10, obj.player_y)

class Walk:
    @staticmethod
    def enter(obj, e):
        if right_down(e):
            obj.player_dx = 10
            obj.direction = 'r'
        elif left_down(e):
            obj.player_dx = -10
            obj.direction = 'l'
        obj.frame = 0
    @staticmethod
    def exit(obj):
        obj.player_dx = 0
    @staticmethod
    def do(obj):
        obj.player_x += obj.player_dx
        obj.frame = (obj.frame + 1) % 4
    @staticmethod
    def draw(obj):
        if obj.direction == 'r':
            obj.walk_motion[obj.frame].composite_draw(0, 'h', obj.player_x, obj.player_y)
        else:
            obj.walk_motion[obj.frame].draw(obj.player_x - 10, obj.player_y)

class Jump:
    @staticmethod
    def enter(obj, e):
        obj.player_dy = 15
        obj.player_jump = True
    @staticmethod
    def exit(obj):
        obj.player_jump = False
        obj.player_dy = 0
    @staticmethod
    def do(obj):
        obj.player_y += obj.player_dy
        obj.player_dy -= obj.gravity
        if obj.player_y <= 50:
            obj.player_y = 50
            obj.state_machine.add_event(('LAND', 0))
    @staticmethod
    def draw(obj):
        if obj.direction == 'r':
            obj.jump_motion.composite_draw(0, 'h', obj.player_x - 25, obj.player_y + 5)
        else:
            obj.jump_motion.draw(obj.player_x + 15, obj.player_y + 5)

class Player:
    def __init__(self):
        self.gravity = 3
        self.player_x, self.player_y = 400, 50
        self.player_dx, self.player_dy = 0, 0
        self.player_jump = False
        self.direction = 'r'
        self.frame = 0
        self.walk_motion = [load_image("walk" + str(x) + ".png") for x in range(4)]
        self.idle_motion = [load_image("idle" + str(x) + ".png") for x in range(3)]
        self.jump_motion = load_image("jump.png")
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions({
            Idle: {right_down: Walk, left_down: Walk, space_down: Jump},
            Walk: {right_up: Idle, left_up: Idle, space_down: Jump},
            Jump: {('LAND', 0): Idle}
        })
    def update(self):
        self.state_machine.update()
    def draw(self):
        self.state_machine.draw()
    def handle_event(self, event):
        self.state_machine.add_event(('INPUT', event))
