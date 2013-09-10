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
from ros_workshop.srv import Test, TestResponse

class Service(object):
    """
    """

    def __init__(self, ):
        """
        """
        self.service_server = rospy.Service("~service", Test, self.service_cb_)

    def service_cb_(self, request):
        print "Received a request: ", request.input
        response = TestResponse()
        response.output = request.input + " " + request.input
        return response


rospy.init_node("test5")
service = Service()
rospy.spin()
