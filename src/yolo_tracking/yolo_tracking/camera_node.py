import rclpy
from rclpy.node import Node
import cv2

from sensor_msgs.msg import Image
from cv_bridge import CvBridge


class CameraNode(Node):
    def __init__(self):
        super().__init__("camera_node")

        self.pub = self.create_publisher(Image, "/camera/image_raw", 10)
        self.bridge = CvBridge()

        self.cap = cv2.VideoCapture(0)
        self.timer = self.create_timer(0.03, self.loop)

    def loop(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        msg = self.bridge.cv2_to_imgmsg(frame, "bgr8")
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = CameraNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
