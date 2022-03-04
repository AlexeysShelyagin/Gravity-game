from Config import *


class vec2 (object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __add__ (self, v2):
        return vec2(self.x + v2.x, self.y + v2.y)
    def __sub__ (self, v2):
        return vec2(self.x - v2.x, self.y - v2.y)
    def __mul__ (self, val):
        return vec2(self.x*val, self.y*val)
    def __rmul__ (self, val):
        return vec2(self.x*val, self.y*val)
    
    def pair (self):
        return (self.x, self.y)

class phys_body (object):
    def __init__(self, pos = vec2(), accel = vec2(), vel = vec2(), mass = 0.0, r = 1.0):
        self.pos = pos
        self.accel = accel
        self.vel = vel
        self.mass = mass
        self.r = r

class phys_scene (object):
    def __init__(self, bodies = [], fixed_bodies = [], frame_rate = 60):
        self.bodies = bodies
        self.fixed_bodies = fixed_bodies
        self.frame_rate = frame_rate
    
    def add_fixed_body(self, body: phys_body):
        self.fixed_bodies.append(body)
    
    def add_body(self, body: phys_body):
        self.bodies.append(body)

class camera (object):
    def __init__(self, pos = vec2(), scale = SCALE, ratio = ASPECT_RATIO):
        self.pos = pos
        self.scale = scale
        self.aspect_ratio = ratio