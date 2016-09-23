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

l_low_arm_roll = herkulex.servo(18)
l_arm_roll  = herkulex.servo(17)
l_shoulder_pitch = herkulex.servo(16)
r_shoulder_pitch = herkulex.servo(13)
r_arm_roll  = herkulex.servo(14)
r_low_arm_roll = herkulex.servo(15)

#new=herkulex.servo(10)
#torso
#l_shoulder_pitch = herkulex.servo(13)
#l_arm_roll  = herkulex.servo(14)
#l_hand_yaw   = herkulex.servo(15)
#r_shoulder_pitch = herkulex.servo(16)
#r_arm_roll  = herkulex.servo(17)
#r_hand_yaw   = herkulex.servo(18)


motor_id = [4, 2, 10, 5, 7, 12, 8, 1, 11, 6,18,17,16,13,14,15]
zero_offset=[-8, -2 , 10,11, 7, 0, 2, -6, -8, -31,0,0,0,0,0,0]
motor_no=16
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

l_low_arm_roll.torque_on()
l_arm_roll.torque_on()
l_shoulder_pitch.torque_on() 
r_shoulder_pitch.torque_on() 
r_arm_roll.torque_on() 
r_low_arm_roll.torque_on()

###########

straight=[0,10,-10,-8,0,0,-10,10,8,0,
10,2,0,-17,-7,0
]

for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(straight[y]+zero_offset[y],100,4)
   time.sleep(0.0007)
time.sleep(1)
############
hand_on_hips=[0,10,-10,-8,0,0,-10,10,8,0,
104,58,2,-20,-53,-84
]

for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(hand_on_hips[y]+zero_offset[y],200,4)
   time.sleep(0.0007)
time.sleep(2)
############
hand_on_hips=[0,10,-10,-8,0,0,-10,10,8,0,
104,58,2,-20,-53,-84
]

for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(hand_on_hips[y]+zero_offset[y],100,4)
   time.sleep(0.0007)
time.sleep(1)

#############

swing_left=[-15,10,0,5,0,-6,-12,7,0,-38,
104,58,2,-20,-53,-84
]

for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(swing_left[y],200,4)
   time.sleep(0.0007)
time.sleep(2)
##############

swing_right=[-1,10,-7,3,13,5,-11,14,5,-28,
104,58,2,-20,-53,-84
]

for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(swing_right[y],200,4)
   time.sleep(0.0007)
time.sleep(2)
##############

right_up=[0,10,-10,-8,0,0,-10,10,8,0,
0,90,0,-17,-7,0
]

for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(right_up[y]+zero_offset[y],200,4)
   time.sleep(0.0007)
time.sleep(2)
##############

both_up=[0,10,-10,-8,0,0,-10,10,8,0,
0,90,0,0,-90,0
]

for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(both_up[y]+zero_offset[y],200,4)
   time.sleep(0.0007)
time.sleep(2)

##############
right_shift_swing=[-15,10,0,5,0,-6,-12,7,0,-38,
0,90,80,-70,7,-70
]

left_shift_swing = [-1,10,-7,3,13,5,-11,14,5,-28,
70,-27,70,-80,-90,0
]
for i in range (0,2):
 for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(right_shift_swing[y],200,4)
   time.sleep(0.0007)
 time.sleep(2)
 for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(left_shift_swing[y],200,4)
   time.sleep(0.0007)
 time.sleep(2)

##############
right_up=[0,10,-10,-8,0,0,-10,10,8,0,
0,90,0,-17,-7,0
]

for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(right_up[y]+zero_offset[y],200,4)
   time.sleep(0.0007)
time.sleep(2)
##############

straight=[0,10,-10,-8,0,0,-10,10,8,0,
10,2,0,-17,-7,0
]

for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(straight[y]+zero_offset[y],200,4)
   time.sleep(0.0007)
time.sleep(2)

##############

l_hand_up = [0,10,-10,-8,0,0,-10,10,8,0,
94,91,0,-17,-7,0
]
both=[0,10,-10,-8,0,0,-10,10,8,0,
#94,91,-6,6,-85,-85
94,91,0,-17,-85,-85
]
r_hand_up=[0,10,-10,-8,0,0,-10,10,8,0,
10,2,0,-17,-85,-85
#8,3,5,6,-85,-85
]
goal_t=70
delay=0.7

for y in range (0,1):
  for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(l_hand_up[y]+zero_offset[y],goal_t,4)
   time.sleep(0.0007)
  time.sleep(delay)
  for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(both[y]+zero_offset[y],goal_t,4)
   time.sleep(0.0007)
  time.sleep(delay) 
  for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(l_hand_up[y]+zero_offset[y],goal_t,4)
   time.sleep(0.0007)
  time.sleep(delay)
