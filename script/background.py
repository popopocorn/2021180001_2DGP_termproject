from pico2d import *
from config import debug_flag
class Platform:
    def __init__(self,x=1000,y=70):
        self.platform = load_image('21.png')
        self.platformxy = [x, y]
    def draw(self):
        self.platform.draw(self.platformxy[0], self.platformxy[1], 43, 50)
        self.platform.composite_draw(0, 'h', self.platformxy[0]-43, self.platformxy[1], 43, 50)
        self.platform.composite_draw(0, 'h', self.platformxy[0]-43-21.5, self.platformxy[1], 43, 50)
        if debug_flag:
            draw_rectangle(*self.get_bb())
    def update(self):
        pass
    def get_bb(self):
        return self.platformxy[0]-80, self.platformxy[1] - 20,self.platformxy[0]+15, self.platformxy[1] + 15
    def handle_collision(self, group, other):
        pass
    def not_collision(self, group, other):
        pass

class Background:
    def __init__(self):
        self.floor = load_image('19.png')
    def draw(self):
        self.floor.draw(0, -50)
        self.floor.draw(360, -50)
        self.floor.draw(720, -50)
        self.floor.draw(1080, -50)
        self.floor.draw(1440, -50)
    def update(self):
        pass
    def get_bb(self):
        pass
if __name__ == '__main__':
    open_canvas(1600, 900)
    bg=Background()
    bg.draw()
    update_canvas()
    input()