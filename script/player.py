from pico2d import *
from time import *

class Player:
    def __init__(self):
        self.player_flag='idle'
        self.player_x=400
        self.player_y=50
        self.walk_motion=[load_image("walk" + str(x) + ".png") for x in range(4)]
        self.idle_motion=[load_image("idle" + str(x) +".png") for x in range(3)]
        self.direction = 'r'
    def set_flag(self):
        global running, frame
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.player_flag = 'right'
                    self.direction = 'r'
                    frame = 0
                elif event.key == SDLK_LEFT:
                    self.player_flag = 'left'
                    self.direction = 'l'
                    frame = 0
                elif event.key == SDLK_LALT:
                    self.player_flag = 'jump'
                    frame = 0

                elif event.key == SDLK_ESCAPE:
                    running = False
            elif event.type == SDL_KEYUP:
                self.player_flag='idle'
                frame=0
    def play_run_animation(self, dir, frame):
        clear_canvas()
        if(dir == 'r'):
            self.walk_motion[frame].composite_draw(0, 'h', self.player_x, self.player_y)
        else:
            self.walk_motion[frame].draw(self.player_x, self.player_y)
        update_canvas()
    def play_idle_animation(self, dir, frame):
        clear_canvas()
        if (dir == 'r'):
            self.idle_motion[frame].composite_draw(0, 'h', self.player_x, self.player_y)
        else:
            self.idle_motion[frame].draw(self.player_x, self.player_y)
        update_canvas()
    def get_location(self):
        return self.player_x, self.player_y
    def move(self, dx):
        self.player_x+=dx
    def get_direction(self):
        return self.direction
    def get_flag(self):
        return self.player_flag
    def jump(self):
        pass
running = True
frame = 0
open_canvas(800,600,sync=True)


player=Player()
while running:
    player.set_flag()
    if(player.get_flag()=='idle'):
        player.play_idle_animation(player.direction, frame)
    elif(player.get_flag()=='left'):
        player.play_run_animation(player.get_direction(), frame)
        if player.get_location()[0]>32:
            player.move(-10)
    elif(player.get_flag()=='right'):
        player.play_run_animation(player.get_direction(), frame)
        if player.get_location()[0]<768:
            player.move(10)
    if (player.get_flag()=='idle'):
        frame = (frame+1)%3
    else:
        frame = (frame+1)%4
    delay(0.05)