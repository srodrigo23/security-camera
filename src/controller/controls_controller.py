import os

class ControlsController():
    """
    All bussines logic of controls of screen, start video, start camera
    """
    def __init__(self, camera, screen_controller):
        """
        MVC Pattern view none to set after
        """
        self.__view__ = None
        self.__camera__ = camera # to control camera stop/play
        self.__screen_controller__ = screen_controller # to change screen start and end execution
        self.__path_system__ = os.path.abspath('.') # path system to read videos
    
    def set_view(self, view):
        # to control frame controls
        self.__controls_view__ = view
        
    def launch_webcamera(self):
        """
        Launch web camera
        """
        if self.__camera__.is_none():
            self.__camera__.set_webcam()
            self.__camera__.start()
            self.__controls_view__.disable_btn_picamera()
            self.__controls_view__.disable_btn_video()
            self.__controls_view__.disable_cbx_video_source()
            self.__controls_view__.set_label_btn_webcamera('Stop WebCamera')
            
            self.__screen_controller__.start_show_frames()
        else:
            self.__camera__.stop() # stop to show frames too
            self.__controls_view__.enable_btn_picamera()
            self.__controls_view__.enable_btn_video()
            self.__controls_view__.enable_cbx_video_source()
            self.__controls_view__.set_label_btn_webcamera('Start WebCamera')
    
    def launch_picamera(self):
        """
        Launch pi camera
        """
        if self.__camera__.is_none():
            try:
                self.__camera__.set_picam()
            except ModuleNotFoundError:
                self.__controls_view__.show_rpi_support_error('Raspberry Pi Camera not supported')
                return
                
            self.__camera__.start()
            self.__controls_view__.disable_btn_webcamera()
            self.__controls_view__.disable_btn_video()
            self.__controls_view__.disable_cbx_video_source()
            self.__controls_view__.set_label_btn_picamera('Stop PiCamera')
            
            self.__screen_controller__.start_show_frames()
            
        else:
            self.__camera__.stop()  # stop to show frames too
            self.__controls_view__.enable_btn_webcamera()
            self.__controls_view__.enable_btn_video()
            self.__controls_view__.enable_cbx_video_source()
            self.__controls_view__.set_label_btn_picamera('Start PiCamera')

            
    def launch_video(self, video_selected):
        """
        launch video with video path
        """
        if self.__camera__.is_none():    
            __path_video_selected__ = os.path.sep.join([self.__path_system__, 'video', video_selected])
            self.__camera__.set_webcam(src=__path_video_selected__)
            self.__camera__.start()
            self.disable_behaviour_launch_video()
            
            self.__screen_controller__.start_show_frames()
        else:
            self.__camera__.stop()
            self.enable_behaviour_launch_video()
    
    def disable_behaviour_launch_video(self):
        """
        Disable buttons controls when start a video or camera
        """
        self.__controls_view__.disable_btn_webcamera()
        self.__controls_view__.disable_btn_picamera()
        self.__controls_view__.disable_cbx_video_source()
        self.__controls_view__.set_label_btn_video('Stop Video')
        
    def enable_behaviour_launch_video(self):
        """
        Enable buttons controls when stop camera or video 
        """
        self.__controls_view__.enable_btn_webcamera()
        self.__controls_view__.enable_btn_picamera()
        self.__controls_view__.enable_cbx_video_source()
        self.__controls_view__.set_label_btn_video('Start video')
    
    def get_videos(self):
        """
        Return list of videos in the path 
        """
        return os.listdir(os.path.sep.join([self.__path_system__, 'video']))