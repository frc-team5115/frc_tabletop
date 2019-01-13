import pygame
import copy
from pygame.math import Vector2


# the rect element is used to blit the sprite

class RobotChassis(pygame.sprite.Sprite):
    def __init__(self, x, y, angle,is_macanum=True):
        self.position= Vector2(x,y)
        self.heading= Vector2(0,0)
        #self.velocity= Vector2(0,0)
        self.rotation_rate=0
        self.set_heading_angle(angle)
        self.forward_speed=0
        self.side_speed=0

        self.dt=1
        self.verbosity=0
        self.is_macanum=is_macanum
        
    def set_heading_angle(self,theta):
        self.heading.from_polar([1,theta])
                       
    def get_heading_angle(self):
        return self.heading.as_polar()[1]
        
    def changespeed(self, a_x, a_y):
        if a_y !=0:
            self.change_forward_speed(a_y)
        elif a_x !=0:
            self.change_side_speed(a_x)        

    def change_forward_speed(self, dv):
        self.forward_speed+=dv

    def change_side_speed(self, dv):
        if self.is_macanum:
            self.side_speed+=dv

    def rotate(self,delta_angle):
        self.rotation_rate+=delta_angle
  
    def update_base(self):
        
   
        theta=self.get_heading_angle()

        velocity=Vector2(self.side_speed,self.forward_speed)
        velocity.rotate_ip(-theta)

        #self.heading.from_polar([1,theta])

        
        ##### let's put in maxium speed

        [speed,direction]=velocity.as_polar()

        self.max_speed=2
        if speed > self.max_speed:
            velocity.from_polar([self.max_speed,direction])

        

        
        self.position = self.position+self.dt*velocity

        delta_angle=self.rotation_rate*self.dt
        self.heading.rotate_ip(delta_angle)


   
        
        
        #if self.verbosity > 5:
        #    print "center=",self.position,
        #    print "delta_angle=",delta_angle,
        #    print "heading_angle=",self.get_heading_angle()

 
