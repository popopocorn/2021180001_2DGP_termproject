from pico2d import *
import game_framework
import game_world
import game_data
import config
import play_mode

def init():
    global font
    font = load_font(config.font, 20)


def finish():
    pass

def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_1:
                    game_framework.quit()
                case pico2d.SDLK_2:
                    game_data.player_info=game_data.init_player_info
                    game_data.cards=game_data.init_cards
                    game_data.enhance=game_data.init_enhance
                    game_framework.change_mode(play_mode)


def update():
    pass

def draw():
    clear_canvas()
    font.draw(config.width/2-100, config.height/2, "승리를 축하합니다", (255, 255, 255))
    font.draw(config.width / 2 - 100, config.height / 2 - 50,"다시하기: 1 종료: 2", (255, 255, 255))
    update_canvas()

def pause():
    pass
def resume():
    pass