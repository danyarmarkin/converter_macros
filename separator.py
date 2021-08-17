import cv2
import os

vidcap = cv2.VideoCapture('IMG_1674.MOV')
success, image = vidcap.read()
count = 0
step = int(input("step = "))
directory = input("to directory: ")
os.mkdir(directory)
nameInd = 0

while success:
    count += 1
    if count % step != 0:
        success, image = vidcap.read()
        continue
    cv2.imwrite(directory + "/frame%d.jpg" % nameInd, image)     # save frame as JPEG file
    success, image = vidcap.read()
    print('Read a new frame:', success, "with frame number", nameInd)
    nameInd += 1

input()