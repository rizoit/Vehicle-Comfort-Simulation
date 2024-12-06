import tkinter as tk
from tkinter import ttk
from ..widgets.parameter_input import ParameterInput

class RoadRegion:
    def __init__(self, parent):
        self.frame = ttk.LabelFrame(parent, text="Road Profile")
        
        # Profile selection
        self.profile_label = ttk.Label(self.frame, text="Choose Road Profile")
        self.profile_label.pack(pady=5)
        
        self.profile_var = tk.StringVar(value='Sinusoidal')
        self.profile_combo = ttk.Combobox(self.frame, textvariable=self.profile_var)
        self.profile_combo['values'] = ('Sinusoidal', 'Step', 'Chirp')
        self.profile_combo.pack(fill=tk.X, padx=5, pady=5)
        self.profile_combo.bind('<<ComboboxSelected>>', self.on_profile_change)
        
        # Parameters frame
        self.params_frame = ttk.Frame(self.frame)
        self.params_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Initialize with Sinusoidal parameters
        self.current_params = {}
        self.init_sinusoidal_params()
    
    def init_sinusoidal_params(self):
        self.clear_params()
        self.current_params = {
            'frequency': ParameterInput(self.params_frame, "Frequency", "1", "Hz"),
            'amplitude': ParameterInput(self.params_frame, "Amplitude", "0.01", "m")
        }
    
    def clear_params(self):
        for widget in self.params_frame.winfo_children():
            widget.destroy()
        self.current_params = {}
    
    def on_profile_change(self, event):
        profile = self.profile_var.get()
        self.clear_params()
        if profile == 'Sinusoidal':
            self.init_sinusoidal_params()
        # Add other profile initializations as needed

