## FACIAL EXPRESSION MEAD DATASET ##

Algorithm to analyses emotions from videos files using DeepFace Python library (https://github.com/serengil/deepface) and generate a summarise table to show how many times each emotion has captured by frame. For this examples, was used MEAD dataset (https://wywu.github.io/projects/MEAD/MEAD.html).

*To use the algorithm:*
1. Create DATASET and ANALYZED folders inside the main folder:
	- '/Users/abc/facial_expression_mead_dataset'
	- '/Users/abc/facial_expression_mead_dataset/datasets'
	- '/Users/abc/facial_expression_mead_dataset/analyzed'
2. Change the path name in "run_analyse.py" file where videos files are in your computer
3. Run this python file
4. Will be create in analyzed folder

	- mead_dataset_analyzed_dict.csv (summaryzed informations from captured emotions from all videos files)
	- file_name.json (each video file will generate a json file from each frame emotion's captured)
	- file_name.txt (each video file will generate a txt file with frames, fps and duration information)

5. Will be create main folder:

	- mead_dataset.db (all captured emotions are save in sqlite database)

#############################################

*Informations about database columns:*

file_name: file name video that captured frames;
emotion_from_mead_ds: emotion categorised by MEAD database;
emotion_returned_from_df: emotion captured by DeepFace Python library;
total_frames: Total frames analysed;
angry, disgust…: Show how many frames were identified by DeepFace Python library.

![Screenshot 2022-10-31 at 09 44 59](https://user-images.githubusercontent.com/77461340/198979180-c8d435b9-6530-450d-8b2f-a922a67464c6.jpg)
