
from pico2d import *
import random

from background import *
from player import Player
import game_world
import game_framework
from timer import Timer
# Game object class here
import game_data

def handle_events():

    global player_jump, timer_event_time
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
    if curr_time - timer_event_time >= 2.0:
        timer.handle_events(player.get_player_location())
        timer_event_time = get_time()

def init():
    global player, timer, timer_event_time
    timer_event_time = 0
    player = Player(game_data.player_info[0], game_data.player_info[1], game_data.player_info[2])
    #player = Player()
    game_world.add_object(player, 2)
    timer = Timer()
    game_world.add_object(timer, 2)
    game_world.add_collision_pair("player:mob", player, timer)
    background = CaveGround()
    game_world.add_object(background, 0)
    platforms = [CavePlatform(1020, 120), CavePlatform(870, 170), CavePlatform(720, 170), CavePlatform(570, 170),
                 CavePlatform(420, 170), CavePlatform(270, 170), CavePlatform(120, 120)]
    for platform in platforms:
        game_world.add_object(platform, 0)
    game_world.add_collision_pair("player:platform", player, None)
    for platform in platforms:
        game_world.add_collision_pair("player:platform", None, platform)
    game_world.add_collision_pair("skill:mob", timer, None)


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    game_world.clear()
    game_data.player_info = [player.hp, player.mp, player.ad]

def update():
    game_world.update()
    game_world.handle_collisions()

def pause():
    pass
def resume():
    pass