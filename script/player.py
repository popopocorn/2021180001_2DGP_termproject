from pico2d import *
from time import *
from state_machine import *
import game_world
import game_framework
from config import *
from skill import *

TIME_PER_ACTION = [0.5, 1.0, 0.68, 0.5]
ACTION_PER_TIME = [1.0/i for i in TIME_PER_ACTION]
FRAMES_PER_ACTION = [4, 3, 5, 7] # walk, idle

aura_blade_y = [0, 0, -12, 15, 15]
aura_blade_x = [0, -30, -30, -0, 0]

brandish_x = [-30,-30, -10, -10, -30, 0, 0]
brandish_y = [0, 0, 20, 20, 20, 10, 5]


class Walk:
    @staticmethod
    def enter(player, e):

        if right_down(e) or left_up(e):
            player.direction = 'r'
            player.player_dx = 5
            player.frame = 0
        elif left_down(e) or right_up(e):
            player.direction = 'l'
            player.player_dx = -5
            player.frame = 0
    def exit(self):
        pass
    @staticmethod
    def do(player):
        player.player_x += player.player_dx * player.run_speed * game_framework.frame_time
        player.frame = (player.frame + FRAMES_PER_ACTION[0]*ACTION_PER_TIME[0] * game_framework.frame_time)%FRAMES_PER_ACTION[0]

    @staticmethod
    def draw(player):
        if player.direction == 'r':
            if not player.player_jump:
                player.walk_motion[int(player.frame)].composite_draw(0, 'h', player.player_x + 10, player.player_y)
            else:
                player.jump_motion.composite_draw(0, 'h', player.player_x - 25, player.player_y + 5)
        else:
            if not player.player_jump:
                player.walk_motion[int(player.frame)].draw(player.player_x - 25, player.player_y)
            else:
                player.jump_motion.draw(player.player_x + 15, player.player_y + 5)


class Idle:
    @staticmethod
    def enter(player, e):
        player.frame = 0

    def exit(self):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION[1]*ACTION_PER_TIME[1] * game_framework.frame_time)%FRAMES_PER_ACTION[1]

    @staticmethod
    def draw(player):
        if not player.player_jump:
            if player.direction == 'r':
                player.idle_motion[int(player.frame)].composite_draw(0, 'h', player.player_x + 10, player.player_y)
            else:
                player.idle_motion[int(player.frame)].draw(player.player_x - 20, player.player_y)
        else:
            if player.direction == 'r':
                player.jump_motion.composite_draw(0, 'h', player.player_x - 15, player.player_y + 5)
            else:
                player.jump_motion.draw(player.player_x + 15, player.player_y + 5)


