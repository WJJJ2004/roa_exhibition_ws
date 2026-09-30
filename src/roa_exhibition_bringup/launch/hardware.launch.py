import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    config = os.path.join(
        get_package_share_directory("roa_exhibition_bringup"),
        "config", "hardware_100hz.yaml")
    return LaunchDescription([
        Node(
            package="robstride_hardware_interface",
            executable="hardware_interface_node",
            name="hardware_interface_node",
            parameters=[config],
            output="screen"),
    ])
