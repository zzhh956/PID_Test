#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64MultiArray

def talker():
    pub = rospy.Publisher('imu_data', Float64MultiArray, queue_size=10)
    rospy.init_node('imu', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        roll = 0.0
        yaw = 0.2
        pitch = 0.0
        imu_vector = [roll, yaw, pitch]

        rospy.loginfo(Float64MultiArray(data = imu_vector))
        pub.publish(Float64MultiArray(data = imu_vector))
        rate.sleep()
 
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass