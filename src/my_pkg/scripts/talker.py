#!/usr/bin/env python3
import contextlib
import rospy
from std_msgs.msg import String

def talker():
    """Talker Node"""
    pub = rospy.Publisher('my_chatter_topic', String, queue_size=10)
    rospy.init_node('my_talker_node', anonymous=True)
    rate = rospy.Rate(200) # 200hz
    while not rospy.is_shutdown():
        hello_str = f"My Talker Node : {rospy.get_time()}"
        rospy.loginfo(hello_str)
        print(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    with contextlib.suppress(rospy.ROSInterruptException):
        talker()