#!/usr/bin/env python3.6

import rclpy
import anki_vector
import threading
import os
import sys

from vector_ros_driver.vector import Vector
from vector_ros_driver.anim import Animation
from vector_ros_driver.drive import Drive
from vector_ros_driver.camera import Camera
from vector_ros_driver.behavior import Behavior
from vector_ros_driver.tf import JointStatesPublisher

def main(args):
    rospy.init_node("vector")

    # use mock robot object if required
    if rclpy.get_param_or("use_mock", False):
        rospy.loginfo("using mock!")
        sys.path.append(os.path.join(os.path.dirname(__file__), "..", "test"))
        import mock_robot
        async_robot = mock_robot.MockRobot()

    else:
        async_robot = anki_vector.AsyncRobot(enable_camera_feed=True)

    # connect to Vector
    async_robot.connect()

    # start all using shared AsyncRobot object
    Vector(async_robot)
    Animation(async_robot)
    Behavior(async_robot)

    # these services require threads to run(and publish) in parallel
    drive_thread = threading.Thread(target=Drive, args=(async_robot,))
    drive_thread.start()

    camera_thread = threading.Thread(target=Camera, args=(async_robot,))
    camera_thread.start()

    tf_thread = threading.Thread(target=JointStatesPublisher, args=(async_robot,))
    tf_thread.start()

    rospy.spin()

if __name__=="__main__":
    sys.exit(main(sys.argv))
