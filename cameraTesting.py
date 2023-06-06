import numpy as np
import cv2

cap = cv2.VideoCapture(0) # paraméter: 0 -> a számítógép saját kameráját fogja érzékelni
cap.set(3,640) # szélesség
cap.set(4,480) # magasság
while(True):
    ret, frame = cap.read()
    
    cv2.imshow('frame', frame)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27: # nyomd le az 'ESC' gombot a kilépéshez
        break
cap.release()
cv2.destroyAllWindows()