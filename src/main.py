from camera import Camera
from motion_detector import MotionDetector

from arguments import VideoArgument

if __name__ == "__main__":
    vid_arg = VideoArgument()
    source = vid_arg.get_data('p')
    camera = Camera(src=source)
    camera.start()
    motion_detector = MotionDetector(camera=camera)
    motion_detector.detect_motion()