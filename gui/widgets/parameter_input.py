import tkinter as tk
from tkinter import ttk

class ParameterInput:
    def __init__(self, parent, label, default_value="", unit=""):
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill=tk.X, padx=5, pady=2)
        
        self.label = ttk.Label(self.frame, text=label, width=5, anchor="w")
        self.label.pack(side=tk.LEFT, padx=(0, 5))
        
        self.value = tk.StringVar(value=default_value)
        self.entry = ttk.Entry(self.frame, textvariable=self.value, width=10)
        self.entry.pack(side=tk.LEFT)
        
        if unit:
            self.unit_label = ttk.Label(self.frame, text=unit, width=5, anchor="w")
            self.unit_label.pack(side=tk.LEFT, padx=(5, 0))
    
    def get_value(self):
        return self.value.get()
    
    def set_value(self, value):
        self.value.set(value)
