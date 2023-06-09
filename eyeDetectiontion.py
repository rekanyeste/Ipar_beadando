import numpy as np
import cv2

# a faceDetection program tartalmazza az alábbi kódnak a funkcióját is!!!

faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
while True: 
    
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(
        gray, 
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20)
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        roi_color = img[y:y+h, x:x+w]
    
    cv2.imshow('video',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()