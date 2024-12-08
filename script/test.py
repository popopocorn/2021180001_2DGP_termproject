from pico2d import *
from config import *
import main_ui
from main_ui import Player_status

open_canvas(width, height)
image = [load_image(f"resource\\barlog_die ({i+1}).png") for i in range(3)]
i=0
hp = load_image("resource\\hp.png")
mp = load_image("resource\\mp.png")
gauge = load_image("resource\\gauge.png")
per = 50
ps=Player_status()
while True:
    clear_canvas()
    # image[i].draw(width/2, height/2)
    # hp.clip_draw_to_origin(0, 0, int(108 * (per/100)), 18, width / 2, height / 2)
    # gauge.clip_draw_to_origin(0, 0, 108, 18, width / 2, height / 2)
    ps.draw()
    update_canvas()
    # input()
    # if i<3:
    #     i+=1
    # else:
    #     i=0
