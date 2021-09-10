from tkinter import *
from tkinter.ttk import Progressbar

from math import *
import json
from tkinter.filedialog import askopenfile, askdirectory, askopenfilenames
import separator

from asyncio import *


files = []

def startTkinterInterface():
    root = Tk()
    root.geometry("600x400")
    root.title("Converter")

    path = StringVar()
    path.set("...")

    outputPath = StringVar()
    outputPath.set("...")

    step = IntVar()
    step.set(10)


    def getFile():
        global files
        file = askopenfilenames(parent=root, title='Choose a files')
        files = file
        if len(file) >= 1:
            path.set(str(len(file)) + " videos")
            outputPath.set("to " + str(len(file)) + " folders")


    def setOutputPath():
        # global outputPath
        file = askdirectory()
        print(file)
        outputPath.set(file)

    frame = Frame(root, borderwidth=1)
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

    # Step

    stepLabel = Label(frame, text="Step")
    stepLabel.grid(row=2, column=1)

    stepOutputFrames = Label(frame, text="")
    stepOutputFrames.grid(row=2, column=2)

    def stepCallback(sv):
        try:
            value = int(sv.get())
            print("try")
            frames = separator.getFramesAmount(path.get())
            print("try")
            stepLabel["text"] = "step with " + str(frames) + " frames video => " + str(int(floor(frames / value))) + " frames"
            print("try")
        except Exception:
            print("exception")
            stepLabel["text"] = "error with step"

    stepEntry = Entry(frame, width=10, textvariable=step, validatecommand=stepCallback)
    stepEntry.grid(row=2, column=0)
    step.trace("w", lambda name, index, mode, sv=step: stepCallback(sv))

    # Progress

    statusLabel = Label(frame, text="")
    statusLabel.grid(row=4, column=1)

    progressBar = Progressbar(frame, length=400, mode="determinate")
    progressBar.grid(row=3, column=1)

    def start():
        global files
        # global statusLabel, progressBar
        for p in files:
            path.set(p)
            name = list(p.split("/"))[-1][:-4]
            if len(list(p.split("/"))) == 1:
                name = list(p.split("\\"))[-1][:-4]
            childes = list(p.split("/"))[:-1]
            isWind = False
            print(childes)
            if len(childes) == 0:
                childes = list(p.split("\\"))[:-1]
                isWind = True
            try:
                if childes[0][-1] == ":":
                    isWind = True
            except Exception:
                pass
            if childes[0] == '':
                childes = childes[1:]
            op = ""
            for child in childes:
                op += "/" + child
            if isWind:
                del op[op.index("/")]

            session = name.split("_")
            obj_name = session[0]
            session_name = session[1]
            devices = session[2]
            folder_name = obj_name + "_" + session_name + "_" + str(devices)[-1] + "_" + session[3] + "_" + session[4]
            op += "/" + folder_name

            outputPath.set(op)
            start_frame = 0
            with open("converter_data.json") as converter_data:
                file_content = json.load(converter_data)
                if folder_name in file_content["sessions"]:
                    start_frame = file_content["sessions"][folder_name]
                file_content["sessions"][folder_name] = start_frame + int(separator.getFramesAmount(path.get()) / step.get())
            with open("converter_data.json", "w") as converter_data:
                converter_data.write(json.dumps(file_content))
            separator.separate(path.get(), int(step.get()), outputPath.get(), statusLabel, progressBar, session_name +
                               "_" + devices, 0)

    startButton = Button(frame, text="Start", command=start)
    startButton.grid(row=3, column=2)

    stepCallback(step)

    root.mainloop()
