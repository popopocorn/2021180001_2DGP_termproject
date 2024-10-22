from pico2d import *



def set_flag():
    global running, player_flag, frame
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                player_flag = 'right'
                frame = 0
            elif event.key == SDLK_LEFT:
                player_flag = 'left'
                frame = 0
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            player_flag='idle'
            frame=0
def play_run_animation(dir, frame, dx, dy):
    clear_canvas()
    ground.draw(400, 300)
    player_run.clip_draw(frame*64, dir*64, 64, 64, dx, dy, 200, 200)
    update_canvas()
def play_idle_animation(frame, x, y):
    clear_canvas()
    ground.draw(400, 300)
    player_idle.clip_draw(frame*64, 256 - 64, 64, 64, x, y, 200, 200)
    update_canvas()


running = True
frame = 0
open_canvas()
player_x=800//2
player_y=600//2
player_idle = load_image('Sword_Idle_full.png')
player_run = load_image('Sword_Run_full.png')
ground = load_image('TUK_GROUND.png')
player_flag='idle'

while running:
    set_flag()
    if(player_flag=='idle'):
        play_idle_animation(frame, player_x, player_y)
    elif(player_flag=='left'):
        play_run_animation(2, frame, player_x, player_y)
        if player_x>32:
            player_x-=10
    elif(player_flag=='right'):
        play_run_animation(1, frame, player_x, player_y)
        if player_x<768:
            player_x+=10
    if (player_flag=='idle'):
        frame = (frame+1)%5
    else:
        frame = (frame+1)%8
    delay(0.05)