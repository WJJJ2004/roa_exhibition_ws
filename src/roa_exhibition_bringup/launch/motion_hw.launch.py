import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    config = os.path.join(
        get_package_share_directory("roa_exhibition_bringup"),
        "config", "motion_player_100hz.yaml")
    return LaunchDescription([
        Node(
            package="roa_motion_player",
            executable="motion_player",
            parameters=[config],
            output="screen"),
    ])
