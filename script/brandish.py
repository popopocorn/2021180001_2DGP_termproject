from tkinter import mainloop

from pico2d import *

def play_brandish():
    ani_frame = [load_image( "brandish_effect"+str(i)+".png") for i in range(11) ]
    motion_frame = [load_image("brandish" + str(i) + ".png") for i in range(7) ]

    ani_frame[2].draw(400, 300)
    motion_frame[2].draw(470, 280)
    update_canvas()

open_canvas(800, 600)
while True:
    play_brandish()
#큰일났다 대부분의 스킬이 이펙트/모션 프레임수가 다름 스킬마다 play함수 따로 정의해서 모듈화 하고 임포트 해야할듯
