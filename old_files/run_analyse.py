import main as mn

#pasta = '/Users/mtcd/Library/Mobile Documents/com~apple~CloudDocs/@Pessoal/@Evernote/Estudos/@programming/facial_expression_mead_dataset/datasets'

#pasta = '/Users/mtcd/Downloads/@datasets/adfes/train'

pasta = '/Users/mtcd/Library/Mobile Documents/com~apple~CloudDocs/@Pessoal/@Evernote/Estudos/@programming/facial_expression_mead_dataset/datasets'
file_type = 'mp4'


#pasta = '/Users/mtcd/Downloads/fer2013_dataset/test'
#file_type = 'jpg'

for file in mn.list_of_files(pasta, file_type):
    mn.analyse_imag(file, 'FER-2013')