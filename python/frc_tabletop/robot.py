import pygame
import copy
from colors import * 
import loader_utils
from units import *

from pygame.math import Vector2

#from robot_chassis import RobotChassis
from chassis_tank_drive import ChassisTankDrive
#from chassis_mecanum_drive import ChassisMecanumDrive

 
#####################################################################
class Robot(pygame.sprite.Sprite):

    def __init__(self, x, y,color, angle, keymap, joystick=-1, is_mecanum=False, team_name=5115, width=27*in_, length=38*in_):

        # Call the parent's constructor
        super(Robot,self).__init__()

        self.verbosity=10

        self.keymap=keymap
        self.joystick_id=joystick


        
        if True:
            self.image = pygame.Surface((width,length), pygame.SRCALPHA)
            
            self.image.fill(color)
            width=self.image.get_rect().width
            height=self.image.get_rect().width


            if is_mecanum:
                for j in range(int(height/3)):
                    for i in range(width):
                        if ((i%4==0) and (j%4==0)):
                            self.image.set_at([i,j],WHITE)
                        
            else:
                for j in range(int(height/3)):
                    for i in range(width):
                        self.image.set_at([i,j],YELLOW)

                    
            font = pygame.font.SysFont('Sans', 10)
            text = font.render(str(team_name), True, (255, 255, 255))
#            text = pygame.transform.rotate(text, angle+180)
            text = pygame.transform.rotate(text, angle+180)
