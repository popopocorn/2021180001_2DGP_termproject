from pico2d import *
import random

from mano import  Mano
from player import Player
# Game object class here


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            if event.type in(SDL_KEYDOWN, SDL_KEYUP):
                player.handle_event(event) #boy에게 event 전달

    mano.hadle_event(player.get_player_location())
def reset_world():
    global running
    global grass
    global team
    global world
    global player
    global mano
    running = True
    world = []

    mano = Mano()
    player = Player()
    world.append(player)
    world.append(mano)



def update_world():
    for o in world:
        o.update()
    pass


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.016)

# finalization code
close_canvas()
