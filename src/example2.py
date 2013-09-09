#!/usr/bin/env python


'''
 @file   example2.py
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

#simple system sleep
from time import sleep

#importing messages: from package_name.msg import MsgName
from std_msgs.msg import Float64

#initialises the node (registers with master)
rospy.init_node("test_2")

def callback(msg):
    print "Received: ", msg.data

#subscribes to a topic, gives callback function
sub = rospy.Subscriber("/test", Float64, callback)

#Stay alive for receiving the data
while not rospy.is_shutdown():
    sleep(1)
