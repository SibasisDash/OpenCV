import cv2
import numpy as np

capture = cv2.VideoCapture(0)

if(capture.isOpened()==False):
    print("Error opening")

while(True):
    ret,frame = capture.read()
    if ret==True:
        cv2.imshow("video",frame)
        if cv2.waitKey(1) == 27:
            break
    else:
        break
capture.release()
cv2.destroyAllWindows()