from pico2d import *
from config import *
from random import randint

class Platform:
    def __init__(self,x=1050,y=120):
        self.platform = load_image('resource\\21.png')
        self.platformxy = [x, y+up]
    def draw(self):
        self.platform.draw(self.platformxy[0], self.platformxy[1], 43, 50)
        self.platform.composite_draw(0, 'h', self.platformxy[0]-43, self.platformxy[1], 43, 50)
        self.platform.composite_draw(0, 'h', self.platformxy[0]-43-21.5, self.platformxy[1], 43, 50)
        if debug_flag:
            draw_rectangle(*self.get_bb())
    def update(self):
        pass
    def get_bb(self):
        return self.platformxy[0]-80, self.platformxy[1] - 20,self.platformxy[0]+15, self.platformxy[1] + 55
    def handle_collision(self, group, other):
        pass
    def not_collision(self, group, other):
        pass


class Background1:
    def __init__(self):
        self.floor = load_image('resource\\19.png')
        self.back=load_image('resource\\back1.png')
    def draw(self):
        self.back.draw(int(1600/1.5)/2,int( 900/1.5)/2+up)
        self.floor.draw(0, up)
        self.floor.draw(360, up)
        self.floor.draw(720, up)
        self.floor.draw(1080, up)
        self.floor.draw(1440, up)
        if debug_flag:
            draw_rectangle(*self.get_bb())
    def update(self):
        pass
    def get_bb(self):
        return 0, 0, width, up+76



class CavePlatform:
    def __init__(self,x=width/2,y=height/2):
        self.platform = [load_image('resource\\blue_cave_platform (' + str(i+1) + ').png') for i in range(2)]
        self.platformxy = [x, y+up]
    def draw(self):
        self.platform[0].draw(self.platformxy[0], self.platformxy[1] + 10)
        self.platform[1].draw(self.platformxy[0] - 3, self.platformxy[1]-17)
        self.platform[0].draw(self.platformxy[0]-30, self.platformxy[1] + 10)
        self.platform[1].draw(self.platformxy[0] - 33, self.platformxy[1] - 17)
        self.platform[0].draw(self.platformxy[0] - 60, self.platformxy[1] + 10)
        self.platform[1].draw(self.platformxy[0] - 63, self.platformxy[1] - 17)
        if debug_flag:
            draw_rectangle(*self.get_bb())
    def update(self):
        pass
    def get_bb(self):
        return self.platformxy[0]-80, self.platformxy[1] - 20,self.platformxy[0]+15, self.platformxy[1] + 55
    def handle_collision(self, group, other):
        pass
    def not_collision(self, group, other):
        pass

class CaveGround:
    def __init__(self):
        self.ground_up=[load_image("resource\\blue_cave_base_up (1).png"), load_image("resource\\blue_cave_base_up (2).png")]
        self.ground_down = [load_image("resource\\blue_cave_base_down (" + str(i+1) + ").png") for i in range(3)]
        self.ground_bottom = [load_image("resource\\blue_cave_base_bottom (" + str(i + 1) + ").png") for i in range(2)]
        self.up_idx=[randint(0, 1)for _ in range(13)]
        self.down_idx = [randint(0, 2) for _ in range(13)]
        self.bottom_idx = [randint(0, 1) for _ in range(13)]
    def draw(self):
        for i in range(13):
            self.ground_up[self.up_idx[i]].draw(i*90, up+65, 90, 24)
            self.ground_down[self.down_idx[i]].draw(i*90, up + 23, 90, 60)
            self.ground_bottom[self.bottom_idx[i]].draw(i*90, up - 25, 90, 35)


        if debug_flag:
            draw_rectangle(*self.get_bb())
    def update(self):
        pass
    def get_bb(self):
        return 0, 0, width, up+76


class BlockPlatform:
    def __init__(self,x=width/2,y=height/2):
        self.platform = [load_image('resource\\block_platform (' + str(i+1) + ').png') for i in range(2)]
        self.platformxy = [x, y + up]
    def draw(self):
        self.platform[0].draw(self.platformxy[0] - 50, self.platformxy[1] + 10)
        self.platform[1].draw(self.platformxy[0] - 50, self.platformxy[1] - 10)
        self.platform[0].draw(self.platformxy[0] - 10, self.platformxy[1] + 10)
        self.platform[1].draw(self.platformxy[0] - 10, self.platformxy[1] - 10)

        if debug_flag:
            draw_rectangle(*self.get_bb())
    def update(self):
        pass
    def get_bb(self):
        return self.platformxy[0]-80, self.platformxy[1] - 20,self.platformxy[0]+15, self.platformxy[1] + 55
    def handle_collision(self, group, other):
        pass
    def not_collision(self, group, other):
        pass

class BlockGround:
    def __init__(self):
        self.ground_up=[load_image("resource\\blue_cave_base_up (1).png"), load_image("resource\\blue_cave_base_up (2).png")]
        self.ground_down = [load_image("resource\\blue_cave_base_down (" + str(i+1) + ").png") for i in range(3)]
        self.ground_bottom = [load_image("resource\\blue_cave_base_bottom (" + str(i + 1) + ").png") for i in range(2)]
        self.up_idx=[randint(0, 1)for _ in range(13)]
        self.down_idx = [randint(0, 2) for _ in range(13)]
        self.bottom_idx = [randint(0, 1) for _ in range(13)]
    def draw(self):
        for i in range(13):
            self.ground_up[self.up_idx[i]].draw(i*90, up+65, 90, 24)
            self.ground_down[self.down_idx[i]].draw(i*90, up + 23, 90, 60)
            self.ground_bottom[self.bottom_idx[i]].draw(i*90, up - 25, 90, 35)


        if debug_flag:
            draw_rectangle(*self.get_bb())
    def update(self):
        pass
    def get_bb(self):
        return 0, 0, width, up+76



if __name__ == '__main__':
    open_canvas(width, height)
    bg=CaveGround()
    pl=BlockPlatform()

    bg.draw()
    pl.draw()
    update_canvas()
    input()