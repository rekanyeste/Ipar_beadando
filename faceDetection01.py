import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml') # beolvassa az előre megírt arcfelismerőt, amit le lehet tölteni, a Cascades mappa tartalmazza
eyeCascade = cv2.CascadeClassifier('Cascades/haarcascade_eye_tree_eyeglasses.xml') # ez a fajta eyedetection jobban működik szemüveggel

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
while True: #ahhoz, hogy 'real-time' legyen a kamera, while-true 'végtelen' ciklust kell írnunk, amiből egy sima break-kel kell kilépnünk
    
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(
        gray, # kamera kép
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20) # mekkora méretű a négyzet, amit az alábbi ciklus rajzol ki:
    )
    eyes = eyeCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20)
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) # x, y a négyzet egy pontja, szélesség: w, magasság: h + RGB színek
        roi_color = img[y:y+h, x:x+w] # a kirajzolja a négyzetet
    for (x,y,w,h) in eyes:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) # Zöld színű lesz a kirajzolt téglalap (R, G = 255, B)
        roi_color = img[y:y+h, x:x+w]
    
    cv2.imshow('video',img) # a for cikluson kívül ha az imshow függvénynek paraméterben megadjuk az előző változót akkor a kamerán megjeleníti a négyzetet
    
    k = cv2.waitKey(30) & 0xff # 'ESC' lenyomásával kibreakel a while-true ciklusból
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()