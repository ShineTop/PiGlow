################################################################
#                        Fading Fuse                           #
################################################################
# Description:                                                 #
# This program lights up arm 1, then lights up arms 2 and 3    #
# at the same time. Then lights up arm 2, which then lights    #
# up arms 1 and 3. Then lights up arm 3, which then lights     #
# up arms 1 and 2.  Then goes through the whole thing again    #
# while increasing the speed. Exactly like my "Light the Fuse" #
# program, except that the fuse fades.                         # 
#                                                              #
# Requirements: PyGlow.py                                      #
#                                                              #
# Author: Paul Ryan                                            #
#                                                              #
################################################################

from PyGlow import PyGlow
from time import sleep

pyglow = PyGlow()

# Initialize
pyglow.all(0)

# Functions
def fading_fuse_1(sleep_speed): 
    # Turn on Arm 1 Red
    pyglow.led(1,120)
    sleep(sleep_speed)
    # Turn on Arm 1 Orange
    pyglow.led(2,120)
    sleep(sleep_speed)
    # Fade Arm 1 Red
    pyglow.led(1,110)
    sleep(sleep_speed)
    # Turn on Arm 1 Yellow
    pyglow.led(3,120)
    sleep(sleep_speed)
    # Fade Arm 1 R, O
    pyglow.led(1,100)
    sleep(sleep_speed)
    pyglow.led(2,110)
    sleep(sleep_speed)
    # Turn on Arm 1 Green
    pyglow.led(4,120)
    sleep(sleep_speed)
    # Fade Arm 1 R, O, Y
    pyglow.led(1,90)
    sleep(sleep_speed)
    pyglow.led(2,100)
    sleep(sleep_speed)    
    pyglow.led(3,110)
    sleep(sleep_speed)
    # Turn on Arm 1 Blue
    pyglow.led(5,120)
    sleep(sleep_speed)
    # Fade Arm 1 R, O, Y, G
    pyglow.led(1,80)
    sleep(sleep_speed)
    pyglow.led(2,90)
    sleep(sleep_speed)    
    pyglow.led(3,100)
    sleep(sleep_speed)
    pyglow.led(4,110)
    sleep(sleep_speed)
    # Arm 1, White
    pyglow.led(6,120)
    sleep(sleep_speed)
    # Fade Arm 1 R, O, Y, G, B
    pyglow.led(1,70)
    sleep(sleep_speed)
    pyglow.led(2,80)
    sleep(sleep_speed)    
    pyglow.led(3,90)
    sleep(sleep_speed)
    pyglow.led(4,100)
    sleep(sleep_speed)
    pyglow.led(5,110)
    sleep(sleep_speed)
    # Turn on Arm 2 and 3 White
    pyglow.led(12,120)
    pyglow.led(18,120)
    sleep(sleep_speed)
    # Fade Arm 1 R, O, Y, G, B, W
    pyglow.led(1,60)
    sleep(sleep_speed)
    pyglow.led(2,70)
    sleep(sleep_speed)    
    pyglow.led(3,80)
    sleep(sleep_speed)
    pyglow.led(4,90)
    sleep(sleep_speed)
    pyglow.led(5,100)
    sleep(sleep_speed)
    pyglow.led(6,110)
    sleep(sleep_speed)
    # Turn on Arm 2 and 3 Blue
    pyglow.led(11,120)
    pyglow.led(17,120)
    sleep(sleep_speed)
    # Fade Arm 1 R, O, Y, G, B, W, Arm 2 and 3 W
    pyglow.led(1,50)
    sleep(sleep_speed)
    pyglow.led(2,60)
    sleep(sleep_speed)    
    pyglow.led(3,70)
    sleep(sleep_speed)
    pyglow.led(4,80)
    sleep(sleep_speed)
    pyglow.led(5,90)
    sleep(sleep_speed)
    pyglow.led(6,100)
    sleep(sleep_speed)
    pyglow.led(12,110)
    pyglow.led(18,110)
    sleep(sleep_speed)
    # Arm 2 and 3, Green
    pyglow.led(10,120)
    pyglow.led(16,120)
    sleep(sleep_speed)
    # Fade Arm 1 R, O, Y, G, B, W, Arm 2 and 3 W, B
    pyglow.led(1,40)
    sleep(sleep_speed)
    pyglow.led(2,50)
    sleep(sleep_speed)    
    pyglow.led(3,60)
    sleep(sleep_speed)
    pyglow.led(4,70)
    sleep(sleep_speed)
    pyglow.led(5,80)
    sleep(sleep_speed)
    pyglow.led(6,90)
    sleep(sleep_speed)
    pyglow.led(12,100)
    pyglow.led(18,100)
    sleep(sleep_speed)
    pyglow.led(11,110)
    pyglow.led(17,110)
    sleep(sleep_speed)
    # Turn on Arm 2 and 3 Yellow
    pyglow.led(9,120)
    pyglow.led(15,120)
    sleep(sleep_speed)
    # Fade Arm 1 R, O, Y, G, B, W, Arm 2 and 3 W, B, G
    pyglow.led(1,30)
    sleep(sleep_speed)
    pyglow.led(2,40)
    sleep(sleep_speed)    
    pyglow.led(3,50)
    sleep(sleep_speed)
    pyglow.led(4,60)
    sleep(sleep_speed)
    pyglow.led(5,70)
    sleep(sleep_speed)
    pyglow.led(6,80)
    sleep(sleep_speed)
    pyglow.led(12,90)
    pyglow.led(18,90)
    sleep(sleep_speed)
    pyglow.led(11,100)
    pyglow.led(17,100)
    sleep(sleep_speed)
    pyglow.led(10,110)
    pyglow.led(16,110)
    sleep(sleep_speed)
    # Turn on Arm 2 and 3 Orange
    pyglow.led(8,120)
    pyglow.led(14,120)
    sleep(sleep_speed)
    # Fade Arm 1 R, O, Y, G, B, W, Arm 2 and 3 W, B, G, Y
    pyglow.led(1,20)
    sleep(sleep_speed)
    pyglow.led(2,30)
    sleep(sleep_speed)    
    pyglow.led(3,40)
    sleep(sleep_speed)
    pyglow.led(4,50)
    sleep(sleep_speed)
    pyglow.led(5,60)
    sleep(sleep_speed)
    pyglow.led(6,70)
    sleep(sleep_speed)
    pyglow.led(12,80)
    pyglow.led(18,80)
    sleep(sleep_speed)
    pyglow.led(11,90)
    pyglow.led(17,90)
    sleep(sleep_speed)
    pyglow.led(10,100)
    pyglow.led(16,100)
    sleep(sleep_speed)
    pyglow.led(9,110)
    pyglow.led(15,110)
    sleep(sleep_speed)
    # Turn on Arm 2 and 3, Red
    pyglow.led(7,120)
    pyglow.led(13,120)
    sleep(sleep_speed)
    # Fade Arm 1 R, O, Y, G, B, W, Arm 2 and 3 W, B, G, Y, O
    pyglow.led(1,10)
    sleep(sleep_speed)
    pyglow.led(2,20)
    sleep(sleep_speed)    
    pyglow.led(3,30)
    sleep(sleep_speed)
    pyglow.led(4,40)
    sleep(sleep_speed)
    pyglow.led(5,50)
    sleep(sleep_speed)
    pyglow.led(6,60)
    sleep(sleep_speed)
    pyglow.led(12,70)
    pyglow.led(18,70)
    sleep(sleep_speed)
    pyglow.led(11,80)
    pyglow.led(17,80)
    sleep(sleep_speed)
    pyglow.led(10,90)
    pyglow.led(16,90)
    sleep(sleep_speed)
    pyglow.led(9,100)
    pyglow.led(15,100)
    sleep(sleep_speed)
    pyglow.led(8,110)
    pyglow.led(14,110)
    sleep(sleep_speed)
    # Fade Arm 1 R, O, Y, G, B, W, Arm 2 and 3 W, B, G, Y, O, R
    pyglow.led(1,0)
    sleep(sleep_speed)
    pyglow.led(2,10)
    sleep(sleep_speed)    
    pyglow.led(3,20)
    sleep(sleep_speed)
    pyglow.led(4,30)
    sleep(sleep_speed)
    pyglow.led(5,40)
    sleep(sleep_speed)
    pyglow.led(6,50)
    sleep(sleep_speed)
    pyglow.led(12,60)
    pyglow.led(18,60)
    sleep(sleep_speed)
    pyglow.led(11,70)
    pyglow.led(17,70)
    sleep(sleep_speed)
    pyglow.led(10,80)
    pyglow.led(16,80)
    sleep(sleep_speed)
    pyglow.led(9,90)
    pyglow.led(15,90)
    sleep(sleep_speed)
    pyglow.led(8,100)
    pyglow.led(14,100)
    sleep(sleep_speed)
    pyglow.led(7,110)
    pyglow.led(13,110)
    sleep(sleep_speed)   
    # Fade Arm 1 O, Y, G, B, W, Arm 2 and 3 W, B, G, Y, O, R
    pyglow.led(2,0)
    sleep(sleep_speed)    
    pyglow.led(3,10)
    sleep(sleep_speed)
    pyglow.led(4,20)
    sleep(sleep_speed)
    pyglow.led(5,30)
    sleep(sleep_speed)
    pyglow.led(6,40)
    sleep(sleep_speed)
    pyglow.led(12,50)
    pyglow.led(18,50)
    sleep(sleep_speed)
    pyglow.led(11,60)
    pyglow.led(17,60)
    sleep(sleep_speed)
    pyglow.led(10,70)
    pyglow.led(16,70)
    sleep(sleep_speed)
    pyglow.led(9,80)
    pyglow.led(15,80)
    sleep(sleep_speed)
    pyglow.led(8,90)
    pyglow.led(14,90)
    sleep(sleep_speed)
    pyglow.led(7,100)
    pyglow.led(13,100)
    sleep(sleep_speed)
    # Fade Arm 1 Y, G, B, W, Arm 2 and 3 W, B, G, Y, O, R    
    pyglow.led(3,0)
    sleep(sleep_speed)
    pyglow.led(4,10)
    sleep(sleep_speed)
    pyglow.led(5,20)
    sleep(sleep_speed)
    pyglow.led(6,30)
    sleep(sleep_speed)
    pyglow.led(12,40)
    pyglow.led(18,40)
    sleep(sleep_speed)
    pyglow.led(11,50)
    pyglow.led(17,50)
    sleep(sleep_speed)
    pyglow.led(10,60)
    pyglow.led(16,60)
    sleep(sleep_speed)
    pyglow.led(9,70)
    pyglow.led(15,70)
    sleep(sleep_speed)
    pyglow.led(8,80)
    pyglow.led(14,80)
    sleep(sleep_speed)
    pyglow.led(7,90)
    pyglow.led(13,90)
    sleep(sleep_speed)
    # Fade Arm 1 G, B, W, Arm 2 and 3 W, B, G, Y, O, R    
    pyglow.led(4,0)
    sleep(sleep_speed)
    pyglow.led(5,10)
    sleep(sleep_speed)
    pyglow.led(6,20)
    sleep(sleep_speed)
    pyglow.led(12,30)
    pyglow.led(18,30)
    sleep(sleep_speed)
    pyglow.led(11,40)
    pyglow.led(17,40)
    sleep(sleep_speed)
    pyglow.led(10,50)
    pyglow.led(16,50)
    sleep(sleep_speed)
    pyglow.led(9,60)
    pyglow.led(15,60)
    sleep(sleep_speed)
    pyglow.led(8,70)
    pyglow.led(14,70)
    sleep(sleep_speed)
    pyglow.led(7,80)
    pyglow.led(13,80)
    sleep(sleep_speed)
    # Fade Arm 1 B, W, Arm 2 and 3 W, B, G, Y, O, R    
    pyglow.led(5,0)
    sleep(sleep_speed)
    pyglow.led(6,10)
    sleep(sleep_speed)
    pyglow.led(12,20)
    pyglow.led(18,20)
    sleep(sleep_speed)
    pyglow.led(11,30)
    pyglow.led(17,30)
    sleep(sleep_speed)
    pyglow.led(10,40)
    pyglow.led(16,40)
    sleep(sleep_speed)
    pyglow.led(9,50)
    pyglow.led(15,50)
    sleep(sleep_speed)
    pyglow.led(8,60)
    pyglow.led(14,60)
    sleep(sleep_speed)
    pyglow.led(7,70)
    pyglow.led(13,70)
    sleep(sleep_speed)
    # Fade Arm 1 W, Arm 2 and 3 W, B, G, Y, O, R    
    pyglow.led(6,0)
    sleep(sleep_speed)
    pyglow.led(12,10)
    pyglow.led(18,10)
    sleep(sleep_speed)
    pyglow.led(11,20)
    pyglow.led(17,20)
    sleep(sleep_speed)
    pyglow.led(10,30)
    pyglow.led(16,30)
    sleep(sleep_speed)
    pyglow.led(9,40)
    pyglow.led(15,40)
    sleep(sleep_speed)
    pyglow.led(8,50)
    pyglow.led(14,50)
    sleep(sleep_speed)
    pyglow.led(7,60)
    pyglow.led(13,60)
    sleep(sleep_speed)
    # Fade Arm 2 and 3 W, B, G, Y, O, R    
    pyglow.led(12,0)
    pyglow.led(18,0)
    sleep(sleep_speed)
    pyglow.led(11,10)
    pyglow.led(17,10)
    sleep(sleep_speed)
    pyglow.led(10,20)
    pyglow.led(16,20)
    sleep(sleep_speed)
    pyglow.led(9,30)
    pyglow.led(15,30)
    sleep(sleep_speed)
    pyglow.led(8,40)
    pyglow.led(14,40)
    sleep(sleep_speed)
    pyglow.led(7,50)
    pyglow.led(13,50)
    sleep(sleep_speed)
    # Fade Arm 2 and 3 B, G, Y, O, R    
    pyglow.led(11,0)
    pyglow.led(17,0)
    sleep(sleep_speed)
    pyglow.led(10,10)
    pyglow.led(16,10)
    sleep(sleep_speed)
    pyglow.led(9,20)
    pyglow.led(15,20)
    sleep(sleep_speed)
    pyglow.led(8,30)
    pyglow.led(14,30)
    sleep(sleep_speed)
    pyglow.led(7,40)
    pyglow.led(13,40)
    sleep(sleep_speed)
    # Fade Arm 2 and 3 G, Y, O, R    
    pyglow.led(10,0)
    pyglow.led(16,0)
    sleep(sleep_speed)
    pyglow.led(9,10)
    pyglow.led(15,10)
    sleep(sleep_speed)
    pyglow.led(8,20)
    pyglow.led(14,20)
    sleep(sleep_speed)
    pyglow.led(7,30)
    pyglow.led(13,30)
    sleep(sleep_speed)
    # Fade Arm 2 and 3 Y, O, R    
    pyglow.led(9,0)
    pyglow.led(15,0)
    sleep(sleep_speed)
    pyglow.led(8,10)
    pyglow.led(14,10)
    sleep(sleep_speed)
    pyglow.led(7,20)
    pyglow.led(13,20)
    sleep(sleep_speed)
    # Fade Arm 2 and 3 O, R    
    pyglow.led(8,0)
    pyglow.led(14,0)
    sleep(sleep_speed)
    pyglow.led(7,10)
    pyglow.led(13,10)
    sleep(sleep_speed)
    # Fade Arm 2 and 3 R   
    pyglow.led(7,0)
    pyglow.led(13,0)
    sleep(sleep_speed)

