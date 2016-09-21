#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import String
import serial
import herkulex
import time 
herkulex.connect('/dev/ttyUSB0',115200)

#biped
l_hip_roll    = herkulex.servo(4)
l_hip_pitch   = herkulex.servo(2)
l_knee_pitch  = herkulex.servo(10)
l_ankle_pitch = herkulex.servo(5)
l_ankle_roll  = herkulex.servo(7)
r_hip_roll    = herkulex.servo(12)
r_hip_pitch   = herkulex.servo(8)
r_knee_pitch  = herkulex.servo(1)
r_ankle_pitch = herkulex.servo(11)
r_ankle_roll  = herkulex.servo(6)
#new=herkulex.servo(10)
#torso
#l_hand_pitch = herkulex.servo(13)
#l_hand_roll  = herkulex.servo(14)
#l_hand_yaw   = herkulex.servo(15)
#r_hand_pitch = herkulex.servo(16)
#r_hand_roll  = herkulex.servo(17)
#r_hand_yaw   = herkulex.servo(18)


motor_id = [4, 2, 10, 5, 7, 12, 8, 1, 11, 6]

## MOTOR_TORQUE_ON ##

l_hip_roll.torque_on()
l_hip_pitch.torque_on()
l_knee_pitch.torque_on()
l_ankle_roll.torque_on()
l_ankle_pitch.torque_on()
r_hip_roll.torque_on()
r_hip_pitch.torque_on() 
r_knee_pitch.torque_on()

r_ankle_pitch.torque_on()
r_ankle_roll.torque_on()

#zero_offset=[-9, 0 , 1,4, 3, 0, 7, 1, 0, -32]
zero_offset=[-5, 4 , 10,11, 9, 3, 6, -9, -8, -31]
down=[0,20,-40,-22,0,0,-20,40,22,0]
up=  [0,10,-10,-8,0,0,-10,10,8,0]


def talker():
 while 1:
  for y in range (0,10):
   herkulex.servo(motor_id[y]).set_servo_angle(down[y]+zero_offset[y],100,4)
   time.sleep(0.0007)
  time.sleep(1)
  for y in range (0,10):
   herkulex.servo(motor_id[y]).set_servo_angle(up[y]+zero_offset[y],100,4)
   time.sleep(0.0007)
  time.sleep(1)
 #for y in range (0,10):
  #print herkulex.servo(motor_id[y]).get_servo_angle()
######################
  
 herkulex.close()
if __name__ == '__main__':
    try:
       talker()
    except rospy.ROSInterruptException:
       pass
