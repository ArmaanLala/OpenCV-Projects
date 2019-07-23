import numpy
import cv2


face_cascade = cv2.CascadeClassifier('cascades/haarcascades/haarcascade_frontalface_alt.xml')
eye_cascase = cv2.CascadeClassifier('cascades/haarcascades/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('cascades/haarcascades/haarcascade_smile.xml')
cap = cv2.VideoCapture(0) #Captures image

def changeResolution(width,height):
    cap.set(3,width)
    cap.set(4,height)

# changeResolution(320,240)

while True:
    ret, frame = cap.read()
    gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(gray,scaleFactor=1.5, minNeighbors=5)

    for (x,y,w,h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        img_item = "my-image.png"
        cv2.imwrite(img_item,roi_gray)

        color =(255,0,0)
        stroke = 2
        end_cord_x = x+w
        end_cord_y = y+h
        cv2.rectangle(frame, (x,y), (end_cord_x,end_cord_y),color,stroke )
        eyes = eye_cascase.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey ),(ex+ew,ey+eh),(0,255,0),1)
        # smile = smile_cascade.detectMultiScale(roi_gray)
        # for (sx,sy,sw,sh) in smile:
        #     cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh), (0,0,255),1)

    cv2.imshow('frame',frame) #Displays Image
    cv2.imshow('Gray',gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

#Release all the windows when everything is done
cap.release()
cv2.destroyAllWindows() 