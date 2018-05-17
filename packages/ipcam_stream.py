from urllib.request import urlopen
import cv2
import numpy as np
import time

def VideoCamera():
    # Replace the URL with your own IPwebcam shot.jpg IP:port
    url='http://192.168.0.103:8080/video'

    while True:

        # Use urllib to get the image and convert into a cv2 usable format
        imgResp=urlopen(url)
        imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
        img=cv2.imdecode(imgNp,-1)

        # put the image on screen
        cv2.imshow('IPWebcam',img)

        #To give the processor some less stress
        #time.sleep(0.1) 

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break