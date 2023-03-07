#!/usr/bin/env python3
"""Run talker and listener nodes."""""

import roslaunch
import rospy
import rospkg
launch_path = rospkg.RosPack().get_path('my_pkg')
rospy.init_node('run_talk_listen_launch', anonymous=False)
uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
roslaunch.configure_logging(uuid)
lauch_file = roslaunch.parent.ROSLaunchParent(
    uuid, [f"{launch_path}/launch/talk_listen.launch"])
lauch_file.start()
rospy.loginfo("Launched talker and listener nodes")
rospy.sleep(4)
lauch_file.shutdown()
