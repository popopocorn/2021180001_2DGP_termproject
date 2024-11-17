from pico2d import *
debug_flag=False

width, height =int(1600/1.5),int(900/1.2)
up=80
font = "resource\\Maplestory Light.ttf"

def change_debug():
    global debug_flag
    debug_flag = not debug_flag