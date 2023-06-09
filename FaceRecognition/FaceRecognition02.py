import cv2
import numpy as np
from PIL import Image # pip install pillow (ha írja a warning-ot)
import os

path = 'C:\Python\Ipar_beadando\FaceRecognition\dataset' # elérési útja az előző programban mentett képeknek
recognizer = cv2.face.LBPHFaceRecognizer_create() # ha azt a hibát dobja, hogy "cv2" has no attribute 'face' -> pip install opencv_contrib_python (ha le van töltve akkor először uninstall, majd install)
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml");

# a függvény a dataset mappán belüli összes fotót szétszedi 2 tömbre: ID-k és arcok (faces)
def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L') # szürkeárnyalatos képeket tanul meg a program!
        img_numpy = np.array(PIL_img,'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples,ids

faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))
recognizer.write('C:/Python/Ipar_beadando/FaceRecognition/trainer/trainer.yml') # nagyon fontos a pontos path megadása minden esetben!!!!
print("\n {0} arc megtanulva.".format(len(np.unique(ids))))