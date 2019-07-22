import numpy
import cv2

cap = cv2.VideoCapture(0)

def changeResolution(width,height):
    cap.set(3,width)
    cap.set(4,height)

changeResolution(640/2,480/2)

while True:
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    cv2.imshow('frame1',frame)
    cv2.imshow('frame2',frame)
    cv2.imshow('frame3',frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()