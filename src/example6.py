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

#importing service
from ros_workshop.srv import Test, TestRequest

class Service(object):
    """
    """

    def __init__(self, ):
        """
        """
        self.service_ = rospy.ServiceProxy("/test5/service", Test)

    def call_srv(self, string):
        req = TestRequest()
        req.input = string
        result = self.service_.call(req)
        print "Service returned: ", result.output


rospy.init_node("test6")
service = Service()
user_msg = raw_input()
service.call_srv(user_msg)
