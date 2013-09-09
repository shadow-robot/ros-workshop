#!/usr/bin/env python


'''
 @file   example3.py
 @author Ugo Cupcic <software@shadowrobot.com>

 Copyright (c) 2013 Shadow Robot Company Ltd.
  All rights reserved.

 This code is proprietary and may not be used, copied, distributed without
  prior authorisation and agreement from Shadow Robot Company Ltd.


 @brief
'''

#importing the package dependencies - always necessary, use package name
import roslib; roslib.load_manifest("ros_workshop")
import rospy
from time import sleep
#importing messages: from package_name.msg import MsgName
from std_msgs.msg import Float64

#initialises the node (registers with master)
rospy.init_node("test3")

#advertises a topic
pub = rospy.Publisher("/test", Float64)

#one shot publisher = BAD
pub.publish(1.0)
sleep(1)
