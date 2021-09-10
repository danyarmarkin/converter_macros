import cv2
import os
from math import *
import tkinter


def getFramesAmount(videoFile):
    vidcap = cv2.VideoCapture(videoFile)
    total = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(total)
    return total


def separate(videoFile, step, directory, status, progressBar):
    try:
        os.mkdir(directory)
    except FileExistsError:
        pass

    vidcap = cv2.VideoCapture(videoFile)
    success, image = vidcap.read()
    count = 0
    nameInd = 0
    total = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    total //= step

    while success:
        count += 1
        if count % step == step - 1:
            success, image = vidcap.read()
            continue
        if count % step != 0:
            vidcap.read()
            continue
        cv2.imwrite(directory + "/frame%d.png" % nameInd, image)     # save frame as PNG file
        success, image = vidcap.read()
        print('Read a new frame:', success, "with frame number", nameInd)
        nameInd += 1
        status["text"] = "Status: " + str(nameInd) + "/" + str(total) + " frames"
        progressBar["value"] = floor(nameInd / total * 100)
        status.update()
        progressBar.update()