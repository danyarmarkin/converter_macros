import cv2
import os

videoFile = input("video file name with extension: ")
step = int(input("step = "))
directory = input("to directory: ")

try:
    os.mkdir(directory)
except FileExistsError:
    print("this folder is already exist")
    print("do yo want to continue(y / n)?")
    res = input()
    if res != "y":
        exit(1)

vidcap = cv2.VideoCapture(videoFile)
success, image = vidcap.read()
count = 0
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
