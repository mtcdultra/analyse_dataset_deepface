import os
import cv2
import tools

##################################################################

def extract_frame(path_videos, path_to_save_frames):
    count = 0
    print(path_videos)
    video = cv2.VideoCapture(path_videos)
    while video.isOpened():
        try:
            _, image = video.read()
            file_name_ = path_videos.replace('/', '_')
            file_name_ = file_name_.replace('.', '_')
            file_name_ = file_name_ + '_' + str(count)
            file_name_ = path_to_save_frames + '/' + file_name_ + '.jpg'
            cv2.imwrite(file_name_, image)
            count += 1
        except:
            break
    video.release()
    return 'Finished'


def extract_frame_v2(path_videos, path_to_save_frames, percentage):
    count = 0
    print(path_videos)
    
    video = cv2.VideoCapture(path_videos)
    try:
        file_list = []
        while video.isOpened():            
            _, image = video.read()
            file_name_ = path_videos.replace('/', '_')
            file_name_ = file_name_.replace('.', '_')
            file_name_ = file_name_ + '_' + str(count)
            file_name_ = path_to_save_frames + '/' + file_name_ + '.jpg'
            cv2.imwrite(file_name_, image)
            count += 1
            file_list.append(file_name_)
    except:
        next
    
    if percentage >= 1:
        
        result = len(file_list) * (percentage/100)
        head_part = int(result / 2)
        tail_part = int(result / 2)

        for i in file_list[0:head_part]: os.remove(i)
        for i in file_list[-tail_part:]: os.remove(i)

    video.release()


    return 'Finished'

# --------------------------------------------------------------------------------------


def main():

    answer = input(
        'Do you want create a folder to save frames files? Y or N >> '
    )
    if answer == 'Y':
        path_to_save_frames = tools.create_folder()
    else:
        path_to_save_frames = input(
            'Type the path where to save frames files: '
        )

    print('In this folder will be saved frames files: ', path_to_save_frames)
    path_videos = input('Type the path where the videos files are: ')
    percentage = int(input('If want cut off initial and final part of video, type a percentage to cut or 0 to keep all: '))
    
    qty_files = len(tools.get_the_file_path(path_videos))
    qty_files_ = qty_files
    for file_name in tools.get_the_file_path(path_videos):
        print(str(qty_files) + ' / ' + str(qty_files_))
        qty_files_ = qty_files_ - 1
        #extract_frame(file_name, path_to_save_frames)
        #print(file_name)
        extract_frame_v2(file_name, path_to_save_frames, percentage)


# --------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()