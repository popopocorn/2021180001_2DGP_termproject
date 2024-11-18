from pico2d import *
import game_framework
import play_mode as next
from config import *

def init():
    global image
    image = load_image("resource\\back1.png")

def finish():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            else:
                game_framework.change_mode(next)



def update():
    pass

def draw():
    clear_canvas()
    image.draw(width/2, height/2)
    update_canvas()


def pause():
    pass
def resume():
    pass