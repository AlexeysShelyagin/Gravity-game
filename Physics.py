import numpy as np

from Entities import *
from Config import *

def gravity_interraction(body1: phys_body, body2: phys_body):
    dx = body2.pos.x - body1.pos.x
    dy = body2.pos.y - body1.pos.y
    m1 = body1.mass
    m2 = body2.mass

    l2 = dx**2 + dy**2
    F = G * m1 * m2 / l2

    if dx != 0:
        ang = np.arctan(dy / dx)
    else:
        ang = np.pi / 2
    if dx < 0:
        ang += np.pi

    Fx = F*np.cos(ang)
    Fy = F*np.sin(ang)

    return vec2(Fx, Fy)

def motion_from_force(body: phys_body, F: vec2, dt):
    body.accel.x = F.x / body.mass
    body.accel.y = F.y / body.mass

    body.vel += body.accel * dt
    
    body.pos += body.vel * dt * 0.5

    return body

def calculate_gravity_scene(scene: phys_scene):
    for i in range(len(scene.bodies)):
        body = scene.bodies[i]
        F = vec2(0, 0)

        for inter_body in scene.fixed_bodies:
            F += gravity_interraction(body, inter_body)
        
        for j in range(len(scene.bodies)):
            if i != j:
                F += gravity_interraction(body, scene.bodies[j])
        
        scene.bodies[i] = motion_from_force(body, F, 1 / scene.frame_rate)