#######
  for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(straight[y]+zero_offset[y],goal_t,4)
   time.sleep(0.0007)
  time.sleep(delay)
  for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(r_hand_up[y]+zero_offset[y],goal_t,4)
   time.sleep(0.0007)
  time.sleep(delay)
  for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(both[y]+zero_offset[y],goal_t,4)
   time.sleep(0.0007)
  time.sleep(delay) 
  for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(r_hand_up[y]+zero_offset[y],goal_t,4)
   time.sleep(0.0007)
  time.sleep(delay)
  for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(straight[y]+zero_offset[y],goal_t,4)
   time.sleep(0.0007)
  time.sleep(delay)
################
inter=[0,10,-10,-8,0,0,-10,10,8,0,
58,43,68,-68,-38,-45]

for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(inter[y]+zero_offset[y],100,4)
   time.sleep(0.0007)
time.sleep(1)

hand_out = [0,10,-10,-8,0,0,-10,10,8,0,
58,37,150,-150,-30,-45
]
hand_in=[0,10,-10,-8,0,0,-10,10,8,0,
48,0,150,-150,0,-45
]
for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(hand_out[y]+zero_offset[y],150,4)
   time.sleep(0.0007)
time.sleep(1)

for i in range(0,4) :
  for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(hand_in[y]+zero_offset[y],50,4)
   time.sleep(0.0007)
  time.sleep(0.5)
  for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(hand_out[y]+zero_offset[y],50,4)
   time.sleep(0.0007)
  time.sleep(0.5) 
################### WAVE


i=0
if i<1:
        l_shoulder_pitch.set_servo_angle(0,100,4)
        time.sleep(0.0007)
        l_arm_roll.set_servo_angle(90,100,4)
        time.sleep(0.0007)
        l_low_arm_roll.set_servo_angle(0,100,4)
        time.sleep(0.0007)     
        r_shoulder_pitch.set_servo_angle(0,100,4)
        time.sleep(0.0007)
        r_arm_roll.set_servo_angle(-90,100,4)
        time.sleep(0.0007)
        r_low_arm_roll.set_servo_angle(0,100,4)
        time.sleep(1)
        print("yoo")
        i=i+1
        for j in range(0,2): 
         l_shoulder_pitch.set_servo_angle(0,100,4)
         time.sleep(0.0007)
         l_arm_roll.set_servo_angle(90,100,4)
         time.sleep(0.0007)
         l_low_arm_roll.set_servo_angle(0,100,4)
         time.sleep(0.5)

         l_low_arm_roll.set_servo_angle(-45,100,4)
         time.sleep(0.5)
         l_arm_roll.set_servo_angle(135,100,4)
         time.sleep(0.0007)  
         l_low_arm_roll.set_servo_angle(90,200,4)

         time.sleep(1.5)
         l_low_arm_roll.set_servo_angle(-45,200,4)
         time.sleep(0.0007)
         l_arm_roll.set_servo_angle(68,100,4)
         time.sleep(0.5) 

         l_shoulder_pitch.set_servo_angle(0,100,4)
         time.sleep(0.0007)
         l_arm_roll.set_servo_angle(90,100,4)
         time.sleep(0.0007)
         l_low_arm_roll.set_servo_angle(0,100,4)
         time.sleep(0.0007) 
         time.sleep(1) 

 ######################################################################################
         r_shoulder_pitch.set_servo_angle(0,100,4)
         time.sleep(0.007)
         r_arm_roll.set_servo_angle(-90,100,4)
         time.sleep(0.007)
         r_low_arm_roll.set_servo_angle(0,100,4)
         time.sleep(0.5)

         r_low_arm_roll.set_servo_angle(-90,100,4)
         time.sleep(0.007)
         r_arm_roll.set_servo_angle(-135,100,4)
         time.sleep(1)
         r_low_arm_roll.set_servo_angle(-90,200,4)
         time.sleep(0.007)

  
         r_arm_roll.set_servo_angle(-45,100,4)
         time.sleep(0.0007)
         r_low_arm_roll.set_servo_angle(75,200,4)
         time.sleep(2)

         r_arm_roll.set_servo_angle(-90,100,4)
         time.sleep(0.0007)
         r_low_arm_roll.set_servo_angle(0,200,4)
         time.sleep(0.5)


################## BOW_DOWN
bend_down=[0,32,-40,-22,0,0,-32,40,22,0,
100,14,50,10,-73,-25
]
inter = [0,10,-10,-8,0,0,-10,10,8,0,
100,70,0,0,-70,-100
]
stand=[0,10,-10,-8,0,0,-10,10,8,0,
77,30,50,-7,-100,-25
]
for i in range (0,1):
  for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(bend_down[y]+zero_offset[y],200,4)
   time.sleep(0.0007)
  time.sleep(2.5)
  for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(inter[y]+zero_offset[y],200,4)
   time.sleep(0.0007)
  time.sleep(2.5)
  for y in range (0,motor_no):
   herkulex.servo(motor_id[y]).set_servo_angle(stand[y]+zero_offset[y],200,4)
   time.sleep(0.0007)
  time.sleep(2.5)
####################
 

def talker():
 
######################
  
 herkulex.close()
if __name__ == '__main__':
    try:
       talker()
    except rospy.ROSInterruptException:
       pass
