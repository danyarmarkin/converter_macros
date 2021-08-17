import cv2
import os

vidcap = cv2.VideoCapture('IMG_1674.MOV')
success, image = vidcap.read()
count = 0
step = int(input("step = "))
nameInd = 0


while success:
    count += 1
    if count % step != 0:
        vidcap.read()
        continue
    cv2.imwrite("AAAA/frame%d.jpg" % nameInd, image)     # save frame as JPEG file
    success, image = vidcap.read()
    print('Read a new frame: ', success)
    nameInd += 1
