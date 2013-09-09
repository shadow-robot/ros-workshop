#!/usr/bin/env python


'''
 @file   example1.py
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

#importing messages: from package_name.msg import MsgName
from std_msgs.msg import Float64

#initialises the node (registers with master)
rospy.init_node("test")

#advertises a topic
pub = rospy.Publisher("/test", Float64)

#publishing at fixed rate
rate = rospy.Rate(10)

#Check if ROS is killed
while not rospy.is_shutdown():
    #actually publish the message
    pub.publish(1.0)
    rate.sleep()
