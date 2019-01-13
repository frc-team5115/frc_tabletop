import pygame
import copy
from pygame.math import Vector2
#      
#   https://en.wikipedia.org/wiki/Axes_conventions#/media/File:RPY_angles_of_cars.png     
#         
#   ##################################                  ^ y
#   #                                 #                 |  
#   #                                  #                |      
#   # back                      front   #               *---> x
#   #                                   #                 
#   #                                  #                  
#   #                                 #                 
#   ##################################                      
#                                                       z is out of page in 2D   
#              
#                                            Yaw is rotation around z                    
#                                         
#                                        
#
#
#
#
#


# the rect element is used to blit the sprite
                                                                 
class ChassisTankDrive(pygame.sprite.Sprite):
    def __init__(self, x, y, angle,is_macanum=False):
        self.position= Vector2(x,y)
        self.heading= Vector2(0,0)
        self.velocity= Vector2(0,0)




        
        self.rotation_rate_keyboard=0
        self.rotation_rate_joystick=0
        

        #self.forward_speed=0
        #self.side_speed=0
        #self.side_speed=0

        ### the "body" means in the reference frame of the robot
        ### where x+ is moving right
        ### y+ is moving forward
        self.velocity_body_keyboard=Vector2(0,0)
        self.velocity_body_joystick=Vector2(0,0)
        
        self.dt=1
        self.verbosity=0
        self.is_macanum=is_macanum


        
        self.set_heading_angle(angle)
        
    def set_heading_angle(self,theta):
        self.heading.from_polar([1,theta])
                       
    def get_heading_angle(self):
        return self.heading.as_polar()[1]

    def set_body_velocity_joystick(self, v_x, v_y):
        v2=Vector2(v_x,v_y)            
        if self.is_macanum:
            v2.y=0
        self.velocity_body_joystick=v2
    

    def change_body_velocity_keyboard(self, a_x, a_y):
        a=Vector2(a_x,a_y)            
        if not self.is_macanum:
            a.x=0
        self.velocity_body_keyboard+=a*self.dt

    def rotate_keyboard(self,delta_angle):
        self.rotation_rate_keyboard+=delta_angle

    def rotate_joystick(self,x):

        self.rotation_rate_joystick=x
        # # x=-1 --> 1
        # delta_angle=x*3
        
        # #### rotate to an intertial frame (the playing field)    
        # self.heading.rotate_ip(delta_angle)
        

  
    def update_base(self):
        
   
        theta=self.get_heading_angle()

        velocity_body=self.velocity_body_keyboard+self.velocity_body_joystick      


        ##### let's put in maxium speed

        [speed,direction]=velocity_body.as_polar()

        self.max_speed=2
        if speed > self.max_speed:
            velocity_body.from_polar([self.max_speed,direction])


        #### rotate to an intertial frame (the playing field)    
        self.velocity=velocity_body.rotate(-theta)

        
        self.position = self.position+self.dt*self.velocity

        rotation_rate=self.rotation_rate_joystick+self.rotation_rate_keyboard
        
        # self.max_rotation_rate=5
        # if rotation_rate > max_rotation_rate:
        #     rotation_rate=max_rotation_rate

        delta_angle=rotation_rate*self.dt
        self.heading.rotate_ip(delta_angle)


   
        
        
        #if self.verbosity > 5:
        #    print "center=",self.position,
        #    print "delta_angle=",delta_angle,
        #    print "heading_angle=",self.get_heading_angle()

 
