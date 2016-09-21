#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import String
import serial
import herkulex
import time 
herkulex.connect('/dev/ttyUSB0',115200)


l_low_arm_roll = herkulex.servo(18)
l_arm_roll  = herkulex.servo(17)
l_shoulder_pitch = herkulex.servo(16)
r_shoulder_pitch = herkulex.servo(13)
r_arm_roll  = herkulex.servo(14)
r_low_arm_roll = herkulex.servo(15)


motor_id = [18,17,16,13,14,15]
motor_no = 6

## MOTOR_TORQUE_ON ##
l_low_arm_roll.torque_on()
l_arm_roll.torque_on()
l_shoulder_pitch.torque_on() 
r_shoulder_pitch.torque_on() 
r_arm_roll.torque_on() 
r_low_arm_roll.torque_on()

init= [0,90,80,-80,-90,0]
right_bend= [0,90,80,-70,7,-70]
left_bend= [70,-27,70,-80,-90,0]


def talker():
 for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(init[y],200,4)
   time.sleep(0.0007)
 time.sleep(3)
 while 1:
  
  for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(right_bend[y],150,4)
   time.sleep(0.0007)
  time.sleep(2)
  for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(left_bend[y],150,4)
   time.sleep(0.0007)
  time.sleep(2)
 
######################
  
 herkulex.close()
if __name__ == '__main__':
    try:
       talker()
    except rospy.ROSInterruptException:
       pass
