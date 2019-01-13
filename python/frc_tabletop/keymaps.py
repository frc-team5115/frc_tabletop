import pygame, sys
from pygame.locals import *
from colors import *

import pygame



## joysticks start at 0 not 1
key_map_1={ pygame.K_w: "forward",
            pygame.K_s: "backward",
            pygame.K_a: "strafe_left", 
            pygame.K_d: "strafe_right",
            pygame.K_e: "rotate_right",
            pygame.K_q:  "rotate_left" }
joystick_1=0

key_map_2={ pygame.K_t: "forward",
            pygame.K_g: "backward",
            pygame.K_f: "strafe_left", 
            pygame.K_h: "strafe_right",
            pygame.K_r: "rotate_right",
            pygame.K_y:  "rotate_left" }
joystick_2=2

key_map_3={ pygame.K_i: "forward",
            pygame.K_k: "backward",
            pygame.K_j: "strafe_left", 
            pygame.K_l: "strafe_right",
            pygame.K_u: "rotate_right",
            pygame.K_o:  "rotate_left" }
joystick_3=4

key_map_4={ pygame.K_UP: "forward",
            pygame.K_DOWN: "backward",
            pygame.K_LEFT: "strafe_left", 
            pygame.K_RIGHT: "strafe_right",
            pygame.K_PAGEUP: "rotate_right",
            pygame.K_PAGEDOWN:  "rotate_left" }
joystick_4=1

key_map_5={ pygame.K_KP0: "forward",
            pygame.K_KP1: "backward",
            pygame.K_KP2: "strafe_left", 
            pygame.K_KP3: "strafe_right",
            pygame.K_KP4:  "rotate_right",
            pygame.K_KP5: "rotate_left" }
joystick_5=3

key_map_6={ pygame.K_0: "forward",
            pygame.K_1: "backward",
            pygame.K_2: "strafe_left", 
            pygame.K_3: "strafe_right",
            pygame.K_4: "rotate_right",
            pygame.K_5: "rotate_left" }
joystick_6=5

