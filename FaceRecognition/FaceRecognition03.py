import cv2
import numpy as np
import os 

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('C:/Python/Ipar_beadando/FaceRecognition/trainer/trainer.yml') # elérési út!!!!
cascadePath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml" # cv2.data.haarcascades + <- enélkül nem olvas!
faceCascade = cv2.CascadeClassifier(cascadePath);

id = 0
# id=0 -> Senki, id=1 -> Nyeste Reka, ... stb. amelyik id-t választottuk azzal kell most is dolgozni
names = ['Senki', 'Nyeste Reka'] 
cam = cv2.VideoCapture(0)
cam.set(3, 640) 
cam.set(4, 480) 
# meg kell adni egy méretet, amiben felismerje az arcunkat a program
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
while True:
    ret, img =cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
    
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        # confidence = az a százalékos érték, amilyen pontossággal beazonosítja a kamerán lévő arcot a program az előzőekben betanult képek alapján
        if (confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence)) # itt jeleníti meg ha felismeri a megtanult arcot
        else:
            id = "Ismeretlen" # ha nem ismeri fel az arcot a kamerában
            confidence = "  {0}%".format(round(100 - confidence))
        
        cv2.putText(img, str(id), (x+5,y-5), 1, (255,255,255), 2) # az id-hoz társított név (fentebb definiált) kiírása és formázása
        cv2.putText(img, str(confidence), (x+5,y+h-5), 1, (255,255,0), 1) # confidence kiíratás
    
    cv2.imshow('camera',img) 
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

cam.release()
cv2.destroyAllWindows()