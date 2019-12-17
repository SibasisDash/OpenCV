import numpy as np
import cv2

detector = cv2.CascadeClassifier('C:\\Users\\user\\PycharmProjects\\OpenCV\\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while (True):
    ret, img = cap.read()
    # cascade classifier can read grey so convert RGB to monocolour
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        # create a rectangle with coordinates x,y,x+w,y+h ; B = 255, G,R, width = 2
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 137, 100), 2)

    cv2.imshow('face', img)
    # wait for 1 millisecond and exit by clicking 'q'
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()