import cv2
import os
import shutil
import pandas as pd
import numpy as np

# --------------------------------------------------------------------------------
def create_folder():
    actual_path = os.getcwd()
    folder_name = input('Type the folder name to save the file(s): ')

    try:
        if not os.path.exists(os.path.join(actual_path, folder_name)):
            os.makedirs(os.path.join(actual_path, folder_name))
            print('Directory created')
        else:
            print('Directory already exists')
    except OSError:
        print('Error: Could not create directory')
    return os.path.join(actual_path, folder_name)

# --------------------------------------------------------------------------------
def get_the_file_path(path):
    """ 
        To returne a list with files to iterate 
    """
    
    list_files = []
    for folder, subfolder, files in os.walk(path):        
        if len(files) > 0:
            for j in files:
                if '.DS_Store' in j: continue
                list_files.append(folder + '/' + j)
    return list_files

# --------------------------------------------------------------------------------
def convert_value_image(original_value, percentage):
    converted_value_image = int( ( ( 100 - percentage ) / 100 ) * original_value )
    return converted_value_image

# --------------------------------------------------------------------------------
def split_train_and_test_csv(original_path):
    df = pd.DataFrame(os.listdir(original_path))
    msk = np.random.rand(len(df)) < 0.8 
    train = df[msk] 
    train['usage'] = 'Training'
    test = df[~msk]
    test['usage'] = 'Test'
    result = pd.merge(train, test, how='outer')
    
    return result.values.tolist()

# --------------------------------------------------------------------------------

def define_emotion_from_file_name(file_name):
    emotions = ['angry', 'disgusted', 'fear', 'happy', 'sad', 'surprised', 'neutral']
    for emotion in emotions:
        if emotion in str(file_name):
            emotion = emotions.index(emotion)
            break
    return emotion

# --------------------------------------------------------------------------------

def define_emotion_from_file_name_(file_name):
    emotions = ['angry', 'disgusted', 'fear', 'happy', 'sad', 'surprised', 'neutral']
    for emotion in emotions:
        if emotion in str(file_name):
            emotion
            break
    return emotion

# --------------------------------------------------------------------------------

def resize_image(img, scale):
    width = int(img.shape[1] * scale / 100)
    height = int(img.shape[0] * scale / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return resized

# --------------------------------------------------------------------------------

def list_of_files(folder):
    files = []
    for diretorio, subpastas, arquivos in os.walk(folder):        
        if arquivos.index('.DS_Store'):
            files.append(arquivos)
    return files

# --------------------------------------------------------------------------------

def qty_of_files(path):
    for folder, subfolder, file in os.walk(path):
        qty = len(file)
    return qty

# --------------------------------------------------------------------------------

def moving_files_to_folders():
    path_test = '/Users/mtcd/Downloads/@datasets/adfes/test/'

    emotions = ['angry', 'disgust', 'fear', 'neutral', 'sad', 'surprise', 'happy']

    for folder, subfolder, file in os.walk(path_test):
        for i in file:
            for j in emotions:
                if j in i:
                    try:
                        print(folder)
                        shutil.move(folder+i, folder + j)
                    except FileNotFoundError:
                        print('Não encontrado')
    return