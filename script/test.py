from pico2d import *
from config import *


open_canvas(width, height)
image = [load_image(f"resource\\barlog_die ({i+1}).png") for i in range(3)]
i=0

while True:
    clear_canvas()
    image[i].draw(width/2, height/2)
    update_canvas()
    input()
    if i<3:
        i+=1
    else:
        i=0