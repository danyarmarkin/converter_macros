from tkinter import *
from tkinter.ttk import Progressbar

import cv2
import os
# from tkFileDialog import *
from tkinter.filedialog import askopenfile, askdirectory
import separator

import Telegram

root = Tk()
root.geometry("600x400")
root.title("Convertor")

path = StringVar()
path.set("...")

outputPath = StringVar()
outputPath.set("...")

step = IntVar()
step.set(10)

def getFile():
    global path, outputPath
    file = askopenfile(parent=root, mode='rb', title='Choose a file')
    p = os.path.abspath(file.name)
    print(p)
    path.set(p)
    childes = list(p.split("/"))[:-1]
    if len(childes) == 0:
        childes = list(p.split("\\"))[:-1]
    if childes[0] == '':
        childes = childes[1:]
    print(childes)
    op = ""
    for child in childes:
        op += "/" + child
    outputPath.set(op)

def setOutputPath():
    global outputPath
    file = askdirectory()
    print(file)
    outputPath.set(file)

frame = Frame(root, borderwidth = 1)
frame.place(relx=0, rely=0)
frame.grid(row=0, column=0)

pathLabel = Label(frame, text="Path to video file")
pathLabel.grid(row=0, column=0)

pathEntry = Entry(frame, width=45, textvariable=path)
pathEntry.grid(row=0, column=1)

browseButton = Button(frame, text="Browse", command=getFile)
browseButton.grid(row=0, column=2)


outputPathLabel = Label(frame, text="Output Folder")
outputPathLabel.grid(row=1, column=0)

outputPathEntry = Entry(frame, width=45, textvariable=outputPath)
outputPathEntry.grid(row=1, column=1)

outputPathBrowseButton = Button(frame, text="Browse", command=setOutputPath)
outputPathBrowseButton.grid(row=1, column=2)


stepLabel = Label(frame, text="Step")
stepLabel.grid(row=2, column=0)

stepEntry = Entry(frame, width=10, textvariable=step)
stepEntry.grid(row=2, column=1)


statusLabel = Label(frame, text="")
statusLabel.grid(row=4, column=1)


progressBar = Progressbar(frame, length=400, mode="determinate")
progressBar.grid(row=3, column=1)

def start():
    global statusLabel, progressBar
    separator.separate(path.get(), int(step.get()), outputPath.get(), statusLabel, progressBar)
startButton = Button(frame, text="Start", command=start)
startButton.grid(row=3, column=2)

root.mainloop()

# Telegram.pool()