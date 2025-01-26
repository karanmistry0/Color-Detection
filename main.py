import os
import cv2
from util import get_limits
from PIL import Image

# Read Video
cam = cv2.VideoCapture(0)
yellow = [0,255,255] # yellow in BGR colorspace
while True:
    ret,frame = cam.read()

    hsvImage = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_limit,upper_limit = get_limits(color = yellow)
    print(lower_limit,upper_limit)
    mask = cv2.inRange(hsvImage,lower_limit,upper_limit)

    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    print(bbox)

    if bbox is not None:
        x1,y1,x2,y2 = bbox
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

    cv2.imshow('Color Detection',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()