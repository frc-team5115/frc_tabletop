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
    def __init__(self, x, y, angle,is_mecanum=False,mecanum_control_is_in_field_frame=False):
        self.position= Vector2(x,y)
        self.heading= Vector2(0,0)
        self.velocity= Vector2(0,0)


        self.max_speed=4

        
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
        self.is_mecanum=is_mecanum
        self.mecanum_control_is_in_field_frame=mecanum_control_is_in_field_frame

        
        self.set_heading_angle(angle)
        
    def set_heading_angle(self,theta):
        self.heading.from_polar([1,theta])
                       
    def get_heading_angle(self):
        return self.heading.as_polar()[1]

    def set_body_velocity_joystick(self, joystick_x, joystick_y):
        
        v_x=joystick_x
        v_y=joystick_y
        
        v_joystick=Vector2(v_x,v_y)
        if (v_joystick.length()==0):
            self.velocity_body_joystick=v_joystick
            return
        
        
        ### convert full scale vector to max speed
        speed_joystick_units=v_joystick.length()

        ### stick gives between -1,1
        speed_joystick_units_max=Vector2(1,1).length()
        
        speed=speed_joystick_units/speed_joystick_units_max*self.max_speed

        v2=v_joystick.normalize()*speed
        
        if not self.is_mecanum:
            v2.x=0
            
        self.velocity_body_joystick=v2
    

    def change_body_velocity_keyboard(self, a_x, a_y):
        a=Vector2(a_x,a_y)            
        if not self.is_mecanum:
            a.x=0
        self.velocity_body_keyboard+=a*self.dt

    def rotate_keyboard(self,delta_angle):
        self.rotation_rate_keyboard-=delta_angle

    def rotate_joystick(self,x):
        self.rotation_rate_joystick=-x  

  
    def update_base(self):        
   
        theta=self.get_heading_angle()

        velocity_body=self.velocity_body_keyboard+self.velocity_body_joystick      


        ##### let's put in maxium speed

        [speed,direction]=velocity_body.as_polar()

        
        if speed > self.max_speed:
            velocity_body.from_polar([self.max_speed,direction])


        #### rotate to an intertial frame (the playing field)    
        if self.is_mecanum and self.mecanum_control_is_in_field_frame:
            self.velocity=velocity_body
        else:
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

 
