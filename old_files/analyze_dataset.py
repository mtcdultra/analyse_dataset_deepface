from deepface import DeepFace
import os
import tools
emotions = ['angry', 'disgust', 'fear', 'neutral', 'sad', 'surprised', 'happy']

##################### TEST VALUES #####################
path_frames_analyze = '/Users/mtcd/Downloads/mead_2023'
#path_frames_analyze = '/Users/mtcd/Downloads/mead_frames_60_perc'
path_save_csv = '/Users/mtcd/Downloads/mead_dataset_60_perc/teste.csv'
dataset_name = 'mead'
#######################################################

#######################################################
#path_frames_analyze = input('')
#path_save_csv = input('')
#dataset_name = ''
#######################################################

to_save = []
with open(path_save_csv, 'w') as f:
    f.write('file_name,emotion_original,emotion_analyzed,dataset\n')

    for folder, subfolder, files in os.walk(path_frames_analyze):                
        for file in files:
            try:
                #print(os.path.join(path_frames_analyze,file))
                if file == '.DS_Store': continue
                img_file = os.path.join(path_frames_analyze,file)
                obj = DeepFace.analyze(img_file, actions = ['emotion'],enforce_detection=False)
                emotion_analyzed = obj['dominant_emotion']
                print(emotion_analyzed)
                emotion_file = tools.define_emotion_from_file_name(file)
                print(emotion_file)
                to_save.append([emotions[emotion_file], emotion_analyzed, file])
                f.write('%s,%s,%s,%s' % (file, emotions[emotion_file], emotion_analyzed, dataset_name))
                f.write('\n')
            except:
                next
    acertos, erros = 0,0

    for i in to_save:
        if i[0] == i[1]:
            acertos = acertos + 1
        else:
            erros = erros + 1

print(f'Acertos {acertos} e erros {erros}')
print(f'{erros/(erros+acertos)*100}% de erros')
print(f'{acertos/(erros+acertos)*100}% de acertos')