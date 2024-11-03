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
        elif left_down(e) or right_up(e):
            player.direction = 'l'
            player.player_dx = -5
            player.frame = 0
    def exit(self):
        pass
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
                player.walk_motion[player.frame].draw(player.player_x - 25, player.player_y)
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
        player.frame = (player.frame + 1)%3

    @staticmethod
    def draw(player):
        if not player.player_jump:
            if player.direction == 'r':
                player.idle_motion[player.frame].composite_draw(0, 'h', player.player_x, player.player_y)
            else:
                player.idle_motion[player.frame].draw(player.player_x - 20, player.player_y)
        else:
            if player.direction == 'r':
                player.jump_motion.composite_draw(0, 'h', player.player_x - 25, player.player_y + 5)
            else:
                player.jump_motion.draw(player.player_x + 15, player.player_y + 5)


class Player:
    def __init__(self):
        self.hp=100
        self.gravity = 3
        self.player_jump = False
        self.player_dx = 0
        self.player_dy = 0
        self.player_x = 200
        self.player_y = 50
        self.walk_motion = [load_image("walk" + str(x) + ".png") for x in range(4)]
        self.idle_motion = [load_image("idle" + str(x) + ".png") for x in range(3)]
        self.jump_motion = load_image(("jump.png"))
        self.direction = 'r'
        self.frame = 0
        self.state_machine=StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Walk: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle},
                Idle: {right_down: Walk, left_down: Walk, left_up: Walk, right_up: Walk},
            }
        )

    def draw(self):
        self.state_machine.draw()
    def update(self):
        self.state_machine.update()
        if self.player_jump:
            self.update_jump()
    def handle_event(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_LALT and not self.player_jump:
            self.player_jump=True
            self.player_dy=20
            print(self.player_jump)
        self.state_machine.add_event(('INPUT', event))
    def get_player_location(self):
        return self.player_x
    def update_jump(self):
        if self.player_jump:
            self.player_y += self.player_dy
            self.player_dy -= self.gravity  # 중력 적용

            if self.player_y <= 50:  # 바닥에 도달했을 때
                self.player_y = 50
                self.player_jump = False
                self.player_dy = 0  # 초기화