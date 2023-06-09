import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # cv2.data.haarcascades <- enélkül nem működik a program!!!! nem tudja beolvasni a scriptet
face_id = input('\n Írd be az ID-d, nyomj Entert és várj! ==>  ')
count = 0 # segédváltozó, ami azért kell hogy a mentett képek címei ne keveredjenek össze
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1
        cv2.imwrite("C:\Python\Ipar_beadando\FaceRecognition\dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        # PONTOSAN!!!! meg kell adni a mappa helyét, ahová elmenti a program a képeket
        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    elif count >= 15: # ennyi képet csinál a program
         break
cam.release()
cv2.destroyAllWindows()