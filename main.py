import tkinter as tk
import numpy as np
from tkinter import ttk
from gui.panels.modeling_panel import ModelingPanel
from models import *
from simulation import *
from road import *
from plotting import *
from matplotlib import pyplot as plt

class VehicleComfortCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Vehicle Comfort Calculator")
        self.root.geometry("800x800")
        
        # Create main container
        self.main_container = ttk.Frame(self.root)
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create modeling panel
        self.modeling_panel = ModelingPanel(self.main_container)
    
    def run(self):
        self.root.mainloop()



if __name__ == "__main__":
    from example.tested_examples import seat_added_quarter_car,quarter_car, half_car
    #quarter_car()
    #seat_added_quarter_car()
    half_car()


    

    