class Player:
    def __init__(self):
        self.run_speed = ((5 * 1000) / 3600) * 10 / 0.3
        self.hp=100
        self.gravity = 3
        self.player_jump = False
        self.jump_speed = ((5 * 1000) / 3600) * 10 / 0.3
        self.player_dx = 0
        self.player_dy = 0
        self.player_x = 200
        self.player_y = 106+up
        self.ground=106+up
        self.temp_xy=[0, 0, 0, 0]
        self.walk_motion = [load_image("resource\\walk" + str(x) + ".png") for x in range(4)]
        self.idle_motion = [load_image("resource\\idle" + str(x) + ".png") for x in range(3)]
        self.jump_motion = load_image(("resource\\jump.png"))

        self.skill_motion=0
        self.aura_blade_motion = [load_image("resource\\auraBlade" +str(i) +".png") for i in range(5)]
        self.brandish_motion = [load_image("resource\\brandish" + str(i)+".png") for i in range(7)]

        self.direction = 'r'
        self.frame = 0
        self.state_machine=StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Walk: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, skill_down: Skill},
                Idle: {right_down: Walk, left_down: Walk, left_up: Walk, right_up: Walk, skill_down: Skill},
                Skill: {time_out: Wait},
                Wait: {right_down: Walk, left_down: Walk},
            }
        )

    def draw(self):
        self.state_machine.draw()
        if debug_flag:
            draw_rectangle(*self.get_bb())
    def update(self):
        if(self.player_x +10 <self.temp_xy[0] or self.player_x -20 > self.temp_xy[2]):
            self.ground=106+up
        if self.player_y>self.ground:
            self.player_jump=True
        self.state_machine.update()
        if self.player_jump:
            self.update_jump(self.ground)
    def handle_event(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_LALT and not self.player_jump:
            self.player_jump=True
            self.player_dy=25
        self.state_machine.add_event(('INPUT', event))
    def get_player_location(self):
        return self.player_x

    def update_jump(self, y):
        if self.player_jump:
            # 점프 속도를 시간 프레임에 따라 계산
            self.player_y += self.player_dy * self.jump_speed * game_framework.frame_time
            self.player_dy -= self.gravity* self.jump_speed * game_framework.frame_time  # 중력 적용

            # 바닥에 도달했을 때
            if self.player_y <= y:
                self.player_y = y
                self.player_jump = False
                self.player_dy = 0  # 점프 속도 초기화
    def get_jump(self):
        return self.player_jump
    def get_bb(self):
        return self.player_x - 20, self.player_y - 35, self.player_x + 10, self.player_y + 30
        pass

    def handle_collision(self, group, other):
        self.temp_xy = other.get_bb()
        if group=="player:platform":
            if self.player_y>=self.temp_xy[3] + 30:
                self.ground=self.temp_xy[3]+30
            else:
                self.ground=106+up


class Skill:
    @staticmethod
    def enter(player, e):
        player.frame=0
        player.start_time = get_time()
        if e[1].key==SDLK_q:
            player.skill_motion = 1
            skill=Aura_blade(player.player_x, player.player_y)
            game_world.add_skill(skill)
        elif e[1].key==SDLK_w:
            player.skill_motion = 2
    def exit(self):
        pass
    @staticmethod
    def do(player):
        if player.skill_motion == 1:
            if player.frame < FRAMES_PER_ACTION[1]+1:
                player.frame = (player.frame + FRAMES_PER_ACTION[player.skill_motion + 1] * ACTION_PER_TIME[player.skill_motion + 1] * game_framework.frame_time)
            if get_time() - player.start_time >= TIME_PER_ACTION[player.skill_motion+1]:
                player.state_machine.add_event(('TIME_OUT', 0))
        if player.skill_motion == 2:
            if player.frame < FRAMES_PER_ACTION[2]+1:
                player.frame = (player.frame + FRAMES_PER_ACTION[player.skill_motion + 1] * ACTION_PER_TIME[player.skill_motion + 1] * game_framework.frame_time)
            if get_time() - player.start_time >= TIME_PER_ACTION[player.skill_motion+1]:
                player.state_machine.add_event(('TIME_OUT', 0))
    @staticmethod
    def draw(player):
        if player.skill_motion == 1:
            if player.direction == 'r':
                player.aura_blade_motion[int(player.frame)].composite_draw(0, 'h', player.player_x + aura_blade_x[int(player.frame)], player.player_y + aura_blade_y[int(player.frame)])
            else:
                player.aura_blade_motion[int(player.frame)].draw(player.player_x - 20 - aura_blade_x[int(player.frame)], player.player_y + aura_blade_y[int(player.frame)])
        elif player.skill_motion == 2:
            if player.direction == 'r':
                player.brandish_motion[int(player.frame)].composite_draw(0, 'h', player.player_x + brandish_x[int(player.frame)], player.player_y+brandish_y[int(player.frame)])
            else:
                player.brandish_motion[int(player.frame)].draw(player.player_x + brandish_x[int(player.frame)], player.player_y+brandish_y[int(player.frame)])

class Wait:
    @staticmethod
    def enter(player, e):

        player.frame = 0

    def exit(self):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION[1] * ACTION_PER_TIME[1] * game_framework.frame_time) % \
                       FRAMES_PER_ACTION[1]

    @staticmethod
    def draw(player):
        if not player.player_jump:
            if player.direction == 'r':
                player.idle_motion[int(player.frame)].composite_draw(0, 'h', player.player_x, player.player_y)
            else:
                player.idle_motion[int(player.frame)].draw(player.player_x - 20, player.player_y)
        else:
            if player.direction == 'r':
                player.jump_motion.composite_draw(0, 'h', player.player_x - 25, player.player_y + 5)
            else:
                player.jump_motion.draw(player.player_x + 15, player.player_y + 5)


