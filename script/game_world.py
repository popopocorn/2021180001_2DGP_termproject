#world =[]

#world[0]에는 백그라운드 객체 배경 등등
#world[1]에는 포그라운드 객체 위에 그려야 할 물체들
world =[ [], [], [], [] ]

def add_object(o, depth):
    world[depth].append(o)

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    print("error: remove target not exist")

def render():
    for layer in world:
        for o in layer:
            o.draw()


def update():
    for layer in world:
        for o in layer:
            o.update()

def clear():
    for layer in world:
        layer.clear()