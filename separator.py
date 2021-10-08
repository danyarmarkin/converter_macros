import cv2
import os
from math import *
import speed

def getFramesAmount(videoFile):
    vidcap = cv2.VideoCapture(videoFile)
    total = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(total)
    return total


is_stop = False

def stop():
    global is_stop
    is_stop = True


def separate(videoFile, step, directory, status, progressBar, name, start_frame, save_as_jpg, tolerance, speedLabel, endLabel):
    global is_stop
    try:
        os.mkdir(directory)
    except FileExistsError:
        pass

    vidcap = cv2.VideoCapture(videoFile)
    success, image = vidcap.read()
    count = 0
    nameInd = 0
    total = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(total)
    total //= step

    images = []
    imagesScore = []
    arrayIndex = 0

    success, image = vidcap.read()
    images.append(image)
    imagesScore.append(cv2.Laplacian(image, cv2.CV_64F).var())

    speed.create(speedLabel, endLabel)
    speed.start()

    def save(nameInd):
        maxScore = max(imagesScore)
        maxImage = images[imagesScore.index(maxScore)]
        for i in range(len(imagesScore)):
            print("frame " + str(i) + " with score: " + str(imagesScore[i]))
        print("max image", imagesScore.index(maxScore), "with score:", maxScore)
        print("-" * 10)

        p = 4 - len(str(start_frame + nameInd))
        if save_as_jpg:
            cv2.imwrite(directory + "/" + name + "_" + "0" * p + "%d.jpg" % (start_frame + nameInd), maxImage)
        else:
            cv2.imwrite(directory + "/" + name + "_" + "0" * p + "%d.png" % (start_frame + nameInd),
                        maxImage)  # save frame as PNG file
        speed.newFrame(total)


    while success:
        if is_stop:
            is_stop = False
            break
        count += 1
        print(count)

        if count % step == tolerance + 1:
            save(nameInd)
            # success, image = vidcap.read()
            nameInd += 1
            status["text"] = "Status: " + str(nameInd) + "/" + str(total) + " frames"
            progressBar["value"] = floor(nameInd / total * 100)
            status.update()
            progressBar.update()

        if count % step == step - tolerance:
            images = [image]
            l = cv2.Laplacian(image, cv2.CV_64F).var()
            imagesScore = [l]
            success, image = vidcap.read()
            continue
        elif count % step > step - tolerance:
            images.append(image)
            l = cv2.Laplacian(image, cv2.CV_64F).var()
            imagesScore.append(l)
            success, image = vidcap.read()
            continue
        elif count % step <= tolerance:
            if tolerance == 0:
                imagesScore = []
                images = []
            images.append(image)
            l = cv2.Laplacian(image, cv2.CV_64F).var()
            imagesScore.append(l)
            success, image = vidcap.read()
            continue
        else:
            vidcap.read()
            continue


