import tkinter as tk


class TitleText:
    def __init__(self, master, title):
        self.title = tk.Text(master, width=len(title), height=1)
        self.title.insert(tk.INSERT, title)
        self.title.config(state=tk.DISABLED)

    def pack(self):
        self.title.pack(side=tk.LEFT, padx=10, pady=10, anchor=tk.NW, expand=False)