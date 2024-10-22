from pico2d import *

class Player:
    def __init__(self):
        self.player_x=0
        self.player_y=0
        self.walking_motion = [load_image("walk" + str(x) + ".png") for x in range(4)]
    def draw(self):

        for i in range(4):
            clear_canvas()
            self.walking_motion[i].draw(400, 300)
            delay(0.1)
            update_canvas()
        
open_canvas()
player = Player()
while True:
    player.draw()