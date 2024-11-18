from pico2d import *
from config import *


class Player_status:
    def __init__(self):
        self.status_base=load_image("resource\\status_bar.png")
        self.mhp_bar=load_image("resource\\hpmp.png")
        self.mhp_alpha=load_image("resource\\gauge_gray.png")
        self.mhp_bar_x, mhp_bar_y=width/2, 30
        self.mhp_bar_ratio = 1.5


    def draw(self):
        self.status_base.draw(width/2 - 100, 60, 570 * 1.5, 71 * 1.5)
        self.mhp_bar.clip_draw(0, 0, 220, 31, width / 2, 30, 220*self.mhp_bar_ratio, 31*self.mhp_bar_ratio)
        self.mhp_alpha.clip_draw(0, 0, 220, 31, width / 2, 30, 220*self.mhp_bar_ratio, 31*self.mhp_bar_ratio)
    def update(self):
        pass
    def handle_events(self, player_location):
        pass
    def get_bb(self):
        return 0, 0, 0, 0
    def handle_collision(self, group, other):
        pass