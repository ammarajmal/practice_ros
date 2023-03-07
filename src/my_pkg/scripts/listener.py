#!/usr/bin/env python3
import contextlib
import rospy
from std_msgs.msg import String

def callback(data):
    """Callback function for subscriber"""
    rospy.loginfo(f"The Listener has heard msg: {data.data}")

def listener():
    """Listener Node"""
    rospy.init_node('my_listener_node', anonymous=True)
    rospy.Subscriber('my_chatter_topic', String, callback)
    rospy.spin()
    
if __name__ == '__main__':
    with contextlib.suppress(rospy.ROSInterruptException):
        listener()

