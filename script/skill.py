from pico2d import *
import game_framework
import game_world

TIME_PER_ACTION = [0.68, 0.5]
ACTION_PER_TIME = [1.0/i for i in TIME_PER_ACTION]
FRAMES_PER_ACTION = [15, 6] # aura_blade, aura

aura_blade_y = [0, 0, -12, 15, 15]
aura_blade_x = [0, -30, -30, -0, 0]



class Aura_blade:
    def __init__(self, x, y, direction):
        self.image =[load_image("resource\\aura_blade_effect (" + str(i+1)+").png") for i in range(FRAMES_PER_ACTION[0])]
        self.frame=0
        self.x=x
        self.y=y
        self.type=0
        self.direction=direction
    def draw(self):
        if self.direction == 'r':
            self.image[int(self.frame)].draw(self.x - 50, self.y)
        else:
            self.image[int(self.frame)].composite_draw(0, 'h', self.x + 50, self.y)
    def update(self):
        if self.frame<FRAMES_PER_ACTION[self.type]-1:
            self.frame = (self.frame + FRAMES_PER_ACTION[self.type] * ACTION_PER_TIME[self.type] * game_framework.frame_time)
        else:
            game_world.remove_object(self)
class Aura:
    def __init__(self, x, y, direction):
        self.image =[load_image("resource\\aura_shoot (" + str(i+1)+").png") for i in range(FRAMES_PER_ACTION[1])]
        self.frame=0
        self.x=x
        self.y=y
        self.type = 1
        self.direction = direction
        self.speed=10
        self.damage=1
    def draw(self):
        if self.direction == 'l':
            self.image[int(self.frame)].draw(self.x - 50, self.y, 480*0.6, 350*0.6)
            self.x -= self.speed * 100 * game_framework.frame_time
        else:
            self.image[int(self.frame)].composite_draw(0, 'h', self.x + 50, self.y, 480*0.6, 350*0.6)
            self.x += self.speed * 100 * game_framework.frame_time
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION[self.type] * ACTION_PER_TIME[
            self.type] * game_framework.frame_time) %FRAMES_PER_ACTION[self.type]
    def get_bb(self):
        # fill here
        if self.direction == 'r':
            return self.x +50, self.y -50, self.x+150, self.y+50
        else:
            return self.x - 150, self.y - 50, self.x - 50, self.y + 50
        pass
    def handle_collision(self, group, other):
        pass

