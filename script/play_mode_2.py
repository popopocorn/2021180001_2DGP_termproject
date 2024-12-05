
from pico2d import *
import random

from background import *
from player import Player
from mushmom import Mushmom
import game_world
import game_framework
import config
import game_data
# Game object class here


def handle_events():

    global player_jump, mushmom_event_time
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            config.debug_flag = not config.debug_flag
            pass
        else:
            if event.type in(SDL_KEYDOWN, SDL_KEYUP):
                player.handle_event(event) #boy에게 event 전달
    if curr_time - mushmom_event_time >= 2.0:
        mushmom.handle_events(player.get_player_location())
        mushmom_event_time = get_time()

def init():
    global player, mushmom, mushmom_event_time
    mushmom_event_time = 0
    mushmom = Mushmom()
    game_world.add_object(mushmom, 1)
    player = Player(game_data.player_info[0], game_data.player_info[1], game_data.player_info[2])
    game_world.add_object(player, 2)
    background = Background1()
    game_world.add_object(background, 0)
    platforms = [Platform(1020, 120), Platform(870, 170), Platform(720, 170), Platform(570, 170),
                 Platform(420, 170), Platform(270, 170), Platform(120, 120)]
    for platform in platforms:
        game_world.add_object(platform, 0)
    game_world.add_collision_pair("player:platform", player, None)
    for platform in platforms:
        game_world.add_collision_pair("player:platform", None, platform)
    game_world.add_collision_pair("player:mob", player, mushmom)
    game_world.add_collision_pair("skill:mob", mushmom, None)


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