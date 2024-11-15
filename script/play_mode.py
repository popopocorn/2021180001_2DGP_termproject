

from pico2d import *
import random


from player import Player
from mano import Mano
import game_world
import game_framework

# Game object class here


def handle_events():

    global player_jump
    player_jump = player.get_jump()
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            pass
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            pass

        else:
            if event.type in(SDL_KEYDOWN, SDL_KEYUP):
                player.handle_event(event) #boy에게 event 전달
    mano.handle_events(player.get_player_location())

def init():
    global player, mano

    mano = Mano()
    game_world.add_object(mano, 1)
    player = Player()
    game_world.add_object(player, 2)


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