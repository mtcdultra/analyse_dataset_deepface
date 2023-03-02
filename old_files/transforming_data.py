import os
import pandas as pd
import numpy as np
import shutil
import csv

### CREATE PANDAS DATAFRAME WITH SUMMARY

def summary():

    persons = ['M005', 'M007', 'M009', 'M011', 'M013', 'M023', 'M024', 'W011', 'W019', 'W027', 'W035']
    emotions = ['angry', 'disgusted', 'fear', 'neutral', 'sad', 'surprised', 'happy']

    path_frame_files = '/Volumes/HD_03/MEAD/Frames_MEAD'

    dirs = os.listdir(path_frame_files)

    emotions_data, persons_data = [], []
    for file in dirs:
        for person in persons:
            if person in file:
                persons_data.append(person)
        for emotion in emotions:
            if emotion in file:
                emotions_data.append(emotion)

    whole_data = list(zip(persons_data, emotions_data))
    data = pd.DataFrame(whole_data, columns=['person','emotion'])

    print(data.groupby('person').count())
    print(data.groupby('emotion').count())

### ----------------------------------------------------------------------------

### DELETE FILES WITH CONTEMPT EMOTION ( THIS EMOTION HASN'T IN DEEPFACE LIBRARY )

def delete_files_contempt():
    path_frame_files = '/Volumes/HD_03/MEAD/Frames_MEAD' 
    count = 0
    for file in dirs:
        if 'contempt' in file:
            count = count +1
            if os.path.exists(os.path.join(path_frame_files, file)):
                os.remove(os.path.join(path_frame_files, file))

    print(count)

### ----------------------------------------------------------------------------

### MOVING FILES FROM LOCAL HD TO EXTERNAL HD AND DELETE FILE IF IN LOCAL IS THE SAME IN EXTERNAL 

original_path = '/Users/mtcd/Downloads/mead_frames'
destination_path = '/Volumes/HD_03/MEAD/Frames_MEAD'

dirs = os.listdir(original_path)
qty = len(dirs)
print('Total of files: ', str(len(dirs)))
for file in dirs:
    try:
        shutil.move(os.path.join(original_path, file), destination_path)        
    except:
        print('File already exists')
        os.remove(os.path.join(original_path, file))
        next
    qty = qty - 1
    print(f'{qty} to finish')

### ----------------------------------------------------------------------------

### SAVE THE FILE NAME IN CSV FILE
### THIS CODE IS IMPORTANT TO SEPARATE THE TRAIN AND TEST FILES TO ALGORITHM

original_path = '/Volumes/HD_03/MEAD/Frames_MEAD'
csv_file_name = 'mead_files_frames.csv'

dirs = os.listdir(original_path)
qty = len(dirs)

with open(csv_file_name, 'w') as f:
    f.write('file_name\n')
    for file_name in dirs:
        print(file_name)
        write = csv.writer(f)        
        write.writerow([file_name])

### ----------------------------------------------------------------------------

### SPLIT 80% OF FRAMES TO TRAIN AND 20% TO TEST
### USING THE CSV FILE CREATED IN PREVIOUS CODE
### GENERATE SEPARETE CSV FILES TO TRAIN AND TEST WITH FILE NAME

def split_train_and_test_csv():

    csv_file_name = 'mead_files_frames.csv'
    df = pd.read_csv(csv_file_name)
    
    csv_file_name_training = 'mead_files_frames_training.csv'
    csv_file_name_test = 'mead_files_frames_test.csv'
    
    msk = np.random.rand(len(df)) < 0.8 
    train = df[msk]
    test = df[~msk]

    print(str(train.count()) + ' files to training')
    print(str(test.count()) + ' files to test')

    ### CREATING TRAINING CSV FILE
    with open(csv_file_name_training, 'w') as f:
        usage = 'Training'     
        f.write('file_name,usage\n')        
        for file_name in train['file_name']:
            write = csv.writer(f)
            write.writerow([file_name,usage])

    ### CREATING TEST CSV FILE
    with open(csv_file_name_test, 'w') as f:
        usage = 'Test'
        f.write('file_name,usage\n')        
        for file_name in test['file_name']:
            write = csv.writer(f)
            write.writerow([file_name,usage])

### ----------------------------------------------------------------------------

### CREATE TEST AND TRAIN FOLDER AND INCLUDE FILES IN RESPECTIVE FOLDER
### USE THE TRAIN AND TEST VARIABLES GENERATED FROM PANDAS

original_path = '/Volumes/HD_03/MEAD/Frames_MEAD'

csv_file_name = 'mead_files_frames_test.csv'
list_of_files = pd.read_csv(csv_file_name)
folder_name = 'test_files'

qty = list_of_files.count()

for file in list_of_files['file_name']:    
    if file == '.DS_Store': continue
    if not os.path.exists(os.path.join(original_path, folder_name)):
        os.mkdir(os.path.join(original_path, folder_name))
    try:
        shutil.move(os.path.join(original_path, file), os.path.join(original_path, folder_name))
    except:
        continue
print('Finished')




    
