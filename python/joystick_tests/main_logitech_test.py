import pygame

pygame.init()

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

p1 = pygame.joystick.Joystick(0)
p1.init()
clock = pygame.time.Clock()

#logitech f350 in X mode
# -- location |axis|  neg  | pos|
# 0 -> left   X    |  left | right
# 1 -> left   Y    |  up   | down
# 2 => triggers -  | right | left
# 3-> right   Y    |  up   | down
# 4->  right X     |  left | right
# (mode)  hat    left,down | up,right
# 0 a | 1 b | x 2 | y 3 | lb4 | rb 5 | ls 8, rs 9| back 6 start 7|

## axis 0 : -1 left stick left
# axis  0 : 1 left stick right
## axis 1 : -1 left stick forward
# axis  1 : 1 left stick backward

#              1                            1          
#              ^                            ^       
#              |                            |       
# axis(0) -1 <-----> 1         axis(3) -1 <-----> 1 
#              |                            |       
#                                                   
#              v                            v       
#             -1                           -1       
#            axis(1)                      axis(4)
#
#
#
# in XBOX mode --> DPAD is HAT motion
#                  ABCD are buttons
#                  LB,RB are buttons (L1,R1 in ps4 lingo)
#                  LT,RT are analog buttons and show up AXIS!   (L2,R2 in ps4 lingo)
#                  LT,RT are 0 when booted, then are -1 are lifted and 1 when pressed
#

while 1:                                        
  for event in pygame.event.get():
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
      print ("event.type", event.type)
      print ("event.type", event.type)
      print ("event.type", event.type)
      print ("get_hat(0)", p1.get_hat(0))

      for i in range(p1.get_numaxes()):
          print ("get_axis(",i,")=",p1.get_axis(i))
          
          
      clock.tick(40)

      
pygame.quit ()
