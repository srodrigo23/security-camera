import sys
from settings import Settings
from camera import Camera
from motion_detector import MotionDetector

# vid_arg = VideoArgument()
# source = vid_arg.get_data('p')

def run(params):
    camera = None
    if not params is None:
        if len(params) > 1 :
            if params[1] == "CAM":
                s = Settings()
                s.set_source(sys.argv[1])
                camera = Camera(mode = 'CAM')
            elif params[1]=="PICAM":
                camera = Camera(mode = 'PICAM')
            else:
                print("Error en los argumentos")
        elif len(params) == 1:
            camera = Camera(mode = 'CAM')
        camera.start()
        motion_detector = MotionDetector(camera=camera)
        motion_detector.run()
    else:
        print("Error en la ejecucion")
    
if __name__ == "__main__":
    run(sys.argv)