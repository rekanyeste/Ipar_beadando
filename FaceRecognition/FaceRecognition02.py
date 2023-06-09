import cv2
import numpy as np
from PIL import Image # pip install pillow (ha írja a warning-ot)
import os

path = 'C:\Python\Ipar_beadando\FaceRecognition\dataset' # elérési útja az előző programban mentett képeknek
recognizer = cv2.face.LBPHFaceRecognizer_create() # ha azt a hibát dobja, hogy "cv2" has no attribute 'face' -> pip install opencv_contrib_python (ha le van töltve akkor először uninstall, majd install)
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml");

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L') # grayscale
        img_numpy = np.array(PIL_img,'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples,ids
print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))
# Save the model into trainer/trainer.yml
recognizer.write('C:/Python/Ipar_beadando/FaceRecognition/trainer/trainer.yml')
# Print the numer of faces trained and end program
print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))