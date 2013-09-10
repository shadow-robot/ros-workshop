/**
 * @file   test.hpp
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

#pragma once

#include <ros/ros.h>
#include <std_msgs/Float64.h>

namespace shadowrobot
{
  class Workshop
  {
  public:
    Workshop();
    virtual ~Workshop() {};

    void message_cb_(const std_msgs::Float64ConstPtr& msg);

  protected:
    ros::NodeHandle nh_;

    ros::Subscriber sub_;
    ros::Publisher pub_;
  };
}

/* For the emacs weenies in the crowd.
   Local Variables:
   c-basic-offset: 2
   End:
*/
