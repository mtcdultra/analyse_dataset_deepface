import os
import tools
import pandas as pd
import numpy as np
import cv2

##################### TEST VALUES #####################
path_to_save_csv_file = '/Users/mtcd/Downloads/MEAD_DATASET/mead_100'
path_frame_files = '/Users/mtcd/Downloads/mead_frames_100_perc'
name_to_save_csv = 'mead_csv_frames_100_60x60'
dimension_1 = 60
dimension_2 = 60
#######################################################

#######################################################
#path_to_save_csv_file = tools.create_folder()
#path_frame_files = input('Type the path where the frame files are: ')
#name_to_save_csv = input('Type a name to save the CSV file (Do not type the extension file): ')
#######################################################

dirs = tools.split_train_and_test_csv(path_frame_files)
qty_files_init, qty_files = len(dirs), len(dirs)
file_csv = os.path.join(path_to_save_csv_file, name_to_save_csv + '.csv')

print(file_csv)

with open(file_csv, 'w') as f:
    f.write('emotion,pixels,usage\n')
    for file_name in dirs:
        usage = file_name[1]
        file_name = file_name[0]

        if file_name == '.DS_Store': continue
        print(f'{name_to_save_csv} - ({qty_files_init}/{qty_files})')
        qty_files -= 1
        person_dir = os.path.join(path_frame_files, file_name)
        image = cv2.imread(person_dir)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #transform image to gray scale
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

        detected_face = image[int(y):int(y+h), int(x):int(x+w)] #crop detected face
        detected_face = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY) #transform to gray scale
        detected_face = cv2.resize(detected_face, (dimension_1, dimension_2))
        
        detected_face = detected_face.reshape(-1)
        image_str = [str(pix) for pix in detected_face]   # convert image pixels to str
        image_str = ' '.join(image_str)
        emotion = tools.define_emotion_from_file_name(file_name)
        f.write('%d,%s,%s' % (emotion, image_str, usage))
        f.write('\n')

    # converting the pixels from string to np array
    print('Finished extraction')
    print('Converting to np array')
    pdata = pd.read_csv(file_csv)

    pdata['pixels'] = pdata['pixels'].apply(
        lambda image_px: np.fromstring(image_px, sep=' ')
    )

print('completed process')