import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_eye.xml') # a face rec. programhoz hasonlóan ez nem az arcot, hanem a szemeket ismeri fel

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
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) # Zöld színű lesz a kirajzolt téglalap (R, G = 255, B)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    
    cv2.imshow('video',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()