def fading_fuse_2(sleep_speed):
    # Turn on Arm 2 Red
    pyglow.led(7,120)
    sleep(sleep_speed)
    # Turn on Arm 2 Orange
    pyglow.led(8,120)
    sleep(sleep_speed)
    # Fade Arm 1 Red
    pyglow.led(7,110)
    sleep(sleep_speed)
    # Turn on Arm 2 Yellow
    pyglow.led(9,120)
    sleep(sleep_speed)
    # Fade Arm 2 R, O
    pyglow.led(7,100)
    sleep(sleep_speed)
    pyglow.led(8,110)
    sleep(sleep_speed)
    # Turn on Arm 2 Green
    pyglow.led(10,120)
    sleep(sleep_speed)
    # Fade Arm 2 R, O, Y
    pyglow.led(7,90)
    sleep(sleep_speed)
    pyglow.led(8,100)
    sleep(sleep_speed)    
    pyglow.led(9,110)
    sleep(sleep_speed)
    # Turn on Arm 2 Blue
    pyglow.led(11,120)
    sleep(sleep_speed)
    # Fade Arm 2 R, O, Y, G
    pyglow.led(7,80)
    sleep(sleep_speed)
    pyglow.led(8,90)
    sleep(sleep_speed)    
    pyglow.led(9,100)
    sleep(sleep_speed)
    pyglow.led(10,110)
    sleep(sleep_speed)
    # Arm 1, White
    pyglow.led(12,120)
    sleep(sleep_speed)
    # Fade Arm 2 R, O, Y, G, B
    pyglow.led(7,70)
    sleep(sleep_speed)
    pyglow.led(8,80)
    sleep(sleep_speed)    
    pyglow.led(9,90)
    sleep(sleep_speed)
    pyglow.led(10,100)
    sleep(sleep_speed)
    pyglow.led(11,110)
    sleep(sleep_speed)
    # Turn on Arm 2 and 3 White
    pyglow.led(6,120)
    pyglow.led(18,120)
    sleep(sleep_speed)
    # Fade Arm 2 R, O, Y, G, B, W
    pyglow.led(7,60)
    sleep(sleep_speed)
    pyglow.led(8,70)
    sleep(sleep_speed)    
    pyglow.led(9,80)
    sleep(sleep_speed)
    pyglow.led(10,90)
    sleep(sleep_speed)
    pyglow.led(11,100)
    sleep(sleep_speed)
    pyglow.led(12,110)
    sleep(sleep_speed)
    # Turn on Arm 2 and 3 Blue
    pyglow.led(5,120)
    pyglow.led(17,120)
    sleep(sleep_speed)
    # Fade Arm 2 R, O, Y, G, B, W, Arm 1 and 3 W
    pyglow.led(7,50)
    sleep(sleep_speed)
    pyglow.led(8,60)
    sleep(sleep_speed)    
    pyglow.led(9,70)
    sleep(sleep_speed)
    pyglow.led(10,80)
    sleep(sleep_speed)
    pyglow.led(11,90)
    sleep(sleep_speed)
    pyglow.led(12,100)
    sleep(sleep_speed)
    pyglow.led(6,110)
    pyglow.led(18,110)
    sleep(sleep_speed)
    # Arm 1 and 3, Green
    pyglow.led(4,120)
    pyglow.led(16,120)
    sleep(sleep_speed)
    # Fade Arm 2 R, O, Y, G, B, W, Arm 1 and 3 W, B
    pyglow.led(7,40)
    sleep(sleep_speed)
    pyglow.led(8,50)
    sleep(sleep_speed)    
    pyglow.led(9,60)
    sleep(sleep_speed)
    pyglow.led(10,70)
    sleep(sleep_speed)
    pyglow.led(11,80)
    sleep(sleep_speed)
    pyglow.led(12,90)
    sleep(sleep_speed)
    pyglow.led(6,100)
    pyglow.led(18,100)
    sleep(sleep_speed)
    pyglow.led(5,110)
    pyglow.led(17,110)
    sleep(sleep_speed)
    # Turn on Arm 1 and 3 Yellow
    pyglow.led(3,120)
    pyglow.led(15,120)
    sleep(sleep_speed)
    # Fade Arm 2 R, O, Y, G, B, W, Arm 1 and 3 W, B, G
    pyglow.led(7,30)
    sleep(sleep_speed)
    pyglow.led(8,40)
    sleep(sleep_speed)    
    pyglow.led(9,50)
    sleep(sleep_speed)
    pyglow.led(10,60)
    sleep(sleep_speed)
    pyglow.led(11,70)
    sleep(sleep_speed)
    pyglow.led(12,80)
    sleep(sleep_speed)
    pyglow.led(6,90)
    pyglow.led(18,90)
    sleep(sleep_speed)
    pyglow.led(5,100)
    pyglow.led(17,100)
    sleep(sleep_speed)
    pyglow.led(4,110)
    pyglow.led(16,110)
    sleep(sleep_speed)
    # Turn on Arm 1 and 3 Orange
    pyglow.led(2,120)
    pyglow.led(14,120)
    sleep(sleep_speed)
    # Fade Arm 2 R, O, Y, G, B, W, Arm 2 and 3 W, B, G, Y
    pyglow.led(7,20)
    sleep(sleep_speed)
    pyglow.led(8,30)
    sleep(sleep_speed)    
    pyglow.led(9,40)
    sleep(sleep_speed)
    pyglow.led(10,50)
    sleep(sleep_speed)
    pyglow.led(11,60)
    sleep(sleep_speed)
    pyglow.led(12,70)
    sleep(sleep_speed)
    pyglow.led(6,80)
    pyglow.led(18,80)
    sleep(sleep_speed)
    pyglow.led(5,90)
    pyglow.led(17,90)
    sleep(sleep_speed)
    pyglow.led(4,100)
    pyglow.led(16,100)
    sleep(sleep_speed)
    pyglow.led(3,110)
    pyglow.led(15,110)
    sleep(sleep_speed)
    # Turn on Arm 1 and 3, Red
    pyglow.led(1,120)
    pyglow.led(13,120)
    sleep(sleep_speed)
    # Fade Arm 2 R, O, Y, G, B, W, Arm 1 and 3 W, B, G, Y, O
    pyglow.led(7,10)
    sleep(sleep_speed)
    pyglow.led(8,20)
    sleep(sleep_speed)    
    pyglow.led(9,30)
    sleep(sleep_speed)
    pyglow.led(10,40)
    sleep(sleep_speed)
    pyglow.led(11,50)
    sleep(sleep_speed)
    pyglow.led(12,60)
    sleep(sleep_speed)
    pyglow.led(6,70)
    pyglow.led(18,70)
    sleep(sleep_speed)
    pyglow.led(5,80)
    pyglow.led(17,80)
    sleep(sleep_speed)
    pyglow.led(4,90)
    pyglow.led(16,90)
    sleep(sleep_speed)
    pyglow.led(3,100)
    pyglow.led(15,100)
    sleep(sleep_speed)
    pyglow.led(2,110)
    pyglow.led(14,110)
    sleep(sleep_speed)
    # Fade Arm 2 R, O, Y, G, B, W, Arm 1 and 3 W, B, G, Y, O, R
    pyglow.led(7,0)
    sleep(sleep_speed)
    pyglow.led(8,10)
    sleep(sleep_speed)    
    pyglow.led(9,20)
    sleep(sleep_speed)
    pyglow.led(10,30)
    sleep(sleep_speed)
    pyglow.led(11,40)
    sleep(sleep_speed)
    pyglow.led(12,50)
    sleep(sleep_speed)
    pyglow.led(6,60)
    pyglow.led(18,60)
    sleep(sleep_speed)
    pyglow.led(5,70)
    pyglow.led(17,70)
    sleep(sleep_speed)
    pyglow.led(4,80)
    pyglow.led(16,80)
    sleep(sleep_speed)
    pyglow.led(3,90)
    pyglow.led(15,90)
    sleep(sleep_speed)
    pyglow.led(2,100)
    pyglow.led(14,100)
    sleep(sleep_speed)
    pyglow.led(1,110)
    pyglow.led(13,110)
    sleep(sleep_speed)   
    # Fade Arm 2 O, Y, G, B, W, Arm 1 and 3 W, B, G, Y, O, R
    pyglow.led(8,0)
    sleep(sleep_speed)    
    pyglow.led(9,10)
    sleep(sleep_speed)
    pyglow.led(10,20)
    sleep(sleep_speed)
    pyglow.led(11,30)
    sleep(sleep_speed)
    pyglow.led(12,40)
    sleep(sleep_speed)
    pyglow.led(6,50)
    pyglow.led(18,50)
    sleep(sleep_speed)
    pyglow.led(5,60)
    pyglow.led(17,60)
    sleep(sleep_speed)
    pyglow.led(4,70)
    pyglow.led(16,70)
    sleep(sleep_speed)
    pyglow.led(3,80)
    pyglow.led(15,80)
    sleep(sleep_speed)
    pyglow.led(2,90)
    pyglow.led(14,90)
    sleep(sleep_speed)
    pyglow.led(1,100)
    pyglow.led(13,100)
    sleep(sleep_speed)
    # Fade Arm 2 Y, G, B, W, Arm 1 and 3 W, B, G, Y, O, R    
    pyglow.led(9,0)
    sleep(sleep_speed)
    pyglow.led(10,10)
    sleep(sleep_speed)
    pyglow.led(11,20)
    sleep(sleep_speed)
    pyglow.led(12,30)
    sleep(sleep_speed)
    pyglow.led(6,40)
    pyglow.led(18,40)
    sleep(sleep_speed)
    pyglow.led(5,50)
    pyglow.led(17,50)
    sleep(sleep_speed)
    pyglow.led(4,60)
    pyglow.led(16,60)
    sleep(sleep_speed)
    pyglow.led(3,70)
    pyglow.led(15,70)
    sleep(sleep_speed)
    pyglow.led(2,80)
    pyglow.led(14,80)
    sleep(sleep_speed)
    pyglow.led(1,90)
    pyglow.led(13,90)
    sleep(sleep_speed)
    # Fade Arm 2 G, B, W, Arm 1 and 3 W, B, G, Y, O, R    
    pyglow.led(10,0)
    sleep(sleep_speed)
    pyglow.led(11,10)
    sleep(sleep_speed)
    pyglow.led(12,20)
    sleep(sleep_speed)
    pyglow.led(6,30)
    pyglow.led(18,30)
    sleep(sleep_speed)
    pyglow.led(5,40)
    pyglow.led(17,40)
    sleep(sleep_speed)
    pyglow.led(4,50)
    pyglow.led(16,50)
    sleep(sleep_speed)
    pyglow.led(3,60)
    pyglow.led(15,60)
    sleep(sleep_speed)
    pyglow.led(2,70)
    pyglow.led(14,70)
    sleep(sleep_speed)
    pyglow.led(1,80)
    pyglow.led(13,80)
    sleep(sleep_speed)
    # Fade Arm 2 B, W, Arm 1 and 3 W, B, G, Y, O, R    
    pyglow.led(11,0)
    sleep(sleep_speed)
    pyglow.led(12,10)
    sleep(sleep_speed)
    pyglow.led(6,20)
    pyglow.led(18,20)
    sleep(sleep_speed)
    pyglow.led(5,30)
    pyglow.led(17,30)
    sleep(sleep_speed)
    pyglow.led(4,40)
    pyglow.led(16,40)
    sleep(sleep_speed)
    pyglow.led(3,50)
    pyglow.led(15,50)
    sleep(sleep_speed)
    pyglow.led(2,60)
    pyglow.led(14,60)
    sleep(sleep_speed)
    pyglow.led(1,70)
    pyglow.led(13,70)
    sleep(sleep_speed)
    # Fade Arm 2 W, Arm 1 and 3 W, B, G, Y, O, R    
    pyglow.led(12,0)
    sleep(sleep_speed)
    pyglow.led(6,10)
    pyglow.led(18,10)
    sleep(sleep_speed)
    pyglow.led(5,20)
    pyglow.led(17,20)
    sleep(sleep_speed)
    pyglow.led(4,30)
    pyglow.led(16,30)
    sleep(sleep_speed)
    pyglow.led(3,40)
    pyglow.led(15,40)
    sleep(sleep_speed)
    pyglow.led(2,50)
    pyglow.led(14,50)
    sleep(sleep_speed)
    pyglow.led(1,60)
    pyglow.led(13,60)
    sleep(sleep_speed)
    # Fade Arm 1 and 3 W, B, G, Y, O, R    
    pyglow.led(6,0)
    pyglow.led(18,0)
    sleep(sleep_speed)
    pyglow.led(5,10)
    pyglow.led(17,10)
    sleep(sleep_speed)
    pyglow.led(4,20)
    pyglow.led(16,20)
    sleep(sleep_speed)
    pyglow.led(3,30)
    pyglow.led(15,30)
    sleep(sleep_speed)
    pyglow.led(2,40)
    pyglow.led(14,40)
    sleep(sleep_speed)
    pyglow.led(1,50)
    pyglow.led(13,50)
    sleep(sleep_speed)
    # Fade Arm 1 and 3 B, G, Y, O, R    
    pyglow.led(5,0)
    pyglow.led(17,0)
    sleep(sleep_speed)
    pyglow.led(4,10)
    pyglow.led(16,10)
    sleep(sleep_speed)
    pyglow.led(3,20)
    pyglow.led(15,20)
    sleep(sleep_speed)
    pyglow.led(2,30)
    pyglow.led(14,30)
    sleep(sleep_speed)
    pyglow.led(1,40)
    pyglow.led(13,40)
    sleep(sleep_speed)
    # Fade Arm 1 and 3 G, Y, O, R    
    pyglow.led(4,0)
    pyglow.led(16,0)
    sleep(sleep_speed)
    pyglow.led(3,10)
    pyglow.led(15,10)
    sleep(sleep_speed)
    pyglow.led(2,20)
    pyglow.led(14,20)
    sleep(sleep_speed)
    pyglow.led(1,30)
    pyglow.led(13,30)
    sleep(sleep_speed)
    # Fade Arm 1 and 3 Y, O, R    
    pyglow.led(3,0)
    pyglow.led(15,0)
    sleep(sleep_speed)
    pyglow.led(2,10)
    pyglow.led(14,10)
    sleep(sleep_speed)
    pyglow.led(1,20)
    pyglow.led(13,20)
    sleep(sleep_speed)
    # Fade Arm 1 and 3 O, R    
    pyglow.led(2,0)
    pyglow.led(14,0)
    sleep(sleep_speed)
    pyglow.led(1,10)
    pyglow.led(13,10)
    sleep(sleep_speed)
    # Fade Arm 1 and 3 R   
    pyglow.led(1,0)
    pyglow.led(13,0)
    sleep(sleep_speed)


