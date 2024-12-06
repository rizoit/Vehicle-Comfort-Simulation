import tkinter as tk
from tkinter import ttk
from ..widgets.parameter_input import ParameterInput

class VehicleRegion:
    def __init__(self, parent):
        self.frame = ttk.LabelFrame(parent, text="Vehicle Configuration")
        
        # Model selection
        self.model_label = ttk.Label(self.frame, text="Choose Vehicle Model")
        self.model_label.pack(pady=5)
        
        self.model_var = tk.StringVar(value='Quarter Car Model')
        self.model_combo = ttk.Combobox(self.frame, textvariable=self.model_var)
        self.model_combo['values'] = ('Quarter Car Model', 'Seat-Added Quarter Car Model', 'Half Car Model')
        self.model_combo.pack(fill=tk.X, padx=5, pady=5)
        self.model_combo.bind('<<ComboboxSelected>>', self.on_model_change)
        
        # Create a container frame for parameters and initial conditions
        self.container_frame = ttk.Frame(self.frame)
        self.container_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Parameters frame
        self.params_frame = ttk.LabelFrame(self.container_frame, text="Vehicle Parameters")
        self.params_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2, pady=5)
        
        # Create a canvas with scrollbar for parameters
        self.params_canvas = tk.Canvas(self.params_frame)
        self.params_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.params_scrollbar = ttk.Scrollbar(self.params_frame, orient=tk.VERTICAL, command=self.params_canvas.yview)
        self.params_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.params_canvas.configure(yscrollcommand=self.params_scrollbar.set)
        self.params_canvas.bind('<Configure>', lambda e: self.params_canvas.configure(scrollregion=self.params_canvas.bbox("all")))
        self.params_inner_frame = ttk.Frame(self.params_canvas)
        self.params_canvas.create_window((0, 0), window=self.params_inner_frame, anchor="nw")

        # Initial conditions frame
        self.ic_frame = ttk.LabelFrame(self.container_frame, text="Initial Conditions")
        self.ic_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2, pady=5)
        
        # Create a canvas with scrollbar for initial conditions
        self.ic_canvas = tk.Canvas(self.ic_frame)
        self.ic_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.ic_scrollbar = ttk.Scrollbar(self.ic_frame, orient=tk.VERTICAL, command=self.ic_canvas.yview)
        self.ic_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.ic_canvas.configure(yscrollcommand=self.ic_scrollbar.set)
        self.ic_canvas.bind('<Configure>', lambda e: self.ic_canvas.configure(scrollregion=self.ic_canvas.bbox("all")))
        self.ic_inner_frame = ttk.Frame(self.ic_canvas)
        self.ic_canvas.create_window((0, 0), window=self.ic_inner_frame, anchor="nw")
        
        # Initialize with Quarter Car Model parameters and initial conditions
        self.current_params = {}
        self.current_ic = {}
        self.init_quarter_car()
    
    def init_quarter_car(self):
        self.clear_params()
        self.current_params = {
            'ms': ParameterInput(self.params_inner_frame, "Ms", "250", "kg"),
            'mu': ParameterInput(self.params_inner_frame, "Mu", "50", "kg"),
            'ks': ParameterInput(self.params_inner_frame, "Ks", "15000", "N/m"),
            'cs': ParameterInput(self.params_inner_frame, "Cs", "1000", "Ns/m"),
            'kt': ParameterInput(self.params_inner_frame, "Kt", "150000", "N/m")
        }
        self.current_ic = {
            'z_s': ParameterInput(self.ic_inner_frame, "z_s", "0", "m"),
            'z_s_dot': ParameterInput(self.ic_inner_frame, "z_s_dot", "0", "m/s"),
            'z_u': ParameterInput(self.ic_inner_frame, "z_u", "0", "m"),
            'z_u_dot': ParameterInput(self.ic_inner_frame, "z_u_dot", "0", "m/s")
        }
    
    def init_seat_added_quarter_car(self):
        self.clear_params()
        self.current_params = {
            'ms': ParameterInput(self.params_inner_frame, "Ms", "250", "kg"),
            'm_seat': ParameterInput(self.params_inner_frame, "M_seat", "35", "kg"),
            'k_seat': ParameterInput(self.params_inner_frame, "K_seat", "1000", "N/m"),
            'c_seat': ParameterInput(self.params_inner_frame, "C_seat", "500", "Ns/m"),
            'mu': ParameterInput(self.params_inner_frame, "Mu", "50", "kg"),
            'ks': ParameterInput(self.params_inner_frame, "Ks", "15000", "N/m"),
            'cs': ParameterInput(self.params_inner_frame, "Cs", "1000", "Ns/m"),
            'kt': ParameterInput(self.params_inner_frame, "Kt", "150000", "N/m")
        }
        self.current_ic = {
            'z_seat': ParameterInput(self.ic_inner_frame, "z_seat", "0", "m"),
            'z_seat_dot': ParameterInput(self.ic_inner_frame, "z_seat_dot", "0", "m/s"),
            'z_s': ParameterInput(self.ic_inner_frame, "z_s", "0", "m"),
            'z_s_dot': ParameterInput(self.ic_inner_frame, "z_s_dot", "0", "m/s"),
            'z_u': ParameterInput(self.ic_inner_frame, "z_u", "0", "m"),
            'z_u_dot': ParameterInput(self.ic_inner_frame, "z_u_dot", "0", "m/s")
        }
    
    def init_half_car(self):
        self.clear_params()
        self.current_params = {
            'ms': ParameterInput(self.params_inner_frame, "Ms", "500", "kg"),
            'I': ParameterInput(self.params_inner_frame, "I", "1000", "kg⋅m²"),
            'mu_f': ParameterInput(self.params_inner_frame, "Mu_f", "25", "kg"),
            'ks_f': ParameterInput(self.params_inner_frame, "Ks_f", "10000", "N/m"),
            'cs_f': ParameterInput(self.params_inner_frame, "Cs_f", "500", "Ns/m"),
            'kt_f': ParameterInput(self.params_inner_frame, "Kt_f", "75000", "N/m"),
            'mu_r': ParameterInput(self.params_inner_frame, "Mu_r", "25", "kg"),
            'ks_r': ParameterInput(self.params_inner_frame, "Ks_r", "10000", "N/m"),
            'cs_r': ParameterInput(self.params_inner_frame, "Cs_r", "500", "Ns/m"),
            'kt_r': ParameterInput(self.params_inner_frame, "Kt_r", "75000", "N/m"),
            'a': ParameterInput(self.params_inner_frame, "a", "0.5", "m"),
            'b': ParameterInput(self.params_inner_frame, "b", "0.5", "m")
        }
        self.current_ic = {
            'z_s': ParameterInput(self.ic_inner_frame, "z_s", "0", "m"),
            'z_s_dot': ParameterInput(self.ic_inner_frame, "z_s_dot", "0", "m/s"),
            'theta': ParameterInput(self.ic_inner_frame, "theta", "0", "rad"),
            'theta_dot': ParameterInput(self.ic_inner_frame, "theta_dot", "0", "rad/s"),
            'z_u_f': ParameterInput(self.ic_inner_frame, "z_u_f", "0", "m"),
            'z_u_f_dot': ParameterInput(self.ic_inner_frame, "z_u_f_dot", "0", "m/s"),
            'z_u_r': ParameterInput(self.ic_inner_frame, "z_u_r", "0", "m"),
            'z_u_r_dot': ParameterInput(self.ic_inner_frame, "z_u_r_dot", "0", "m/s")
        }
    
    def clear_params(self):
        for widget in self.params_inner_frame.winfo_children():
            widget.destroy()
        for widget in self.ic_inner_frame.winfo_children():
            widget.destroy()
        self.current_params = {}
        self.current_ic = {}
    
    def on_model_change(self, event):
        model = self.model_var.get()
        if model == 'Quarter Car Model':
            self.init_quarter_car()
        elif model == 'Seat-Added Quarter Car Model':
            self.init_seat_added_quarter_car()
        elif model == 'Half Car Model':
            self.init_half_car()
    
    def get_parameters(self):
        return {key: float(param.get_value()) for key, param in self.current_params.items()}
    
    def get_initial_conditions(self):
        return {key: float(ic.get_value()) for key, ic in self.current_ic.items()}

