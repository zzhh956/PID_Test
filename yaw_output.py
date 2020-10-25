#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64MultiArray
import pid_class

pid = pid_class.PID(2, 0.1, 0.2)
motor = [0.0]*8  # 1-4 A-D

#       1-4 up/down
#       A-D direction
#               
#     <-        u       <-
#      A        1        D
#       -----------------
#       |               |
#    u  |               |  u
#    2  |               |  4
#       |               |
#       |               |
#       -----------------
#      B        3        C
#     <-        u       <-
        
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "%s", data.data)
    feedback = pid.update(data.data[1])
    print(feedback)
    update_motor(feedback)
    talker()

def listener():
    rospy.Subscriber("imu_data", Float64MultiArray, callback)
    rospy.spin()

def update_motor(yaw_value):
    #yaw
    if yaw_value > 0:
        for i in range (4, 8):
            motor[i] = 5
    elif yaw_value < 0:
        for i in range (4, 8):
            motor[i] = -5

def talker():
    rospy.loginfo(Float64MultiArray(data = motor))
    pub.publish(Float64MultiArray(data = motor))

if __name__ == '__main__':
    rospy.init_node('pid', anonymous=True)
    pub = rospy.Publisher('Motors_Force', Float64MultiArray, queue_size=10)
    listener()