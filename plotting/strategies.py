from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import numpy as np
from dataclasses import dataclass
import configuration

@dataclass
class QuarterCarOutouts():
    acc_ms_max: float = 0.0
    vel_ms_max: float = 0.0
    disp_ms_max: float = 0.0

    acc_mu_max: float = 0.0     
    vel_mu_max: float = 0.0
    disp_mu_max: float = 0.0

    rms_acc_ms: float = 0.0
    disp_range: float = 0.0

 
class PlottingStrategy(ABC):
    @abstractmethod
    def plot(self, analysis_data):
        pass

class QuarterCarPlottingStrategy(PlottingStrategy):
    def plot(self, analysis_data):
        """
        Plots quarter car simulation results showing displacements and accelerations.

        Args:
            analysis_data (dict): Dictionary containing simulation results with time series
                                data for sprung and unsprung mass movements.

        Returns:
            None: Displays two subplot figures showing displacements and accelerations.
        """
        # Apply plot style configurations
        plt.rcParams['font.size'] = configuration.PLOT_STYLE['font_size']
        plt.rcParams['font.family'] = configuration.PLOT_STYLE['font_family']
        
        time_data = np.array(analysis_data['results']['t'])
        y_data = np.array(analysis_data['results']['y'])
        road_profile = np.array(analysis_data['results']['road_profile'])

        z_s_data = y_data[0]#sprung mass displacement
        z_s_dot_data = y_data[1]#sprung mass velocity
        z_u_data = y_data[2]#unsprung mass displacement
        z_u_dot_data = y_data[3]#unsprung mass velocity

        # Calculate accelerations
        z_s_ddot_data = np.gradient(z_s_dot_data, time_data)#sprung mass acceleration
        z_u_ddot_data = np.gradient(z_u_dot_data, time_data)#unsprung mass acceleration

        # Create two subplots with configured figure size
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=configuration.PLOT_STYLE['figure_size'])

        # First subplot: Displacements
        ax1.plot(time_data, road_profile, label="Road profile", 
                linewidth=configuration.PLOT_STYLE['line_width'],
                color=configuration.PLOT_STYLE['colors'][0])
        ax1.plot(time_data, z_s_data, label="Sprung mass displacement",
                linewidth=configuration.PLOT_STYLE['line_width'],
                color=configuration.PLOT_STYLE['colors'][1])
        ax1.plot(time_data, z_u_data, label="Unsprung mass displacement",
                linewidth=configuration.PLOT_STYLE['line_width'],
                color=configuration.PLOT_STYLE['colors'][2])
        
        ax1.set_title("Quarter Car Simulation Results - Displacements", 
                     fontsize=configuration.PLOT_STYLE['title_size'],
                     fontweight=configuration.PLOT_STYLE['title_weight'])
        ax1.set_xlabel("Time [s]", fontsize=configuration.PLOT_STYLE['axis_label_size'])
        ax1.set_ylabel("Displacement [m]", fontsize=configuration.PLOT_STYLE['axis_label_size'])
        ax1.legend(fontsize=configuration.PLOT_STYLE['legend_font_size'], 
                  loc=configuration.PLOT_STYLE['legend_location'])
        ax1.grid(True, linewidth=configuration.PLOT_STYLE['grid_style'].get('linewidth', 1))

        # Second subplot: Accelerations
        ax2.plot(time_data, z_s_ddot_data, label="Sprung mass acceleration",
                linewidth=configuration.PLOT_STYLE['line_width'],
                color=configuration.PLOT_STYLE['colors'][3])
        ax2.plot(time_data, z_u_ddot_data, label="Unsprung mass acceleration",
                linewidth=configuration.PLOT_STYLE['line_width'],
                color=configuration.PLOT_STYLE['colors'][4])
        
        ax2.set_title("Quarter Car Simulation Results - Accelerations",
                     fontsize=configuration.PLOT_STYLE['title_size'],
                     fontweight=configuration.PLOT_STYLE['title_weight'])
        ax2.set_xlabel("Time [s]", fontsize=configuration.PLOT_STYLE['axis_label_size'])
        ax2.set_ylabel("Acceleration [m/s²]", fontsize=configuration.PLOT_STYLE['axis_label_size'])
        ax2.legend(fontsize=configuration.PLOT_STYLE['legend_font_size'],
                  loc=configuration.PLOT_STYLE['legend_location'])
        ax2.grid(True, linewidth=configuration.PLOT_STYLE['grid_style'].get('linewidth', 1))

        plt.tight_layout()
        plt.show()

