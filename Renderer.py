import pygame
import ctypes

from Entities import *
from Physics import *
from Config import *

try:
    ctypes.windll.user32.SetProcessDPIAware()
except AttributeError:
    pass

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
screen.fill(BLACK)

def render_gravity_scene(scene: phys_scene, cam: camera):
    screen.fill(BLACK)

    calculate_gravity_scene(scene)

    for obj in scene.fixed_bodies:
        pygame.draw.circle( screen, YELLOW, ( (obj.pos - cam.pos) * cam.scale ).pair(), np.ceil(obj.r*cam.scale) )
    for obj in scene.bodies:
        pygame.draw.circle( screen, GREEN, ( (obj.pos - cam.pos) * cam.scale ).pair(), np.ceil(obj.r*cam.scale) )

    pygame.display.update()