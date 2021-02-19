#!/usr/bin/env python3

'''
Retrieves individual frames from videos taken on the robot.
'''

import cv2

labels = ['A-BLUE', 'A-RED', 'B-BLUE', 'B-RED']

for label in labels:
    frame_count = 0
    for i in range(3):
        video_path = './video/' + label + '/' + label + '-' + str(i) + '.mp4'
        save_path = './input/' + label + '/' + label + '-'
        ftype = '.jpg'
        vidcap = cv2.VideoCapture(video_path)
        success, image = vidcap.read()
        while success:
            img_name = save_path + str(frame_count) + ftype
            print(img_name)
            cv2.imwrite(img_name, image)
            success, image = vidcap.read()
            frame_count += 1