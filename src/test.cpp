/**
 * @file   test.cpp
 * @author Ugo Cupcic <ugo@shadowrobot.com>
 *
 * Copyright (c) 2013 Shadow Robot Company Ltd.
 *  All rights reserved.
 *
 * This code is proprietary and may not be used, copied, distributed without
 *  prior authorisation and agreement from Shadow Robot Company Ltd.
 *
 * @brief
 *
 *
 */

#include "ros_workshop/test.hpp"

namespace shadowrobot
{
  Workshop::Workshop()
    : nh_("~")
  {
    pub_ = nh_.advertise<std_msgs::Float64>("output", 2);
    sub_ = nh_.subscribe("input", 2, &Workshop::message_cb_, this);
  }

  void Workshop::message_cb_(const std_msgs::Float64ConstPtr& msg)
  {
    double input = msg->data;

    std_msgs::Float64 output_msg;
    output_msg.data = input * 2.0;

    pub_.publish(output_msg);
  }

}

int main(int argc, char *argv[])
{
  ros::init(argc, argv, "testcpp");

  shadowrobot::Workshop workshop;

  ros::spin();

  return 0;
}


/* For the emacs weenies in the crowd.
   Local Variables:
   c-basic-offset: 2
   End:
*/
