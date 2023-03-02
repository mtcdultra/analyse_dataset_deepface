import main as mn

folder = '/Users/mtcd/Library/Mobile Documents/com~apple~CloudDocs/@Pessoal/@Evernote/Estudos/@programming/p.face_emotion_new/analyzed'

for file_name in mn.list_of_files(folder, 'json'):
    file_name_txt = file_name[124:]
    file_name_txt = file_name_txt.replace('face_detection.json','metadata.txt')
    print(mn.summarize_emotions(file_name))
    print(open(folder+file_name_txt,'r').readlines())
    print("")