from camera import Camera
from motion_detector import MotionDetector


if __name__ == "__main__":
    # source = '../video/video6.mp4'
    source=0
    camera = Camera(src=source)
    camera.start()
    motion_detector = MotionDetector(camera=camera)
    motion_detector.detect_motion()
    