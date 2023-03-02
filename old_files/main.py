from datetime import datetime
import cv2
from deepface import DeepFace
import json
import os
from collections import Counter
import sqlite3
import csv
from pathlib import Path

def list_of_files(folder, file_type):
    files = []
    for diretorio, subpastas, arquivos in os.walk(folder):
        for arquivo in arquivos:
            if arquivo[-len(file_type):] == file_type:
                files.append(os.path.join(diretorio, arquivo))
    return files

def summarize_emotions(file_name):
    with open(file_name, encoding='utf-8') as json_file:
        dados = json.load(json_file)   

    lista_emocoes = []
    lista_emocoes = list(dados.values())

    return file_name[125:-5], 'Total frames: ' + str(len(lista_emocoes)), Counter(lista_emocoes)

def obtain_file_metadata(path):
    data = cv2.VideoCapture(path) 
    frames = data.get(cv2.CAP_PROP_FRAME_COUNT) 
    fps = int(data.get(cv2.CAP_PROP_FPS)) 
    duration = frames / fps

    return f'Frames: {str(frames)} - FPS {str(fps)} - Duration: {str(duration)}'


def original_emotion_dataset(name):
    if name == 'MEAD':
        original_emotion = ['angry','contempt','disgusted','fear','neutral','sad','surprised','happy']
    if name == 'ADFES-BIV':
        original_emotion = ['anger','contempt','disgust','fear','joy','neutral','sadness','surprise']
    return original_emotion


def define_file_name_to_record(file_name):

    # Get whole path and cut to separate emotion / It will dependes of dolder localization
    file_name_to_record = file_name[22:-4]     # Path in Download folder
    #file_name_to_record = file_name[137:-4]            

    file_name_to_record = file_name_to_record.replace('/', '_')

    return file_name_to_record


# ---------------------------------------------
# Better way to obtain the file name

def define_file_name(path_name):

    file_name = path_name.split('/')[-1:]

    return file_name

# ---------------------------------------------

emotion_default = ['angry','contempt','disgusted','fear','neutral','sad','surprised','happy']

def define_emotion_default_dataset(dataset_name, file_name):

    if dataset_name == 'MEAD':
        emotion_default = ['angry','contempt','disgusted','fear','neutral','sad','surprised','happy']
    else:
        emotion_default = ['angry','contempt','disgust','fear','happy','neutral','sad','surprise']

    for emotion in emotion_default:
        if emotion in file_name:
            emotion
            break

    return emotion
    
def analyse_imag(file_name, dataset_name):

    conn = sqlite3.connect('dataset.db')
    cursor = conn.cursor()

    file_name_to_record = define_file_name_to_record(file_name)

    # Filter to know if the file was already analyzed
    resultado = cursor.execute('SELECT file_name from emotion_record WHERE file_name = ?', [file_name_to_record]).fetchone()
       
    # Emotions from dataset (need to get emotions settings)
    #original_emotion = original_emotion_dataset('MEAD')

    video=cv2.VideoCapture(file_name)
    result_line = {}

    # If the file wasn't analyzed, do analyze
    if resultado is None:
        frame_number = 0
        while video.isOpened():
            _,frame = video.read()
            print(file_name_to_record)
            if frame is not None:
                frame_number += 1
                analyze = DeepFace.analyze(frame,actions=['emotion'], enforce_detection=False)
                dominant_emotion = analyze['dominant_emotion']
                result_line[frame_number] = dominant_emotion
                info_metadata = obtain_file_metadata(file_name)


                with open('./analyzed/' + file_name_to_record + "_face_detection.json", 'w') as outfile:
                    json.dump(result_line, outfile)
            else:
                    print("")
                    break      
            
            # Saving data in TXT file with metadata informations
            with open('./analyzed/' + file_name_to_record +  '_metadata.txt', 'w') as file:
                file.write(info_metadata)

            dominant_emotion = []                
            dominant_emotion = list(result_line.values())
        
        emotion_analysed_from_mead_dataset = dict(Counter(dominant_emotion))

        

        # Saving data in database
        for i in emotion_analysed_from_mead_dataset.items():
            emotion = i[0]
            classification = i[1]
            original_emotion = define_emotion_default_dataset(dataset_name, file_name_to_record)
            to_db = [file_name_to_record, emotion, classification, dataset_name, original_emotion]

            cursor.execute('INSERT INTO emotion_analysed_mead_dataset (file_name, emotion, classification, dataset, equivalent_emotion_from_df) VALUES (?,?,?,?,?)', to_db)
            conn.commit()

        emotion_captured_name = (Counter(dominant_emotion).most_common()[0][0])
        emotion_captured_qty = (Counter(dominant_emotion).most_common()[0][1])

        id_emotion = cursor.execute('SELECT id FROM emotion WHERE emotion = ?', [emotion_captured_name,]).fetchone()
        
        

        #to_db = [id_emotion[0], file_name_to_record, frame_number, emotion_captured_qty, dataset_name, original_emotion]
        to_db = [id_emotion[0], emotion_captured_name, file_name_to_record, frame_number, emotion_captured_qty, dataset_name, original_emotion]
        
        cursor.execute('INSERT INTO emotion_record (emotion_captured, emotion_captured_name, file_name, total_frames, qty_emotion_captured, dataset, original_emotion) VALUES (?, ?,?,?,?,?,?)', to_db)
        conn.commit()                

        #Saving data in CSV
        register_date = datetime.today()
        file_exist = Path('./analyzed/mead_dataset_analyzed_dict.csv').is_file()
        field_names = ['file_name', 'emotion_captured', 'original_emotion', 'total_frame', 'qty_emotion_captured', 'register_date']
        data = {'file_name': file_name_to_record, 'emotion_captured': emotion_captured_name, 'original_emotion': '', 'total_frame': frame_number, 'qty_emotion_captured' : emotion_captured_qty, 'register_date': register_date }
        
        with open('./analyzed/mead_dataset_analyzed_dict.csv', 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)            
            if not file_exist:
                writer.writeheader()
            writer.writerow(data)
            csvfile.close()

    else:
        print('File already analyzed')

    conn.close()
    print("Analysis Completed")
    return video.release()