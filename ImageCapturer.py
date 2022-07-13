import cv2
from PIL import ImageGrab
import numpy as np

class ImageCapturer(object):
    @staticmethod
    def getBWCapture():
        screen_capture_image = ImageGrab.grab() #x, y, w, h
        current_screen_frame_BGR = np.array(screen_capture_image)
        return cv2.cvtColor(current_screen_frame_BGR, cv2.COLOR_BGR2GRAY)
    
    @staticmethod
    def getColorCapture():
        screen_capture_image = ImageGrab.grab() #x, y, w, h
        current_screen_frame_BGR = np.array(screen_capture_image)
        return cv2.cvtColor(current_screen_frame_BGR, cv2.COLOR_BGR2RGB)
    