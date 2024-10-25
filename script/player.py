from pico2d import *
from time import *

class Player:
    def __init__(self):
        self.player_state='idle'
        self.player_dx=0
        self.player_dy=0
        self.player_x=400
        self.player_y=50
        self.walk_motion=[load_image("walk" + str(x) + ".png") for x in range(4)]
        self.idle_motion=[load_image("idle" + str(x) +".png") for x in range(3)]
        self.direction = 'r'
        self.frame = 0
        self.running=True
    def set_flag(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.player_state = 'walking'
                    self.direction = 'r'
                    self.frame = 0
                elif event.key == SDLK_LEFT:
                    self.player_state = 'walking'
                    self.direction = 'l'
                    self.frame = 0
                elif event.key == SDLK_LALT:
                    self.player_state = 'jump'
                    self.frame = 0
                elif event.key == SDLK_ESCAPE:
                    running = False
            elif event.type == SDL_KEYUP and self.player_dy==0:
                self.player_state = 'idle'

        if self.player_dx==0 and self.player_dy==0:
            self.player_state="idle"
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

    def jump(self, frame):
        pass
    def update(self):
        if self.player_state=='idle':
            pass
        if self.player_state=='walking' and self.direction=='r':
            pass
        if self.player_state=='walking' and self.direction=='l':
            pass
        if self.player_state=='jump':
            pass
    def get_running(self):
        return self.running
def main():
    running = True
    open_canvas(800,600,sync=True)


    player=Player()
    while player.get_running:
        player.set_flag()
        ''' if(player.get_flag()=='idle'):
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
                frame = (frame+1)%4'''
        delay(0.05)
    close_canvas()
if __name__ == '__main__':
    main()
