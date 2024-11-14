

from pico2d import *
import random

from grass import Grass
from boy import Boy
import game_world
import game_framework
import title_mode
import item_mode
# Game object class here


def handle_events():


    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.push_mode(item_mode)

        else:
            if event.type in(SDL_KEYDOWN, SDL_KEYUP):
                boy.handle_event(event) #boy에게 event 전달


def init():
    global running
    global grass
    global team
    global boy

    running = True


    grass = Grass()
    game_world.add_object(grass, 0)
    boy = Boy()
    game_world.add_object(boy, 1)


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    game_world.clear()

def update():
    game_world.update()

def pause():
    pass
def resume():
    pass