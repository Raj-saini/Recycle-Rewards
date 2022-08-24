
import cv2 
import pyzbar.pyzbar as pyzbar
import numpy as np
import time 

cap = cv2.VideoCapture(0)
cap.set(3, 700)  # 3- width
cap.set(4, 700) # 4- height 
used_codes = []
camera = True
while camera == True:
    _, frame = cap.read()
    decodedObjects = pyzbar.decode(frame)
    # success, frame = cap.read()
    
    for code in decodedObjects:
        if code.data.decode('utf-8') not in used_codes:
            print('Approved, You can enter')
            print(code.data.decode('utf-8'))
            used_codes.append(code.data.decode('utf-8'))
            time.sleep(5)
        elif code.data.decode('utf-8') in used_codes:
            print('Sorry, this code has been already used!')
            time.sleep(5)
        else:
            print("Code reading errro ")

    cv2.imshow('Testing -code-scan', frame)
    key = cv2.waitKey(1)
    if key == 1:
        break
   
   
   