#            self.image.blit(text, self.image.get_rect())
            self.image.blit(text, [0,height/2])
            
        else:
            picture = pygame.image.load('./data/playerShip1_orange.png').convert()
            self.image=pygame.transform.scale(picture, (width,length))

        self.image_original=self.image
        self.rect_original=self.image_original.get_rect()
        
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()

        if (angle==90):
            self.rect.right = x
        elif (angle==270):
            self.rect.left = x
        else:
            self.rect.centerx = x
            
        self.rect.centery = y


       # if is_mecanum:
       #    self.chassis=ChassisMecanumDrive(self.rect.x,self.rect.y,angle)
       # else:
        self.chassis=ChassisTankDrive(self.rect.x,self.rect.y,angle,is_mecanum)

        self.dt=1
        self.d_angle=3
        self.d_speed=3
        
        # self.last_position=0
        # self.last_heading=0
        # self.last_rotation_rate=0

    def change_body_velocity_keyboard(self, a_x, a_y):
        self.chassis.change_body_velocity_keyboard(a_x,a_y)

    def set_body_velocity_joystick(self, a_x, a_y):
        self.chassis.set_body_velocity_joystick(a_x,a_y)

    def rotate_keyboard(self,delta_angle):
        #self.rotation_rate+=delta_angle
        self.chassis.rotate_keyboard(delta_angle)
    def rotate_joystick(self,delta_angle):
        #self.rotation_rate+=delta_angle
        self.chassis.rotate_joystick(delta_angle)
        

        
    def update(self,all_sprites_list):

        backup_chassis=copy.deepcopy(self.chassis)
        self.update_base()
        
        for sprite in all_sprites_list:
            if self != sprite:
                if self.is_collided_with(sprite):
                    self.chassis=copy.deepcopy(backup_chassis)

        

    def store_starting_position(self):
        self.last_position=position
        self.last_heading=heading
        self.last_forward
        
    def update_base(self):        
        self.chassis.update_base()
        self.update_rect_heading_and_position()  

    def update_rect_heading_and_position(self):
        angle= self.chassis.get_heading_angle()
        rect_orig=self.image_original.get_rect()
        
        self.image = pygame.transform.rotate(self.image_original, angle)
        ### get the center from the original image
        self.rect = self.image.get_rect(center=rect_orig.center)

        #now translate the whole thing
        self.rect.move_ip(self.chassis.position.x,self.chassis.position.y)

        
    def is_collided_with(self, sprite):
        is_collided=self.rect.colliderect(sprite.rect)
        return is_collided

    def process_event(self, event):
        #key=event.dict["key"]
        key=event.key

        value=""
        #print "key=", type(key), "value=",key
        #print "pygame.K_w=", type(pygame.K_w), "value=",pygame.K_w

        
        if (key in self.keymap):
            value=self.keymap[key]
        else:
           # print "selfkeymap doesn't have the key"
            #for keys,values in self.keymap.items():
            #    print(keys)
            #    print(values)
            return
        


       # print "value=", value
        
        # Set the speed based on the key pressed
        if event.type == pygame.KEYDOWN:            
            if value == "strafe_left":
                self.change_body_velocity_keyboard(-self.d_speed, 0)
            elif value == "strafe_right":
                self.change_body_velocity_keyboard(self.d_speed, 0)
            elif value == "forward":
                self.change_body_velocity_keyboard(0, -self.d_speed)
            elif value == "backward":
                self.change_body_velocity_keyboard(0, self.d_speed)
            elif value == "rotate_left":
                self.rotate_keyboard(self.d_angle)
            elif value == "rotate_right":
                self.rotate_keyboard(-self.d_angle)

                # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if value == "strafe_left":
                self.change_body_velocity_keyboard(self.d_speed, 0)
            elif value == "strafe_right":
                self.change_body_velocity_keyboard(-self.d_speed, 0)
            elif value == "forward":
                self.change_body_velocity_keyboard(0, self.d_speed)
            elif value == "backward":
                self.change_body_velocity_keyboard(0, -self.d_speed)
            elif value == "rotate_left":
                self.rotate_keyboard(-self.d_angle)
            elif value == "rotate_right":
                self.rotate_keyboard(self.d_angle)

    def process_joystick_event(self, event):
        if self.verbosity > 0:
             print ("n_joysticks", pygame.joystick.get_count())
             print ("self.joystick_id", self.joystick_id)
             print ("event.type", event.type)
        
        n_joysticks=pygame.joystick.get_count()
        if self.joystick_id >= n_joysticks:
            return

        my_joystick=pygame.joystick.Joystick(self.joystick_id)
        if self.verbosity > 0:
             print ("n_joysticks", pygame.joystick.get_count())
             print ("event.type", event.type)

             #JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
             
             if event.type == pygame.JOYAXISMOTION:
                 print("JOYAXISMOTION")
             elif event.type == pygame.JOYAXISMOTION:
                print("JOYBALLMOTION")
             elif event.type == pygame.JOYBUTTONDOWN:
                print("JOYBUTTONDOWN")
             elif event.type == pygame.JOYBUTTONUP:
                 print("JOYBUTTONUP")
             elif event.type == pygame.JOYHATMOTION:
                 print("JOYHATMOTION")

             print ("event.type", event.type)
             print ("get_hat(0)", my_joystick.get_hat(0))

             for i in range(my_joystick.get_numaxes()):
                 print ("get_axis(",i,")=",my_joystick.get_axis(i))
          
          
            
        #              1                            1          
        #              ^                            ^       
        #              |                            |       
        # axis(0) -1 <-----> 1         axis(3) -1 <-----> 1 
        #              |                            |       
        #                                                   
        #              v                            v       
        #             -1                           -1       
        #            axis(1)                      axis(4)
        
        #print "key=", type(key), "value=",key
        #print "pygame.K_w=", type(pygame.K_w), "value=",pygame.K_w

        left_stick_x=my_joystick.get_axis(0)
        left_stick_y=my_joystick.get_axis(1)
        right_stick_x=my_joystick.get_axis(3)


        
        accel_x=round(left_stick_x,3);
        accel_y=round(left_stick_y,3);
        rotate=round(right_stick_x,3);
        self.set_body_velocity_joystick(accel_x,accel_y)

        d_angle=rotate
        self.rotate_joystick(d_angle)

