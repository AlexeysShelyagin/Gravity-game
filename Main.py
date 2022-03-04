import pygame
import time

from pygame import mouse

from Renderer import *

scene = phys_scene()
cam = camera()

body = phys_body()
body.mass = -7e15
body.r = 5
body.vel = vec2(0, 0)
body.pos = vec2(500, 300)
scene.add_fixed_body(body)

body = phys_body()
body.mass = 7e16
body.r = 5
body.vel = vec2(0, 0)
body.pos = vec2(300, 300)
scene.add_fixed_body(body)

body = phys_body()
body.mass = 7e16
body.r = 5
body.vel = vec2(0, 0)
body.pos = vec2(500, 500)
scene.add_fixed_body(body)

body = phys_body()
body.mass = -7e15
body.r = 5
body.vel = vec2(0, 0)
body.pos = vec2(300, 500)
scene.add_fixed_body(body)

body = phys_body()
body.mass = 1e2
body.r = 5
body.vel = vec2(300, 100)
body.pos = vec2(300, 400)
scene.add_body(body)

frame_start = time.time()
running = True
last_pos = None
cur_pos = vec2()

while running:
    dt = time.time() - frame_start
    if dt != 0:
        scene.frame_rate = 1 / dt
    frame_start = time.time()

    render_gravity_scene(scene, cam)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
            break
        if event.type == pygame.MOUSEWHEEL:
            if event.y != 0:
                cam.scale += 0.1*event.y
            