from tkinter import *
from time import *

rootSpeed = None

speed = "1 fps"

speedLabel = None
endLabel = None

startTime = time()
frames = 0


def destroy():
    global rootSpeed
    rootSpeed.destroy()


def create(speedL, endL):
    global rootSpeed, speed, speedLabel, endLabel
    # rootSpeed = Tk()
    # rootSpeed.geometry("120x40")
    # rootSpeed.title("speed")
    speedLabel = speedL
    endLabel = endL
    # speedLabel.grid(row=0, column=0)

def start():
    global startTime, speed, speedLabel, frames
    startTime = time()
    speed = "0 fps"
    frames = 0
    speedLabel.update()


def newFrame(total):
    global frames, speed, speedLabel, endLabel
    frames += 1
    s = round(frames / (time() - startTime), 3)
    speed = str(s) + " fps"
    speedLabel["text"] = speed
    speedLabel.update()
    minutes = round(s * (total - frames)) // 60
    seconds = round(s * (total - frames)) % 60
    minutes0 = 2 - len(str(minutes))
    seconds0 = 2 - len(str(seconds))
    if minutes0 < 0:
        minutes0 = 0
    if seconds0 < 0:
        seconds0 = 0
    endLabel["text"] = "0"*minutes0 + str(minutes) + ":" + "0"*seconds0 + str(seconds)