def fading_fuse_3(sleep_speed):
    # Turn on Arm 3 Red
    pyglow.led(13,120)
    sleep(sleep_speed)
    # Turn on Arm 3 Orange
    pyglow.led(14,120)
    sleep(sleep_speed)
    # Fade Arm 3 Red
    pyglow.led(13,110)
    sleep(sleep_speed)
    # Turn on Arm 3 Yellow
    pyglow.led(15,120)
    sleep(sleep_speed)
    # Fade Arm 3 R, O
    pyglow.led(13,100)
    sleep(sleep_speed)
    pyglow.led(14,110)
    sleep(sleep_speed)
    # Turn on Arm 3 Green
    pyglow.led(16,120)
    sleep(sleep_speed)
    # Fade Arm 3 R, O, Y
    pyglow.led(13,90)
    sleep(sleep_speed)
    pyglow.led(14,100)
    sleep(sleep_speed)    
    pyglow.led(15,110)
    sleep(sleep_speed)
    # Turn on Arm 3 Blue
    pyglow.led(17,120)
    sleep(sleep_speed)
    # Fade Arm 3 R, O, Y, G
    pyglow.led(13,80)
    sleep(sleep_speed)
    pyglow.led(14,90)
    sleep(sleep_speed)    
    pyglow.led(15,100)
    sleep(sleep_speed)
    pyglow.led(16,110)
    sleep(sleep_speed)
    # Arm 3, White
    pyglow.led(18,120)
    sleep(sleep_speed)
    # Fade Arm 3 R, O, Y, G, B
    pyglow.led(13,70)
    sleep(sleep_speed)
    pyglow.led(14,80)
    sleep(sleep_speed)    
    pyglow.led(15,90)
    sleep(sleep_speed)
    pyglow.led(16,100)
    sleep(sleep_speed)
    pyglow.led(17,110)
    sleep(sleep_speed)
    # Turn on Arm 1 and 2 White
    pyglow.led(6,120)
    pyglow.led(12,120)
    sleep(sleep_speed)
    # Fade Arm 3 R, O, Y, G, B, W
    pyglow.led(13,60)
    sleep(sleep_speed)
    pyglow.led(14,70)
    sleep(sleep_speed)    
    pyglow.led(15,80)
    sleep(sleep_speed)
    pyglow.led(16,90)
    sleep(sleep_speed)
    pyglow.led(17,100)
    sleep(sleep_speed)
    pyglow.led(18,110)
    sleep(sleep_speed)
    # Turn on Arm 1 and 2 Blue
    pyglow.led(5,120)
    pyglow.led(11,120)
    sleep(sleep_speed)
    # Fade Arm 3 R, O, Y, G, B, W, Arm 1 and 2 W
    pyglow.led(13,50)
    sleep(sleep_speed)
    pyglow.led(14,60)
    sleep(sleep_speed)    
    pyglow.led(15,70)
    sleep(sleep_speed)
    pyglow.led(16,80)
    sleep(sleep_speed)
    pyglow.led(17,90)
    sleep(sleep_speed)
    pyglow.led(18,100)
    sleep(sleep_speed)
    pyglow.led(6,110)
    pyglow.led(12,110)
    sleep(sleep_speed)
    # Arm 1 and 2, Green
    pyglow.led(4,120)
    pyglow.led(10,120)
    sleep(sleep_speed)
    # Fade Arm 3 R, O, Y, G, B, W, Arm 1 and 2 W, B
    pyglow.led(13,40)
    sleep(sleep_speed)
    pyglow.led(14,50)
    sleep(sleep_speed)    
    pyglow.led(15,60)
    sleep(sleep_speed)
    pyglow.led(16,70)
    sleep(sleep_speed)
    pyglow.led(17,80)
    sleep(sleep_speed)
    pyglow.led(18,90)
    sleep(sleep_speed)
    pyglow.led(6,100)
    pyglow.led(12,100)
    sleep(sleep_speed)
    pyglow.led(5,110)
    pyglow.led(11,110)
    sleep(sleep_speed)
    # Turn on Arm 1 and 2 Yellow
    pyglow.led(3,120)
    pyglow.led(9,120)
    sleep(sleep_speed)
    # Fade Arm 3 R, O, Y, G, B, W, Arm 1 and 2 W, B, G
    pyglow.led(13,30)
    sleep(sleep_speed)
    pyglow.led(14,40)
    sleep(sleep_speed)    
    pyglow.led(15,50)
    sleep(sleep_speed)
    pyglow.led(16,60)
    sleep(sleep_speed)
    pyglow.led(17,70)
    sleep(sleep_speed)
    pyglow.led(18,80)
    sleep(sleep_speed)
    pyglow.led(6,90)
    pyglow.led(12,90)
    sleep(sleep_speed)
    pyglow.led(5,100)
    pyglow.led(11,100)
    sleep(sleep_speed)
    pyglow.led(4,110)
    pyglow.led(10,110)
    sleep(sleep_speed)
    # Turn on Arm 1 and 2 Orange
    pyglow.led(2,120)
    pyglow.led(8,120)
    sleep(sleep_speed)
    # Fade Arm 3 R, O, Y, G, B, W, Arm 1 and 2 W, B, G, Y
    pyglow.led(13,20)
    sleep(sleep_speed)
    pyglow.led(14,30)
    sleep(sleep_speed)    
    pyglow.led(15,40)
    sleep(sleep_speed)
    pyglow.led(16,50)
    sleep(sleep_speed)
    pyglow.led(17,60)
    sleep(sleep_speed)
    pyglow.led(18,70)
    sleep(sleep_speed)
    pyglow.led(6,80)
    pyglow.led(12,80)
    sleep(sleep_speed)
    pyglow.led(5,90)
    pyglow.led(11,90)
    sleep(sleep_speed)
    pyglow.led(4,100)
    pyglow.led(10,100)
    sleep(sleep_speed)
    pyglow.led(3,110)
    pyglow.led(9,110)
    sleep(sleep_speed)
    # Turn on Arm 1 and 2, Red
    pyglow.led(1,120)
    pyglow.led(7,120)
    sleep(sleep_speed)
    # Fade Arm 3 R, O, Y, G, B, W, Arm 1 and 2 W, B, G, Y, O
    pyglow.led(13,10)
    sleep(sleep_speed)
    pyglow.led(14,20)
    sleep(sleep_speed)    
    pyglow.led(15,30)
    sleep(sleep_speed)
    pyglow.led(16,40)
    sleep(sleep_speed)
    pyglow.led(17,50)
    sleep(sleep_speed)
    pyglow.led(18,60)
    sleep(sleep_speed)
    pyglow.led(6,70)
    pyglow.led(12,70)
    sleep(sleep_speed)
    pyglow.led(5,80)
    pyglow.led(11,80)
    sleep(sleep_speed)
    pyglow.led(4,90)
    pyglow.led(10,90)
    sleep(sleep_speed)
    pyglow.led(3,100)
    pyglow.led(9,100)
    sleep(sleep_speed)
    pyglow.led(2,110)
    pyglow.led(8,110)
    sleep(sleep_speed)
    # Fade Arm 3 R, O, Y, G, B, W, Arm 1 and 2 W, B, G, Y, O, R
    pyglow.led(13,0)
    sleep(sleep_speed)
    pyglow.led(14,10)
    sleep(sleep_speed)    
    pyglow.led(15,20)
    sleep(sleep_speed)
    pyglow.led(16,30)
    sleep(sleep_speed)
    pyglow.led(17,40)
    sleep(sleep_speed)
    pyglow.led(18,50)
    sleep(sleep_speed)
    pyglow.led(6,60)
    pyglow.led(12,60)
    sleep(sleep_speed)
    pyglow.led(5,70)
    pyglow.led(11,70)
    sleep(sleep_speed)
    pyglow.led(4,80)
    pyglow.led(10,80)
    sleep(sleep_speed)
    pyglow.led(3,90)
    pyglow.led(9,90)
    sleep(sleep_speed)
    pyglow.led(2,100)
    pyglow.led(8,100)
    sleep(sleep_speed)
    pyglow.led(1,110)
    pyglow.led(7,110)
    sleep(sleep_speed)   
    # Fade Arm 3 O, Y, G, B, W, Arm 1 and 2 W, B, G, Y, O, R
    pyglow.led(14,0)
    sleep(sleep_speed)    
    pyglow.led(15,10)
    sleep(sleep_speed)
    pyglow.led(16,20)
    sleep(sleep_speed)
    pyglow.led(17,30)
    sleep(sleep_speed)
    pyglow.led(18,40)
    sleep(sleep_speed)
    pyglow.led(6,50)
    pyglow.led(12,50)
    sleep(sleep_speed)
    pyglow.led(5,60)
    pyglow.led(11,60)
    sleep(sleep_speed)
    pyglow.led(4,70)
    pyglow.led(10,70)
    sleep(sleep_speed)
    pyglow.led(3,80)
    pyglow.led(9,80)
    sleep(sleep_speed)
    pyglow.led(2,90)
    pyglow.led(8,90)
    sleep(sleep_speed)
    pyglow.led(1,100)
    pyglow.led(7,100)
    sleep(sleep_speed)
    # Fade Arm 3 Y, G, B, W, Arm 1 and 2 W, B, G, Y, O, R    
    pyglow.led(15,0)
    sleep(sleep_speed)
    pyglow.led(16,10)
    sleep(sleep_speed)
    pyglow.led(17,20)
    sleep(sleep_speed)
    pyglow.led(18,30)
    sleep(sleep_speed)
    pyglow.led(6,40)
    pyglow.led(12,40)
    sleep(sleep_speed)
    pyglow.led(5,50)
    pyglow.led(11,50)
    sleep(sleep_speed)
    pyglow.led(4,60)
    pyglow.led(10,60)
    sleep(sleep_speed)
    pyglow.led(3,70)
    pyglow.led(9,70)
    sleep(sleep_speed)
    pyglow.led(2,80)
    pyglow.led(8,80)
    sleep(sleep_speed)
    pyglow.led(1,90)
    pyglow.led(7,90)
    sleep(sleep_speed)
    # Fade Arm 3 G, B, W, Arm 1 and 2 W, B, G, Y, O, R    
    pyglow.led(16,0)
    sleep(sleep_speed)
    pyglow.led(17,10)
    sleep(sleep_speed)
    pyglow.led(18,20)
    sleep(sleep_speed)
    pyglow.led(6,30)
    pyglow.led(12,30)
    sleep(sleep_speed)
    pyglow.led(5,40)
    pyglow.led(11,40)
    sleep(sleep_speed)
    pyglow.led(4,50)
    pyglow.led(10,50)
    sleep(sleep_speed)
    pyglow.led(3,60)
    pyglow.led(9,60)
    sleep(sleep_speed)
    pyglow.led(2,70)
    pyglow.led(8,70)
    sleep(sleep_speed)
    pyglow.led(1,80)
    pyglow.led(7,80)
    sleep(sleep_speed)
    # Fade Arm 3 B, W, Arm 1 and 2 W, B, G, Y, O, R    
    pyglow.led(17,0)
    sleep(sleep_speed)
    pyglow.led(18,10)
    sleep(sleep_speed)
    pyglow.led(6,20)
    pyglow.led(12,20)
    sleep(sleep_speed)
    pyglow.led(5,30)
    pyglow.led(11,30)
    sleep(sleep_speed)
    pyglow.led(4,40)
    pyglow.led(10,40)
    sleep(sleep_speed)
    pyglow.led(3,50)
    pyglow.led(9,50)
    sleep(sleep_speed)
    pyglow.led(2,60)
    pyglow.led(8,60)
    sleep(sleep_speed)
    pyglow.led(1,70)
    pyglow.led(7,70)
    sleep(sleep_speed)
    # Fade Arm 3 W, Arm 1 and 2 W, B, G, Y, O, R    
    pyglow.led(18,0)
    sleep(sleep_speed)
    pyglow.led(6,10)
    pyglow.led(12,10)
    sleep(sleep_speed)
    pyglow.led(5,20)
    pyglow.led(11,20)
    sleep(sleep_speed)
    pyglow.led(4,30)
    pyglow.led(10,30)
    sleep(sleep_speed)
    pyglow.led(3,40)
    pyglow.led(9,40)
    sleep(sleep_speed)
    pyglow.led(2,50)
    pyglow.led(8,50)
    sleep(sleep_speed)
    pyglow.led(1,60)
    pyglow.led(7,60)
    sleep(sleep_speed)
    # Fade Arm 1 and 2 W, B, G, Y, O, R    
    pyglow.led(6,0)
    pyglow.led(12,0)
    sleep(sleep_speed)
    pyglow.led(5,10)
    pyglow.led(11,10)
    sleep(sleep_speed)
    pyglow.led(4,20)
    pyglow.led(10,20)
    sleep(sleep_speed)
    pyglow.led(3,30)
    pyglow.led(9,30)
    sleep(sleep_speed)
    pyglow.led(2,40)
    pyglow.led(8,40)
    sleep(sleep_speed)
    pyglow.led(1,50)
    pyglow.led(7,50)
    sleep(sleep_speed)
    # Fade Arm 1 and 2 B, G, Y, O, R    
    pyglow.led(5,0)
    pyglow.led(11,0)
    sleep(sleep_speed)
    pyglow.led(4,10)
    pyglow.led(10,10)
    sleep(sleep_speed)
    pyglow.led(3,20)
    pyglow.led(9,20)
    sleep(sleep_speed)
    pyglow.led(2,30)
    pyglow.led(8,30)
    sleep(sleep_speed)
    pyglow.led(1,40)
    pyglow.led(7,40)
    sleep(sleep_speed)
    # Fade Arm 1 and 2 G, Y, O, R    
    pyglow.led(4,0)
    pyglow.led(10,0)
    sleep(sleep_speed)
    pyglow.led(3,10)
    pyglow.led(9,10)
    sleep(sleep_speed)
    pyglow.led(2,20)
    pyglow.led(8,20)
    sleep(sleep_speed)
    pyglow.led(1,30)
    pyglow.led(7,30)
    sleep(sleep_speed)
    # Fade Arm 1 and 2 Y, O, R    
    pyglow.led(3,0)
    pyglow.led(9,0)
    sleep(sleep_speed)
    pyglow.led(2,10)
    pyglow.led(8,10)
    sleep(sleep_speed)
    pyglow.led(1,20)
    pyglow.led(7,20)
    sleep(sleep_speed)
    # Fade Arm 1 and 2 O, R    
    pyglow.led(2,0)
    pyglow.led(8,0)
    sleep(sleep_speed)
    pyglow.led(1,10)
    pyglow.led(7,10)
    sleep(sleep_speed)
    # Fade Arm 1 and 2 R   
    pyglow.led(1,0)
    pyglow.led(7,0)
    sleep(sleep_speed)

def fading_fuse ():
    sleep_speed = 0.05
    ''' Uncomment the following line for feedback while the program is running '''
    #print "Going fast..."
    while sleep_speed > 0.01:
        ''' Uncomment the following line for feedback while the program is running '''
        #print "sleep_speed = ", sleep_speed
        fading_fuse_1(sleep_speed)
        fading_fuse_2(sleep_speed)
        fading_fuse_3(sleep_speed)
        # increse speed
        sleep_speed -= 0.0025
    go_faster()

def go_faster():
    sleep_speed = 0.01
    ''' Uncomment the following line for feedback while the program is running '''
    #print "Going faster..."
    counter = 10
    while counter > 0:
        ''' Uncomment the following line for feedback while the program is running '''
        #print "sleep_speed = ", sleep_speed#print "counter = ", counter
        fading_fuse_1(sleep_speed)
        fading_fuse_2(sleep_speed)
        fading_fuse_3(sleep_speed)
        # decrease counter
        counter -= 1
    sleep(2)
    fading_fuse()
    
# Start the Program
try:
   fading_fuse()
# Stop the program and turn off LEDs with Ctrl-C
except KeyboardInterrupt:
    pyglow.all()
