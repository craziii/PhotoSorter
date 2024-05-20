import tkinter as tk
import LockedSearchFolderEntry
import InputSection
import os

window = tk.Tk()
window.title("PhotoSorter")
window.geometry("1920x1080")
window.resizable(False, False)
topFrame = tk.Frame(window)
exitButton = tk.Button(master=topFrame, text="Exit", command=window.destroy)
exitButton.pack(side=tk.TOP, padx=5, pady=5, anchor=tk.NE, expand=False)
topFrame.pack(side=tk.RIGHT, fill=tk.NONE, anchor=tk.NE, expand=False)
inputFrame = tk.Frame(window, padx=5, pady=5)
inputFrame.pack(anchor="nw")
inputFolder = LockedSearchFolderEntry.LockedSearchFolderEntry(inputFrame, "Input Folder:", os.path.dirname(os.path.realpath(__file__)))
inputFolder.pack()
inputSuffix = InputSection.InputSection(inputFrame, "Input Suffix:", "")
inputSuffix.pack()


def lockall():
    lockinputs(True)

def unlockall():
    lockinputs(False)

def lockinputs(lock):
    inputFolder.inputSection.lock(lock)
    inputSuffix.lock(lock)

lockFrame = tk.Frame(window)
lockAllButton = tk.Button(master=lockFrame, text="Lock All", command=lockall)
unlockAllButton = tk.Button(master=lockFrame, text="Unlock All", command=unlockall)

lockAllButton.pack(anchor=tk.NW, side=tk.LEFT, padx=5)
unlockAllButton.pack(anchor=tk.NW, side=tk.LEFT, padx=5)
lockFrame.pack(anchor=tk.NW, side=tk.LEFT, padx=5)

window.mainloop()


