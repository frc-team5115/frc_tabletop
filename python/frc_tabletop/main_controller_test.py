#!/usr/bin/python
#
#

"""
FRC robot sim
Team 5115 - Knight Riders

Author: Joe Adams
 Email: joseph.s.adams@gmail.com
   URL: git@github.com:frc-team5115/frc_tabletop.git

version: 3

yy/mm/dd
19/01/11 - multiple keymaps now working



"""

import pygame, sys
from pygame.locals import *
from colors import *
from keymaps import *

import pygame
from robot import Robot
from cargo_ship import Cargo_ship
from rocket import Rocket
from wall import Wall


from hab_platform_level_0 import Hab_platform_level_0
from hab_platform_level_1 import Hab_platform_level_1
from hab_platform_level_2 import Hab_platform_level_2
from hab_platform_level_3 import Hab_platform_level_3
from depot import Depot
from loading_station import LoadingStation

from colors import *
from units import *


class Game:

    def __init__(self):
        self.verbosity=10
        
        ##############################################
        #field_width=230*in_*3
        #field_height=133*in_*3

        self.field_width=54*ft_;
        self.field_height=27*ft_;

        self.hab_line_x=94.3*in_;
        # Call this function so the Pygame library can initialize itself
        pygame.init()
        pygame.joystick.init()

        self.joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

        for joystick in self.joysticks:
            joystick.init()
            

        

        # Create an 800x600 sized screen
        #screen_size=[800,600]

        screen_size=[self.field_width,int(self.field_height*1.20)]
        self.screen = pygame.display.set_mode(screen_size,pygame.RESIZABLE)
    
        # Set the title of the window
        pygame.display.set_caption('Test')


    
        
        
        max_x=self.field_width;
        max_y=self.field_height;

        min_x=0
        min_y=0
        mid_x=max_x/2.0
        mid_y=max_y/2.0


        wall_thickness=1*in_
        
        wall_1=Wall(min_x,min_y,width=self.field_width,height=wall_thickness,color=BLACK)
        wall_2=Wall(min_x,max_y,width=self.field_width,height=wall_thickness,color=BLACK)

        wall_3=Wall(min_x,min_y,width=wall_thickness,height=self.field_height,color=BLACK)
        wall_4=Wall(max_x,min_y,width=wall_thickness,height=self.field_height,color=BLACK)

        ############################################
        #  Robot starting points
        #

        blue_x=min_x+5*ft_
        blue_y1=mid_y
        blue_y2=blue_y1+5*ft_
        blue_y3=blue_y1-5*ft_

        red_x=max_x-5*ft_
        red_y1=blue_y1
        red_y2=blue_y2
        red_y3=blue_y3
        




        # Create the robot object

        #
        #
        #
        self.robot1 = Robot(x=blue_x, y=blue_y1, color=BLUE1, angle=-90,keymap=key_map_1, joystick=joystick_1,is_mecanum=True,mecanum_control_is_in_field_frame=False,team_name=5115,width=27*in_,length=45*in_)
        self.robot2 = Robot(x=blue_x, y=blue_y2, color=BLUE2, angle=0,keymap=key_map_2, joystick=joystick_2,is_mecanum=False,team_name=493,width=27*in_,length=55*in_)
        self.robot3 = Robot(x=blue_x, y=blue_y3, color=BLUE3, angle=180,keymap=key_map_3, joystick=joystick_3,is_mecanum=False,team_name=503,width=45*in_,length=45*in_)


        self.robot4 = Robot(x=red_x, y=red_y1,color=RED1,angle=90,keymap=key_map_4,joystick=joystick_4,is_mecanum=True,team_name=3361,width=27*in_,length=45*in_)
        self.robot5 = Robot(x=red_x, y=red_y2,color=RED2,angle=90,keymap=key_map_5,joystick=joystick_5,is_mecanum=False,team_name=3258,width=27*in_,length=45*in_)
        self.robot6 = Robot(x=red_x, y=red_y3,color=RED3,angle=90,keymap=key_map_6,joystick=joystick_6,is_mecanum=False,team_name=2106,width=27*in_,length=45*in_)


