from pico2d import *
from time import *
from state_machine import *


class Walk:
    @staticmethod
    def enter(player, e):
        if right_down(e) or left_up(e):
            player.direction = 'r'
            player.player_dx = 5
            player.frame = 0

    @staticmethod
    def do(player):
        player.player_x += player.player_dx
        player.frame =(player.frame+1)%4

    @staticmethod
    def draw(player):
        if player.direction == 'r':
            if not player.player_jump:
                player.walk_motion[player.frame].composite_draw(0, 'h', player.player_x, player.player_y)
            else:
                player.jump_motion.composite_draw(0, 'h', player.player_x - 25, player.player_y + 5)
        else:
            if not player.player_jump:
                player.walk_motion[player.frame].draw(player.player_x - 10, player.player_y)
            else:
                player.jump_motion.draw(player.player_x + 15, player.player_y + 5)


class Idle:
    @staticmethod
    def enter(player):
        pass

    @staticmethod
    def do(player):
        pass

    @staticmethod
    def draw(player):
        if not player.player_jump:
            if player.direction == 'r':
                player.idle_motion[player.frame].composite_draw(0, 'h', player.player_x, player.player_y)
            else:
                player.idle_motion[player.frame].draw(player.player_x - 10, player.player_y)
        else:
            if player.direction == 'r':
                player.jump_motion.composite_draw(0, 'h', player.player_x - 25, player.player_y + 5)
            else:
                player.jump_motion.draw(player.player_x + 15, player.player_y + 5)


class Player:
    def __init__(self):
        self.gravity = 3
        self.player_jump = False
        self.player_dx = 0
        self.player_dy = 0
        self.player_x = 400
        self.player_y = 50
        self.walk_motion = [load_image("walk" + str(x) + ".png") for x in range(4)]
        self.idle_motion = [load_image("idle" + str(x) + ".png") for x in range(3)]
        self.jump_motion = load_image(("jump.png"))
        self.direction = 'r'
        self.frame = 0

    def move(self):
        self.player_x += self.player_dx

    def update_jump(self):
        if self.player_jump:
            self.player_y += self.player_dy
            self.player_dy -= self.gravity  # 중력 적용

            if self.player_y <= 50:  # 바닥에 도달했을 때
                self.player_y = 50
                self.player_jump = False
                self.player_dy = 0  # 초기화


    def get_running(self):
        return self.running
