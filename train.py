import cv2
import os
import numpy as np
import os
import time


trainDir = r"dataset/Train"
testDir = r"dataset/Test"

recognizer = cv2.face.LBPHFaceRecognizer_create()
face_detector = cv2.CascadeClassifier('frontal_face_default.xml')
epoch = 5

trainingImagePaths = [os.path.join(trainDir,f) for f in os.listdir(trainDir)] 
testingImagePaths =  [os.path.join(testDir,f) for f in os.listdir(testDir)] 

def getImageAndId(adr):
    imagePaths = [os.path.join(adr,f) for f in os.listdir(adr)]
    faceSamples=[]
    ids = []
    for imagePath in imagePaths:
        id = int(os.path.split(imagePath)[-1].split(".")[1])

        img = cv2.imread(imagePath)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_detector.detectMultiScale(img)
        for (x,y,w,h) in faces:
            faceSamples.append(img[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples, ids


# Training
print("Training Faces ...", end="")

trainFaces, ids = getImageAndId(trainDir)
copyTrainFace, copyIds = getImageAndId(trainDir)

print(len(trainFaces), len(ids))
print(len(copyTrainFace), len(copyIds))

for _ in range(epoch):
    trainFaces.extend(copyTrainFace)
    ids.extend(copyIds)

print(len(trainFaces), len(ids))
recognizer.train(trainFaces, np.array(ids))
recognizer.save('trainer/trainer.yml')
total_faces = len(np.unique(ids))

print(f"\r{total_faces} Faces Trained Successfuly 😁")
