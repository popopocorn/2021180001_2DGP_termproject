
from pico2d import *
import random

from background import *
from player import Player
from mushmom import Mushmom
import game_world
import game_framework

# Game object class here


def handle_events():

    global player_jump
    player_jump = player.get_jump()
    events = get_events()
    curr_time=get_time()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            pass

        else:
            if event.type in(SDL_KEYDOWN, SDL_KEYUP):
                player.handle_event(event) #boy에게 event 전달

def init():
    global player
    player = Player()
    game_world.add_object(player, 2)
    background = CaveGround()
    game_world.add_object(background, 0)
    platforms = [CavePlatform(1020, 120), CavePlatform(870, 170), CavePlatform(720, 170), CavePlatform(570, 170),
                 CavePlatform(420, 170), CavePlatform(270, 170), CavePlatform(120, 120)]
    for platform in platforms:
        game_world.add_object(platform, 0)
    game_world.add_collision_pair("player:platform", player, None)
    for platform in platforms:
        game_world.add_collision_pair("player:platform", None, platform)



def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    game_world.clear()

def update():
    game_world.update()
    game_world.handle_collisions()

def pause():
    pass
def resume():
    pass