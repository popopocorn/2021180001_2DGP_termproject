from pico2d import *
from config import *


open_canvas(width, height)
image = [load_image("resource\\mano_skill"+str(i)+".png") for i in range(10)]
i=0

while True:
    clear_canvas()
    image[i].draw(width/2, height/2 + mano_motion_y[i])
    update_canvas()
    input()
    if i<9:
        i+=1
    else:
        i=0