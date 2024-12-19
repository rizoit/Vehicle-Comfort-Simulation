import tkinter as tk
from tkinter import ttk


class ResultsList:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)

        # Title
        self.title = ttk.Label(self.frame, text="Available Results:")
        self.title.pack(pady=5)

        # Listbox with scrollbar
        self.scrollbar = ttk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(self.frame, yscrollcommand=self.scrollbar.set)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar.config(command=self.listbox.yview)

    def add_result(self, name, date):
        self.listbox.insert(tk.END, f"{name} / {date}")

    def get_selected(self):
        selection = self.listbox.curselection()
        if selection:
            return self.listbox.get(selection[0])
        return None

    def clear(self):
        self.listbox.delete(0, tk.END)
