from pico2d import *
from time import *

class Player:
    def __init__(self):
        self.gravity = 3
        self.player_state = 'idle'
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
        self.running = True

    def set_flag(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                self.running = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT and self.player_state != "skill":
                    self.player_state = 'walking'
                    self.direction = 'r'
                    self.frame = 0
                    self.player_dx = 10
                elif event.key == SDLK_LEFT and self.player_state != "skill":
                    self.player_state = 'walking'
                    self.direction = 'l'
                    self.frame = 0
                    self.player_dx = -10
                elif event.key == SDLK_LALT and self.player_state != "skill" and self.player_dy == 0:
                    self.player_jump = True
                    self.frame = 0
                    self.player_dy = 15
                elif event.key == SDLK_ESCAPE:
                    self.running = False
            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT or event.key == SDLK_LEFT:
                    self.player_dx = 0
            if self.player_dx == 0 and self.player_dy == 0 and self.player_state != "skill":
                self.player_state = "idle"
                self.frame = 0

        print(self.player_state)
    def update_run(self):
        clear_canvas()

        if self.direction == 'r':
            if not self.player_jump:
                self.walk_motion[self.frame].composite_draw(0, 'h', self.player_x, self.player_y)
            else:
                self.jump_motion.composite_draw(0, 'h', self.player_x, self.player_y)
        else:
            if not self.player_jump:
                self.walk_motion[self.frame].draw(self.player_x, self.player_y)
            else:
                self.jump_motion.draw(self.player_x, self.player_y)
        update_canvas()

    def update_idle(self):
        clear_canvas()
        if not self.player_jump:
            if self.direction == 'r':
                self.idle_motion[self.frame].composite_draw(0, 'h', self.player_x, self.player_y)
            else:
                self.idle_motion[self.frame].draw(self.player_x, self.player_y)
        else:
            if self.direction == 'r':
                self.jump_motion.composite_draw(0, 'h', self.player_x, self.player_y)
            else:
                self.jump_motion.draw(self.player_x, self.player_y)
        update_canvas()

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

    def update(self):
        if self.player_state == 'idle':
            self.update_idle()
            self.frame = (self.frame + 1) % 3
        if self.player_state == 'walking':
            self.move()
            self.update_run()
            self.frame = (self.frame + 1) % 4
        if self.player_jump:
            self.update_jump()



    def get_running(self):
        return self.running

def main():
    open_canvas(800, 600, sync=True)

    player = Player()
    while player.get_running():
        player.set_flag()
        player.update()
        delay(0.06)
    close_canvas()

if __name__ == '__main__':
    main()
