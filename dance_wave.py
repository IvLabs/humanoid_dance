#!/usr/bin/env python
# license removed for brevity

## Date : 12|08|2016 ##
## Author : Surabhi Verma ##
## TORSO_STATIC_WALKING ##
## INPUT FROM EXCEL SHEET, ANGLES PRECALCULATED IN MATLAB ##

import rospy
from std_msgs.msg import Float64
import serial
import herkulex
import time 
import xlrd
import math
herkulex.connect('/dev/ttyUSB4',115200)


l_hand_roll  = herkulex.servo(17)
l_hand_pitch = herkulex.servo(16)
l_low_arm = herkulex.servo(18)

r_hand_roll  = herkulex.servo(14)
r_hand_pitch = herkulex.servo(13)
r_low_arm   = herkulex.servo(15)





motor_id = [4, 2, 10, 5, 7, 12, 8, 1, 11, 6,13,14,15,16,17,18]
delay=1.5

############################

 
## MOTOR_TORQUE_ON ##


l_hand_pitch.torque_on() 
l_hand_roll.torque_on()
l_low_arm.torque_on()
r_hand_pitch.torque_on()
r_hand_roll.torque_on()
r_low_arm.torque_on()

k=0.5


def talker():
      
    pub = rospy.Publisher('angles', Float64, queue_size=10) #node is publishing to the angles topic 
    rospy.init_node('test_motor_behavior', anonymous=True) #plot_graphs is the name of the publishing node
    t_init = rospy.get_time()
    rate = rospy.Rate(40) # 40hz
    while not rospy.is_shutdown():
       #hiii#
       while(1):
         
         if i<1:
          l_hand_pitch.set_servo_angle(0,100,4)
          time.sleep(0.0007)
          l_hand_roll.set_servo_angle(90,100,4)
          time.sleep(0.0007)
          l_low_arm.set_servo_angle(0,100,4)
          time.sleep(0.0007)     
          r_hand_pitch.set_servo_angle(0,100,4)
          time.sleep(0.0007)
          r_hand_roll.set_servo_angle(-90,100,4)
          time.sleep(0.0007)
          r_low_arm.set_servo_angle(0,100,4)
          time.sleep(1)
          print("yoo")
          i=i+1

         

         l_hand_pitch.set_servo_angle(0,100,4)
         time.sleep(0.0007)
         l_hand_roll.set_servo_angle(90,100,4)
         time.sleep(0.0007)
         l_low_arm.set_servo_angle(0,100,4)
         time.sleep(0.5)

         l_low_arm.set_servo_angle(-45,100,4)
         time.sleep(0.5)
         l_hand_roll.set_servo_angle(135,100,4)
         time.sleep(0.0007)  
         l_low_arm.set_servo_angle(90,200,4)

         time.sleep(1.5)
         l_low_arm.set_servo_angle(-45,200,4)
         time.sleep(0.0007)
         l_hand_roll.set_servo_angle(68,100,4)
         time.sleep(0.5) 

         l_hand_pitch.set_servo_angle(0,100,4)
         time.sleep(0.0007)
         l_hand_roll.set_servo_angle(90,100,4)
         time.sleep(0.0007)
         l_low_arm.set_servo_angle(0,100,4)
         time.sleep(0.0007) 
         time.sleep(1) 

 ######################################################################################
         r_hand_pitch.set_servo_angle(0,100,4)
         time.sleep(0.007)
         r_hand_roll.set_servo_angle(-90,100,4)
         time.sleep(0.007)
         r_low_arm.set_servo_angle(0,100,4)
         time.sleep(0.5)

         r_low_arm.set_servo_angle(-90,100,4)
         time.sleep(0.007)
         r_hand_roll.set_servo_angle(-135,100,4)
         time.sleep(1)
         r_low_arm.set_servo_angle(-90,200,4)
         time.sleep(0.007)

  
         r_hand_roll.set_servo_angle(-45,100,4)
         time.sleep(0.0007)
         r_low_arm.set_servo_angle(75,200,4)
         time.sleep(2)

         r_hand_roll.set_servo_angle(-90,100,4)
         time.sleep(0.0007)
         r_low_arm.set_servo_angle(0,200,4)
         time.sleep(0.5)









   
       rate.sleep() 
  
    herkulex.close()
if __name__ == '__main__':
    try:
       talker()
    except rospy.ROSInterruptException:
       pass