class SeatAddedQuarterCarPlottingStrategy(PlottingStrategy):
    def plot(self, analysis_data):
        # Apply plot style configurations
        plt.rcParams['font.size'] = configuration.PLOT_STYLE['font_size']
        plt.rcParams['font.family'] = configuration.PLOT_STYLE['font_family']
        
        time_data = np.array(analysis_data['results']['t'])
        y_data = np.array(analysis_data['results']['y'])
        road_profile = np.array(analysis_data['results']['road_profile'])

        # Extract displacement data
        z_seat_data = y_data[0]  # seat displacement
        z_seat_dot_data = y_data[1]  # seat velocity
        z_s_data = y_data[2]  # sprung mass displacement
        z_s_dot_data = y_data[3]  # sprung mass velocity
        z_u_data = y_data[4]  # unsprung mass displacement
        z_u_dot_data = y_data[5]  # unsprung mass velocity

        # Calculate accelerations using velocity gradients
        z_seat_ddot_data = np.gradient(z_seat_dot_data, time_data)  # seat acceleration
        z_s_ddot_data = np.gradient(z_s_dot_data, time_data)  # sprung mass acceleration
        z_u_ddot_data = np.gradient(z_u_dot_data, time_data)  # unsprung mass acceleration

        # Create two subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=configuration.PLOT_STYLE['figure_size'])

        # First subplot: Accelerations
        ax1.plot(time_data, z_seat_ddot_data, label="Seat acceleration",
                linewidth=configuration.PLOT_STYLE['line_width'],
                color=configuration.PLOT_STYLE['colors'][0])
        ax1.plot(time_data, z_s_ddot_data, label="Sprung mass acceleration",
                linewidth=configuration.PLOT_STYLE['line_width'],
                color=configuration.PLOT_STYLE['colors'][1])
        ax1.plot(time_data, z_u_ddot_data, label="Unsprung mass acceleration",
                linewidth=configuration.PLOT_STYLE['line_width'],
                color=configuration.PLOT_STYLE['colors'][2])
        
        ax1.set_title("Seat-Added Quarter Car Simulation Results - Accelerations",
                     fontsize=configuration.PLOT_STYLE['title_size'],
                     fontweight=configuration.PLOT_STYLE['title_weight'])
        ax1.set_xlabel("Time [s]", fontsize=configuration.PLOT_STYLE['axis_label_size'])
        ax1.set_ylabel("Acceleration [m/s²]", fontsize=configuration.PLOT_STYLE['axis_label_size'])
        ax1.legend(fontsize=configuration.PLOT_STYLE['legend_font_size'],
                  loc=configuration.PLOT_STYLE['legend_location'])
        ax1.grid(True, linewidth=configuration.PLOT_STYLE['grid_style'].get('linewidth', 1))

        # Second subplot: Displacements
        ax2.plot(time_data, road_profile, label="Road profile",
                linewidth=configuration.PLOT_STYLE['line_width'],
                color=configuration.PLOT_STYLE['colors'][3])
        ax2.plot(time_data, z_seat_data, label="Seat displacement",
                linewidth=configuration.PLOT_STYLE['line_width'],
                color=configuration.PLOT_STYLE['colors'][4])
        ax2.plot(time_data, z_s_data, label="Sprung mass displacement",
                linewidth=configuration.PLOT_STYLE['line_width'],
                color=configuration.PLOT_STYLE['colors'][5])
        ax2.plot(time_data, z_u_data, label="Unsprung mass displacement",
                linewidth=configuration.PLOT_STYLE['line_width'],
                color=configuration.PLOT_STYLE['colors'][6])
        
        ax2.set_title("Seat-Added Quarter Car Simulation Results - Displacements",
                     fontsize=configuration.PLOT_STYLE['title_size'],
                     fontweight=configuration.PLOT_STYLE['title_weight'])
        ax2.set_xlabel("Time [s]", fontsize=configuration.PLOT_STYLE['axis_label_size'])
        ax2.set_ylabel("Displacement [m]", fontsize=configuration.PLOT_STYLE['axis_label_size'])
        ax2.legend(fontsize=configuration.PLOT_STYLE['legend_font_size'],
                  loc=configuration.PLOT_STYLE['legend_location'])
        ax2.grid(True, linewidth=configuration.PLOT_STYLE['grid_style'].get('linewidth', 1))

        plt.tight_layout()
        plt.show()

