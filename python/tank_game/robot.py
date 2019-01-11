import pygame
import copy
from colors import * 
import loader_utils

from pygame.math import Vector2
from robot_chassis import RobotChassis

 
#####################################################################
class Robot(pygame.sprite.Sprite):

    def __init__(self, x, y,color, angle, is_mecanum=False, width=15, length=38):

        # Call the parent's constructor
        super(Robot,self).__init__()

        self.verbosity=0
        

#        width=15
#        length=38

        if True:
            self.image = pygame.Surface((width,length), pygame.SRCALPHA)
            self.image.fill(color)
        else:
            picture = pygame.image.load('./data/playerShip1_orange.png')
            self.image=pygame.transform.scale(picture, (width,length))

        self.image_original=self.image
        self.rect_original=self.image_original.get_rect()
        
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        
        self.chassis=RobotChassis(x,y,angle,is_mecanum)

        self.dt=1

        # self.last_position=0
        # self.last_heading=0
        # self.last_rotation_rate=0

    def changespeed(self, a_x, a_y):
        if a_y !=0:
            self.chassis.change_forward_speed(a_y)
        elif a_x !=0:
            self.chassis.change_side_speed(a_x)        

        

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

   
        # theta=self.get_heading_angle()

        # velocity=Vector2(self.side_speed,self.forward_speed)
        # velocity.rotate_ip(-theta)
        
        # self.chassis.position = self.chassis.position+self.dt*velocity

        # delta_angle=self.rotation_rate*self.dt
        # self.chassis.heading.rotate_ip(delta_angle)

        # if self.verbosity > 5:
        #     print "center=",self.chassis.position,
        #     print "delta_angle=",delta_angle,
        #     print "heading_angle=",self.get_heading_angle()


        
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

    def rotate(self,delta_angle):
        #self.rotation_rate+=delta_angle
        self.chassis.rotate(delta_angle)
        
        
    def is_collided_with(self, sprite):
        is_collided=self.rect.colliderect(sprite.rect)
        return is_collided