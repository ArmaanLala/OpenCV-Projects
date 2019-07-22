import numpy
import cv2

cap = cv2.VideoCapture(0) #Captures image


while True:
    ret, frame = cap.read()
    cv2.imshow('frame',frame) #Displays Image

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

#Release all the windows when everything is done
cap.release()
cv2.destroyAllWindows()