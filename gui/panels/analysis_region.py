import tkinter as tk
from tkinter import ttk
from ..widgets.parameter_input import ParameterInput


class AnalysisRegion:
    def __init__(self, parent):
        self.frame = ttk.LabelFrame(parent, text="Analysis Control")

        # Analysis parameters
        self.name_input = ParameterInput(self.frame, "Name", "Test 1")
        self.duration_input = ParameterInput(self.frame, "Duration", "3", "sec")
        self.steps_input = ParameterInput(self.frame, "Number of Steps", "3000")

        # Run button
        self.run_button = ttk.Button(self.frame, text="RUN")
        self.run_button.pack(fill=tk.X, padx=5, pady=10)

        # See Results button
        self.results_button = ttk.Button(self.frame, text="See Results")
        self.results_button.pack(fill=tk.X, padx=5, pady=5)
