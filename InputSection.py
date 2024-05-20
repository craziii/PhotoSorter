import tkinter as tk
import TitleText


class InputSection:

    def __init__(self, master, title, currentInput):
        self.master = master
        self.frame = tk.Frame(master)
        self.lockInput = tk.BooleanVar()
        self.lockInputButton = tk.Checkbutton(self.frame, text="Lock?", variable=self.lockInput, onvalue=True, offvalue=False, command=self.setInputAccessState)
        self.title = TitleText.TitleText(self.frame, title)
        self.searchInput = tk.Entry(master=self.frame, justify='left', state=tk.NORMAL, width=75)
        self.setInput(currentInput)
        self.setInputAccessState()

    def setInput(self, Input):
        self.searchInput.config(state=tk.NORMAL)
        self.searchInput.delete(0, tk.END)
        self.searchInput.insert("1", Input)
        self.setInputAccessState()

    def setInputAccessState(self):
        if self.lockInput.get():
            self.searchInput.config(state=tk.DISABLED)
        else:
            self.searchInput.config(state=tk.NORMAL)

    def lock(self, lock):
        if self.lockInput.get():
            if not lock:
                self.lockInputButton.invoke()
        else:
            if lock:
                self.lockInputButton.invoke()

    def pack(self):
        self.title.pack()
        self.lockInputButton.pack(side=tk.LEFT, padx=5, pady=5, anchor=tk.NW)
        self.searchInput.pack(side=tk.LEFT, padx=5, pady=5, anchor=tk.NW, expand=True)
        self.frame.pack(fill=tk.BOTH, expand=True)