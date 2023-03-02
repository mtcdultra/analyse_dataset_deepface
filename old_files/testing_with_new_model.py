from deepface import DeepFace
import os
import cv2

path = '/Users/mtcd/Downloads/TESTE_MEAD_DATASET/temp'

for folder, subfolder, files in os.walk(path):            
    for file in files:
        try:             
            face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            img = cv2.imread(os.path.join(path, file))
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #transform image to gray scale
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                #print(x,y,w,h)
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                cv2.imshow('img',img)
           
            detected_face = img[int(y):int(y+h), int(x):int(x+w)] #crop detected face
            detected_face = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY) #transform to gray scale
            detected_face = cv2.resize(detected_face, (48, 48)) #resize to 48x48
            print(detected_face.size)
            #print('$$$')
            obj = DeepFace.analyze(os.path.join(path, file), actions = ['emotion'],enforce_detection=False)['dominant_emotion']
            #print('###')
            #print(file)
            print(f'{obj} - {file}')

        except:
            next