class HalfCarPlottingStrategy(PlottingStrategy):
    def plot(self, analysis_data):
        time_data = np.array(analysis_data['results']['t'])
        y_data = np.array(analysis_data['results']['y'])

        z_s_data = y_data[0]
        theta_data = y_data[2]
        z_u_f_data = y_data[4]
        z_u_r_data = y_data[6]

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))
        
        ax1.plot(time_data, z_s_data, label="Sprung mass displacement")
        ax1.plot(time_data, z_u_f_data, label="Front unsprung displacement")
        ax1.plot(time_data, z_u_r_data, label="Rear unsprung displacement")
        ax1.set_title("Half Car Simulation Results - Displacements")
        ax1.set_xlabel("Time [s]")
        ax1.set_ylabel("Displacement [m]")
        ax1.legend()
        ax1.grid(True, linewidth=configuration.PLOT_STYLE['grid_style'].get('linewidth', 1))

        ax2.plot(time_data, theta_data, label="Pitch angle")
        ax2.set_title("Half Car Simulation Results - Pitch Angle")
        ax2.set_xlabel("Time [s]")
        ax2.set_ylabel("Angle [rad]")
        ax2.legend()
        ax2.grid(True, linewidth=configuration.PLOT_STYLE['grid_style'].get('linewidth', 1))

        plt.tight_layout()
        plt.show()

class PerformanceMetricsStrategy(ABC):
    @abstractmethod
    def calculate_performance_metrics(self, analysis_data):
        pass    

class QuarterCarPerformanceMetricsStrategy(PerformanceMetricsStrategy):
    def __init__(self, params = QuarterCarOutouts()):
        self.params = params
    def calculate_performance_metrics(self, analysis_data):
        """
        Calculates and displays performance metrics for quarter car simulation.

        Args:
            analysis_data (dict): Dictionary containing simulation results and metadata.

        Updates:
            self.params: Updates the QuarterCarOutputs dataclass with calculated metrics.
        """
        # Implement performance metrics calculation for quarter car
        name = analysis_data["name"]
        execution_date = analysis_data["execution_date"]


        time_data = np.array(analysis_data['results']['t'])
        y_data = np.array(analysis_data['results']['y'])
        

        z_s_data = y_data[0]
        z_s_dot_data = y_data[1]
        z_u_data = y_data[2]
        z_u_dot_data = y_data[3]

        # Calculate accelerations
        z_s_ddot_data = np.gradient(z_s_dot_data, time_data)
        z_u_ddot_data = np.gradient(z_u_dot_data, time_data)

        self.params.acc_ms_max = max(z_s_ddot_data)
        self.params.vel_ms_max = max(z_s_dot_data)
        self.params.disp_ms_max = max(z_s_data)
        self.params.acc_mu_max = max(z_u_ddot_data)
        self.params.vel_mu_max = max(z_u_dot_data)
        self.params.disp_mu_max = max(z_u_data)
        self.params.rms_acc_ms = np.sqrt(np.mean(z_s_ddot_data**2))
        self.params.disp_range = np.ptp(z_s_data)

        # Get significant figures from configuration
        sig_figs = configuration.TABLE_STYLE['significant_figures']
        
        print("\n" + "="*60)
        print(f" Performance Metrics for {name}")
        print(f" {execution_date}")
        print("="*60)
        
        print("\nSprung Mass Metrics:")
        print("-"*30)
        print(f"{'Displacement (max):':<20} {self.params.disp_ms_max:>.{sig_figs['displacement']}f} m")
        print(f"{'Velocity (max):':<20} {self.params.vel_ms_max:>.{sig_figs['velocity']}f} m/s")
        print(f"{'Acceleration (max):':<20} {self.params.acc_ms_max:>.{sig_figs['acceleration']}f} m/s²")
        print(f"{'RMS Acceleration:':<20} {self.params.rms_acc_ms:>.{sig_figs['acceleration']}f} m/s²")
        print(f"{'Displacement Range:':<20} {self.params.disp_range:>.{sig_figs['displacement']}f} m")
        
        print("\nUnsprung Mass Metrics:")
        print("-"*30)
        print(f"{'Displacement (max):':<20} {self.params.disp_mu_max:>.{sig_figs['displacement']}f} m")
        print(f"{'Velocity (max):':<20} {self.params.vel_mu_max:>.{sig_figs['velocity']}f} m/s")
        print(f"{'Acceleration (max):':<20} {self.params.acc_mu_max:>.{sig_figs['acceleration']}f} m/s²")
        print("\n")

class SeatAddedQuarterCarPerformanceMetricsStrategy(PerformanceMetricsStrategy):
    def calculate_performance_metrics(self, analysis_data):
        pass