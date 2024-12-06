import tkinter as tk
from tkinter import ttk, filedialog
from ..widgets.results_list import ResultsList

class ControlRegion:
    def __init__(self, parent, simulation_collector):
        self.frame = ttk.LabelFrame(parent, text="Control and History")
        self.simulation_collector = simulation_collector
        
        # Title
        self.title = ttk.Label(self.frame, text="Vehicle Comfort Calculator", font=("Arial", 16, "bold"))
        self.title.pack(pady=10)
        
        # Export button
        self.export_button = ttk.Button(self.frame, text="Export Result")
        self.export_button.pack(fill=tk.X, padx=5, pady=5)
        
        # Load button
        self.load_button = ttk.Button(self.frame, text="Load Result", command=self.load_result)
        self.load_button.pack(fill=tk.X, padx=5, pady=5)
        
        # Results list
        self.results_list = ResultsList(self.frame)
        self.results_list.frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def load_result(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            self.simulation_collector.import_results(file_path)
            self.update_results_list()

    def update_results_list(self):
        self.results_list.clear()
        for name in self.simulation_collector.list_analyses():
            analysis = self.simulation_collector.get_analysis(name)
            self.results_list.add_result(name, analysis['execution_date'])

