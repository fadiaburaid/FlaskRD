import numpy as np
from PIL import ImageGrab
import cv2


class VideoScreen(object): 
    def get_frame(self):
        screen =  np.array(ImageGrab.grab())
        image=cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
        image=cv2.resize(image,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()   
