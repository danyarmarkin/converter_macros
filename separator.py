import cv2
import os
import tkinter

def separate(videoFile, step, directory, status):
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
        if count % step != 0:
            success, image = vidcap.read()
            continue
        cv2.imwrite(directory + "/frame%d.jpg" % nameInd, image)     # save frame as JPEG file
        success, image = vidcap.read()
        print('Read a new frame:', success, "with frame number", nameInd)
        nameInd += 1
        status["text"] = "Status: " + str(nameInd) + "/" + str(total) + " frames"
        status.update()