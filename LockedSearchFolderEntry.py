import tkinter as tk
import InputSection


class LockedSearchFolderEntry:

    def __init__(self, master, title, currentFolder):
        self.inputSection = InputSection.InputSection(master, title, currentFolder)
        self.searchFolderButton = tk.Button(master=self.inputSection.frame, text="Search", command=self.findFolder)

    def findFolder(self):
        from tkinter import filedialog
        self.inputSection.setInput(filedialog.askdirectory(mustexist=True))

    def lock(self, lock):
        self.inputSection.lock(lock)

    def pack(self):
        self.inputSection.title.pack()
        self.inputSection.lockInputButton.pack(side=tk.LEFT, padx=5, pady=5, anchor=tk.NW)
        self.inputSection.searchInput.pack(side=tk.LEFT, padx=5, pady=5, anchor=tk.NW, expand=True)
        self.searchFolderButton.pack(side=tk.LEFT, padx=5, pady=5, anchor=tk.NW)
        self.inputSection.frame.pack(fill=tk.BOTH, expand=False)