#        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.OrderedUpdates()

     
        self.all_sprites_list.add(wall_1)
        self.all_sprites_list.add(wall_2)
        self.all_sprites_list.add(wall_3)
        self.all_sprites_list.add(wall_4)
        

        self.all_sprites_list.add(self.robot1)
        self.all_sprites_list.add(self.robot2)
        self.all_sprites_list.add(self.robot3)
        self.all_sprites_list.add(self.robot4)
        self.all_sprites_list.add(self.robot5)
        self.all_sprites_list.add(self.robot6)


        
        self.solid_sprites_list = pygame.sprite.Group()
    
        # self.solid_sprites_list.add(wall_1)
        # self.solid_sprites_list.add(wall_2)
        # self.solid_sprites_list.add(wall_3)
        # self.solid_sprites_list.add(wall_4)


        # self.solid_sprites_list.add(self.robot1)
        # self.solid_sprites_list.add(self.robot2)
        # self.solid_sprites_list.add(self.robot3)
        # self.solid_sprites_list.add(self.robot4)
        # self.solid_sprites_list.add(self.robot5)
        # self.solid_sprites_list.add(self.robot6)

        self.robots_list = pygame.sprite.Group()
        self.robots_list.add(self.robot1)
        self.robots_list.add(self.robot2)
        self.robots_list.add(self.robot3)
        self.robots_list.add(self.robot4)
        self.robots_list.add(self.robot5)
        self.robots_list.add(self.robot6)

        
        self.clock = pygame.time.Clock()



    def redraw_screen(self):
        

        max_x=self.field_width;
        max_y=self.field_height;

        min_x=0
        min_y=0
        mid_x=max_x/2.0
        mid_y=max_y/2.0

        line_width=2*in_

        # draw on the surface object
        self.screen.fill(WHITE)
        pygame.draw.polygon(self.screen, GREY, ((min_x,min_y), (max_x, min_y), (max_x,max_y), (min_x,max_y), (0, 0)))
        

        pygame.draw.line(self.screen, YELLOW, (min_x, mid_y), (max_x, mid_y), line_width)

        # pygame.draw.line(self.screen, BLUE, (self.hab_line_x, min_y), (self.hab_line_x, max_y), line_width)
        # pygame.draw.line(self.screen, RED, (max_x-self.hab_line_x, min_y), (max_x-self.hab_line_x, max_y), line_width)

        # dx=9*in_
        # mid_blue_x=mid_x-dx
        # mid_red_x=mid_x+dx
        
        # pygame.draw.line(self.screen, BLUE, (mid_blue_x, min_y), (mid_blue_x, max_y), line_width)
        # pygame.draw.line(self.screen, RED, (mid_red_x, min_y), (mid_red_x, max_y), line_width)

     

        
    def run(self):
        d_angle=3
        d_speed=3
        done=False
        
        while not done:

            for event in pygame.event.get():
                if self.verbosity>0:
                    print ("n_joysticks", pygame.joystick.get_count())
                    print ("event.type", event.type)


                    #JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
                    print ("event.type", event.type),
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


                    
                    for joystick in self.joysticks:
                        print ("get_hat(0)", joystick.get_hat(0))

                        for i in range(joystick.get_numaxes()):
                            print ("get_axis(",i,")=",joystick.get_axis(i))






                
                if event.type == pygame.QUIT:
                    done = True

                # elif event.type == pygame.VIDEORESIZE:
                #     old_surface_saved = surface
                #     surface = pygame.display.set_mode((event.w, event.h),
                #                                       pygame.RESIZABLE)
                #     # On the next line, if only part of the window
                #     # needs to be copied, there's some other options.
                #     surface.blit(old_surface_saved, (0,0))
                #     del old_surface_saved                     

                elif event.type == pygame.KEYDOWN:
                    for robot in self.robots_list:
                        robot.process_event(event)

                elif event.type == pygame.KEYUP:
                    for robot in self.robots_list:
                        robot.process_event(event)
                        
                elif event.type == pygame.JOYBUTTONDOWN:
                    for robot in self.robots_list:
                        robot.process_joystick_event(event)

                elif event.type == pygame.JOYBUTTONUP:
                    for robot in self.robots_list:
                        robot.process_joystick_event(event)

                elif event.type == pygame.JOYAXISMOTION:
                    for robot in self.robots_list:
                        robot.process_joystick_event(event)

            for robot in self.robots_list:
                robot.update(self.solid_sprites_list)
            # This actually moves the robot block based on the current speed
            #self.robot1.update(self.solid_sprites_list)
            #self.robot2.update()
            #self.robot3.update()
            #self.robot4.update()
            #self.robot5.update()
            #self.robot6.update()

            # -- Draw everything
            # Clear self.screen
            #self.screen.fill(WHITE)
            self.redraw_screen()

            # Draw sprites
            self.all_sprites_list.draw(self.screen)

            # Flip screen
            pygame.display.flip()

            # Pause
            self.clock.tick(60)

            #if self.robot1.is_collided_with(self.robot2):
            #    print "COLLISION"

        pygame.quit()

if __name__ == '__main__':

    the_game=Game()
    the_game.run();
    

