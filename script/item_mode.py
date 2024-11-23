from pico2d import *
import game_framework
import play_mode as next
from config import *

def init():
    global image, notice, title
    image = load_image("resource\\back1.png")
    notice = load_font(font, 30)
    title = load_font(font, 60)

def finish():
    global image, notice, title
    del image
    del notice
    del title

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
    title.draw(width / 2 - 125, height / 2, "히어로그", (255, 255, 255))
    notice.draw(width/2-175, height/2 - 150, "Press Any Key To Start", (255, 255, 255))
    update_canvas()


def pause():
    pass
def resume():
    pass