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

rospy.init_node("test7")

test_param = rospy.get_param("~param", 100) #default value

rospy.loginfo("Test param = "+str(test_param))
