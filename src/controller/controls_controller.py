
class ControlsController():
    
    def __init__(self, player=None):
        self.__view__ = None
        
        self.__player__ = player
        
        self.status_webcam = True # experimental
        self.status_picam = True  # experimental
        self.status_video = True  # experimental
    
    def set_view(self, view):
        self.__controls_view__ = view
        
    def launch_webcamera(self):
        if self.status_webcam:
            self.status_webcam = False
            self.__controls_view__.disable_btn_picamera()
            self.__controls_view__.disable_btn_video()
            self.__controls_view__.disable_cbx_video_source()
            self.__controls_view__.set_label_btn_webcamera('Stop WebCamera')
        else:
            self.status_webcam = True
            self.__controls_view__.enable_btn_picamera()
            self.__controls_view__.enable_btn_video()
            self.__controls_view__.enable_cbx_video_source()
            self.__controls_view__.set_label_btn_webcamera('Start WebCamera')
    
    def launch_picamera(self):
        if self.status_picam:
            self.status_picam = False
            self.__controls_view__.disable_btn_webcamera()
            self.__controls_view__.disable_btn_video()
            self.__controls_view__.disable_cbx_video_source()
            self.__controls_view__.set_label_btn_picamera('Stop PiCamera')
        else:
            self.status_picam = True
            self.__controls_view__.enable_btn_webcamera()
            self.__controls_view__.enable_btn_video()
            self.__controls_view__.enable_cbx_video_source()
            self.__controls_view__.set_label_btn_picamera('Start PiCamera')

    def launch_video(self):
        if self.status_video:
            self.status_video = False
            self.__controls_view__.disable_btn_webcamera()
            self.__controls_view__.disable_btn_picamera()
            self.__controls_view__.disable_cbx_video_source()
            self.__controls_view__.set_label_btn_video('Stop video')
        else:
            self.status_video = True
            self.__controls_view__.enable_btn_webcamera()
            self.__controls_view__.enable_btn_picamera()
            self.__controls_view__.enable_cbx_video_source()
            self.__controls_view__.set_label_btn_video('Start video')
