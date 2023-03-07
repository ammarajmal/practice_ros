#!/usr/bin/env python3
"""Run talker and listener nodes."""""

import rospy
import roslaunch
PACKAGE = 'my_pkg'

node_talker = roslaunch.core.Node(PACKAGE, 'talker.py')
listener_node = roslaunch.core.Node(PACKAGE, 'listener.py')

launch = roslaunch.scriptapi.ROSLaunch()
launch.start()

process_1 = launch.launch(node_talker)
process_2 = launch.launch(listener_node)


rospy.sleep(15)
process_1.stop()
process_2.stop()
process_1.stop()
