import cv2
import numpy
import os
import time

total_images_to_collect = 150

trainDir = r"dataset/Train"
testDir = r"dataset/Test"

trainCount = 0
testCount = 0

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

face_id = input('\nEnter the Student ID >>> ')
print("Initializing face capture.", end="")

face_detector = cv2.CascadeClassifier('frontal_face_default.xml')

time.sleep(1)
print("\rLook at Camera and Smile :) 😇", end="")
time.sleep(3)

flag = False
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 1)

    cv2.imshow("Camera", img)
    
    if type(faces)==numpy.ndarray:
        for (x,y,w,h) in faces:
            if (trainCount+testCount)%5:
                trainCount += 1
                cv2.imwrite(f"{trainDir}/Student.{face_id}.{trainCount}.jpg", gray[y:y+h,x:x+w])
                print(f"                                \r{trainCount+testCount} Images Collected", end="")
            else:
                testCount += 1
                cv2.imwrite(f"{testDir}/Student.{face_id}.{testCount}.jpg", gray[y:y+h,x:x+w])
                print(f"                                \r{trainCount+testCount} Images Collected", end="")

    if (cv2.waitKey(100) & 0xff) == 27:
        break
    elif trainCount+testCount >= total_images_to_collect:
         flag = True
         break
    

print("\nDataset created. [Exiting...]") if flag else print("\nFailed to create Dataset. [Exiting...]")
cam.release()
cv2.destroyAllWindows()


