import tkinter as tk
from tkinter import ttk
from ..panels.control_region import ControlRegion
from ..panels.vehicle_region import VehicleRegion
from ..panels.road_region import RoadRegion
from ..panels.analysis_region import AnalysisRegion
from simulation.collector import SimulationCollector

class ModelingPanel:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Initialize SimulationCollector
        self.simulation_collector = SimulationCollector()
        
        # Create grid layout
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        
        # Initialize regions
        self.control_region = ControlRegion(self.frame, self.simulation_collector)
        self.control_region.frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        self.vehicle_region = VehicleRegion(self.frame)
        self.vehicle_region.frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        
        self.road_region = RoadRegion(self.frame)
        self.road_region.frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        
        self.analysis_region = AnalysisRegion(self.frame)
        self.analysis_region.frame.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

