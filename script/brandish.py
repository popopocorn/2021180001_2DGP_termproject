from tkinter import mainloop

from pico2d import *

def play_brandish():
    ani_frame = [load_image( "brandish_effect"+str(i)+".png") for i in range(11) ]
    motion_frame = [load_image("brandish" + str(i) + ".png") for i in range(7) ]
    ani_index = 0
    motion_index = 0

    ani_time_per_frame = 70  # ani_frame이 70프레임마다 한 번 변경
    motion_time_per_frame = 130  # motion_frame이 130프레임마다 한 번 변경

    for i in range(770):
        clear_canvas()

        # ani_frame 애니메이션 처리
        if i % ani_time_per_frame == 0:
            ani_index = (ani_index + 1) % len(ani_frame)
        ani_frame[ani_index].draw(400, 300)

        # motion_frame 애니메이션 처리
        if i % motion_time_per_frame == 0:
            motion_index = (motion_index + 1) % len(motion_frame)
        motion_frame[motion_index].draw(400, 300)

        update_canvas()
        delay(0.0001)

open_canvas()
while True:
    play_brandish()
#모션 잘못 추출했다.. 이펙트는 새거인데 모션은 리마스터 이전...
#메이플이 용량을 줄이려는지 구 이펙트 삭제중이라 리마스터 이후로 통일해야함
#모션 다시 구해야함 하...