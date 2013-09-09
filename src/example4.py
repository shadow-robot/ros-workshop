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

class SubscribeAndPublish(object):
    """
    """

    def __init__(self, ):
        """
        """
        self.pub_ = rospy.Publisher("~output", Float64)
        self.last_msg_ = Float64()

        self.sub_ = rospy.Subscriber("~input", Float64, self.msg_cb_)

        self.timer = rospy.Timer(rospy.Duration(0.1), self.timer_cb_)

    def msg_cb_(self, msg):
        self.last_msg_.data = msg.data

    def timer_cb_(self, event):
        self.pub_.publish(self.last_msg_.data * 2.0)


rospy.init_node("test4")
sub_and_pub = SubscribeAndPublish()
rospy.spin()
