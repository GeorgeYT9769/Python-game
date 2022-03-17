from turtle import Screen
from ursina import *

app = Ursina()
player = Entity(model='cube', collider='box', origin_y=-.5, color=color.blue, scale = Vec3(0.7,0.7,0.7))
trigger_box2 = Entity(model='wireframe_cube', color=color.gray, scale=2, collider='box', position=Vec3(3,-1,0), origin_y=-.5)
trigger_box = Entity(model='wireframe_cube', color=color.gray, scale=2, collider='box', position=Vec3(-3,-1,0), origin_y=-.5)
EditorCamera()


def update():
    player.x += held_keys["d"] * 0.1
    player.x -= held_keys["a"] * 0.1
    player.y += held_keys["w"] * 0.1
    player.y -= held_keys["s"] * 0.1
    player.rotation_y += held_keys["r"] * 3
    player.rotation_y -= held_keys["t"] * 3

    if player.intersects(trigger_box2).hit:
        trigger_box2.color = color.red
    else:
        trigger_box2.color = color.lime
    
    if player.intersects(trigger_box).hit:
        trigger_box.color = color.red
    else:
        trigger_box.color = color.lime
window.title = 'George YT9769'                # The window title
window.borderless = False               # Show a border
window.fullscreen = True               # Go Fullscreen
window.exit_button.visible = True      # Show the in-game red X that loses the window
window.fps_counter.enabled = True       # Show the FPS (Frames per second) counter

app.run()