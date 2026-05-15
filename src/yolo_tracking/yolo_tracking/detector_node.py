import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from yolo_tracking.yolov8_tracking import YOLODetector


class DetectorNode(Node):
    def __init__(self):
        super().__init__("detector_node")

        self.bridge = CvBridge()
        self.detector = YOLODetector()

        self.sub = self.create_subscription(
            Image, "/camera/image_raw", self.callback, 10
        )

        self.pub = self.create_publisher(Image, "/camera/detection", 10)

    def callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")

        # 🔥 roda YOLO
        frame = self.detector.process(frame)

        out = self.bridge.cv2_to_imgmsg(frame, "bgr8")
        self.pub.publish(out)


def main(args=None):
    rclpy.init(args=args)
    node = DetectorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
