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

@dataclass
class SeatAddedQuarterCarOutouts():
    acc_seat_max: float = 0.0
    vel_seat_max: float = 0.0
    disp_seat_max: float = 0.0

    acc_ms_max: float = 0.0
    vel_ms_max: float = 0.0
    disp_ms_max: float = 0.0

    acc_mu_max: float = 0.0     
    vel_mu_max: float = 0.0
    disp_mu_max: float = 0.0

    rms_acc_ms: float = 0.0
    disp_range_ms: float = 0.0

    rms_acc_seat: float = 0.0
    disp_range_seat: float = 0.0

@dataclass
class HalfCarOutouts():
    acc_ms_max: float = 0.0 # Sprung mass acceleration max
    vel_ms_max: float = 0.0 # Sprung mass velocity max
    disp_ms_max: float = 0.0 # Sprung mass displacement max

    disp_pitch_max:float = 0.0 #Sprung mass angular displacement
    vel_pitch_max:float = 0.0 #Sprung mass angular velocity
    acc_pitch_max:float = 0.0 #Sprung mass angular acceleration

    acc_mu_r_max: float = 0.0 # Rear unsprung mass acceleration max
    vel_mu_r_max: float = 0.0 # Rear unsprung mass velocity max
    disp_mu_r_max: float = 0.0 # Rear unsprung mass displacement max

    acc_mu_f_max: float = 0.0 # Front unsprung mass acceleration max
    vel_mu_f_max: float = 0.0 # Front unsprung mass velocity max
    disp_mu_f_max: float = 0.0 # Front unsprung mass displacement max

    rms_acc_ms: float = 0.0 #rms value of sprung mass acceleration 
    rms_acc_pitch: float = 0.0 #rms value of sprung mass pitch acceleration
    disp_range: float = 0.0 #displacement range of sprung mass

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
        # Extract data
        time_data = np.array(analysis_data['results']['t'])
        y_data = np.array(analysis_data['results']['y'])
        road_profile = np.array(analysis_data['results']['road_profile'])
        # Displacements and angles
        z_s_data = y_data[0]  # sprung mass displacement
        z_s_dot_data = y_data[1]  # sprung mass velocity
        theta_data = y_data[2]  # pitch angle
        theta_dot_data = y_data[3]  # pitch angular velocity
        z_u_f_data = y_data[4]  # front unsprung displacement
        z_u_f_dot_data = y_data[5]  # front unsprung velocity
        z_u_r_data = y_data[6]  # rear unsprung displacement
        z_u_r_dot_data = y_data[7]  # rear unsprung velocity

        # Calculate accelerations
        z_s_ddot_data = np.gradient(z_s_dot_data, time_data)  # sprung mass acceleration
        theta_ddot_data = np.gradient(theta_dot_data, time_data)  # pitch acceleration
        z_u_f_ddot_data = np.gradient(z_u_f_dot_data, time_data)  # front unsprung acceleration
        z_u_r_ddot_data = np.gradient(z_u_r_dot_data, time_data)  # rear unsprung acceleration

        # Create figure with two subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=configuration.PLOT_STYLE['figure_size'])

        # First subplot: Accelerations with secondary axis for pitch acceleration
        ax1_twin = ax1.twinx()  # Create secondary y-axis

        # Plot accelerations on primary axis
        ax1.plot(time_data, z_s_ddot_data, label="Sprung mass acceleration",
                linewidth=configuration.PLOT_STYLE['line_width'],
                color=configuration.PLOT_STYLE['colors'][0])
        ax1.plot(time_data, z_u_f_ddot_data, label="Front unsprung acceleration",
                linewidth=configuration.PLOT_STYLE['line_width'],
                color=configuration.PLOT_STYLE['colors'][1])
        ax1.plot(time_data, z_u_r_ddot_data, label="Rear unsprung acceleration",
                linewidth=configuration.PLOT_STYLE['line_width'],
                color=configuration.PLOT_STYLE['colors'][2])
       

        # Plot pitch acceleration on secondary axis
        ax1_twin.plot(time_data, theta_ddot_data, label="Pitch acceleration",
                     linewidth=configuration.PLOT_STYLE['line_width'],
                     color=configuration.PLOT_STYLE['colors'][3],
                     linestyle='--')

        # Configure first subplot
        ax1.set_title("Half Car Simulation Results - Accelerations",
                     fontsize=configuration.PLOT_STYLE['title_size'],
                     fontweight=configuration.PLOT_STYLE['title_weight'])
        ax1.set_xlabel("Time [s]", fontsize=configuration.PLOT_STYLE['axis_label_size'])
        ax1.set_ylabel("Linear Acceleration [m/s²]", fontsize=configuration.PLOT_STYLE['axis_label_size'])
        ax1_twin.set_ylabel("Angular Acceleration [rad/s²]", fontsize=configuration.PLOT_STYLE['axis_label_size'])

        # Combine legends from both axes
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax1_twin.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2,
                  fontsize=configuration.PLOT_STYLE['legend_font_size'],
                  loc=configuration.PLOT_STYLE['legend_location'])

        ax1.grid(True, linewidth=configuration.PLOT_STYLE['grid_style'].get('linewidth', 1))

        # Second subplot: Displacements with secondary axis for pitch angle
        ax2_twin = ax2.twinx()  # Create secondary y-axis

        # Plot displacements on primary axis
        ax2.plot(time_data, z_s_data, label="Sprung mass displacement",
                linewidth=configuration.PLOT_STYLE['line_width'],
                color=configuration.PLOT_STYLE['colors'][0])
        ax2.plot(time_data, z_u_f_data, label="Front unsprung displacement",
                linewidth=configuration.PLOT_STYLE['line_width'],
                color=configuration.PLOT_STYLE['colors'][1])
        ax2.plot(time_data, z_u_r_data, label="Rear unsprung displacement",
                linewidth=configuration.PLOT_STYLE['line_width'],
                color=configuration.PLOT_STYLE['colors'][2])
        ax2.plot(time_data, road_profile, label="Road profile",
                linewidth=configuration.PLOT_STYLE['line_width'],
                color=configuration.PLOT_STYLE['colors'][3])

        # Plot pitch angle on secondary axis
        ax2_twin.plot(time_data, theta_data*180/np.pi, label="Pitch angle",
                     linewidth=configuration.PLOT_STYLE['line_width'],
                     color=configuration.PLOT_STYLE['colors'][3],
                     linestyle='--')

        # Configure second subplot
        ax2.set_title("Half Car Simulation Results - Displacements",
                     fontsize=configuration.PLOT_STYLE['title_size'],
                     fontweight=configuration.PLOT_STYLE['title_weight'])
        ax2.set_xlabel("Time [s]", fontsize=configuration.PLOT_STYLE['axis_label_size'])
        ax2.set_ylabel("Linear Displacement [m]", fontsize=configuration.PLOT_STYLE['axis_label_size'])
        ax2_twin.set_ylabel("Pitch Angle [degree]", fontsize=configuration.PLOT_STYLE['axis_label_size'])

        # Combine legends from both axes
        lines1, labels1 = ax2.get_legend_handles_labels()
        lines2, labels2 = ax2_twin.get_legend_handles_labels()
        ax2.legend(lines1 + lines2, labels1 + labels2,
                  fontsize=configuration.PLOT_STYLE['legend_font_size'],
                  loc=configuration.PLOT_STYLE['legend_location'])

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
    def __init__(self, params=SeatAddedQuarterCarOutouts()):
        self.params = params

    def calculate_performance_metrics(self, analysis_data):
        """
        Calculates and displays performance metrics for seat-added quarter car simulation.

        Args:
            analysis_data (dict): Dictionary containing simulation results and metadata.

        Updates:
            self.params: Updates the SeatAddedQuarterCarOutouts dataclass with calculated metrics.
        """
        name = analysis_data["name"]
        execution_date = analysis_data["execution_date"]

        time_data = np.array(analysis_data['results']['t'])
        y_data = np.array(analysis_data['results']['y'])

        # Extract data
        z_seat_data = y_data[0]  # seat displacement
        z_seat_dot_data = y_data[1]  # seat velocity
        z_s_data = y_data[2]  # sprung mass displacement
        z_s_dot_data = y_data[3]  # sprung mass velocity
        z_u_data = y_data[4]  # unsprung mass displacement
        z_u_dot_data = y_data[5]  # unsprung mass velocity

        # Calculate accelerations
        z_seat_ddot_data = np.gradient(z_seat_dot_data, time_data)  # seat acceleration
        z_s_ddot_data = np.gradient(z_s_dot_data, time_data)  # sprung mass acceleration
        z_u_ddot_data = np.gradient(z_u_dot_data, time_data)  # unsprung mass acceleration

        # Update params with calculated metrics
        self.params.acc_seat_max = max(abs(z_seat_ddot_data))
        self.params.vel_seat_max = max(abs(z_seat_dot_data))
        self.params.disp_seat_max = max(abs(z_seat_data))
        self.params.acc_ms_max = max(abs(z_s_ddot_data))
        self.params.vel_ms_max = max(abs(z_s_dot_data))
        self.params.disp_ms_max = max(abs(z_s_data))
        self.params.acc_mu_max = max(abs(z_u_ddot_data))
        self.params.vel_mu_max = max(abs(z_u_dot_data))
        self.params.disp_mu_max = max(abs(z_u_data))
        self.params.rms_acc_seat = np.sqrt(np.mean(z_seat_ddot_data**2))
        self.params.rms_acc_ms = np.sqrt(np.mean(z_s_ddot_data**2))
        self.params.disp_range_seat = np.ptp(z_seat_data)
        self.params.disp_range_ms = np.ptp(z_s_data)

        # Get significant figures from configuration
        sig_figs = configuration.TABLE_STYLE['significant_figures']
        
        print("\n" + "="*60)
        print(f" Performance Metrics for {name}")
        print(f" {execution_date}")
        print("="*60)
        
        print("\nSeat Metrics:")
        print("-"*30)
        print(f"{'Displacement (max):':<20} {self.params.disp_seat_max:>.{sig_figs['displacement']}f} m")
        print(f"{'Velocity (max):':<20} {self.params.vel_seat_max:>.{sig_figs['velocity']}f} m/s")
        print(f"{'Acceleration (max):':<20} {self.params.acc_seat_max:>.{sig_figs['acceleration']}f} m/s²")
        print(f"{'RMS Acceleration:':<20} {self.params.rms_acc_seat:>.{sig_figs['acceleration']}f} m/s²")
        print(f"{'Displacement Range:':<20} {self.params.disp_range_seat:>.{sig_figs['displacement']}f} m")

        print("\nSprung Mass Metrics:")
        print("-"*30)
        print(f"{'Displacement (max):':<20} {self.params.disp_ms_max:>.{sig_figs['displacement']}f} m")
        print(f"{'Velocity (max):':<20} {self.params.vel_ms_max:>.{sig_figs['velocity']}f} m/s")
        print(f"{'Acceleration (max):':<20} {self.params.acc_ms_max:>.{sig_figs['acceleration']}f} m/s²")
        print(f"{'RMS Acceleration:':<20} {self.params.rms_acc_ms:>.{sig_figs['acceleration']}f} m/s²")
        print(f"{'Displacement Range:':<20} {self.params.disp_range_ms:>.{sig_figs['displacement']}f} m")
        
        print("\nUnsprung Mass Metrics:")
        print("-"*30)
        print(f"{'Displacement (max):':<20} {self.params.disp_mu_max:>.{sig_figs['displacement']}f} m")
        print(f"{'Velocity (max):':<20} {self.params.vel_mu_max:>.{sig_figs['velocity']}f} m/s")
        print(f"{'Acceleration (max):':<20} {self.params.acc_mu_max:>.{sig_figs['acceleration']}f} m/s²")
        print("\n")

class HalfCarPerformanceMetricsStrategy(PerformanceMetricsStrategy):
    def __init__(self, params=HalfCarOutouts()):
        self.params = params

    def calculate_performance_metrics(self, analysis_data):
        """
        Calculates and displays performance metrics for half car simulation.

        Args:
            analysis_data (dict): Dictionary containing simulation results and metadata.

        Updates:
            self.params: Updates the HalfCarOutouts dataclass with calculated metrics.
        """
        name = analysis_data["name"]
        execution_date = analysis_data["execution_date"]

        time_data = np.array(analysis_data['results']['t'])
        y_data = np.array(analysis_data['results']['y'])



        # Extract data
        z_s_data = y_data[0]  # sprung mass displacement
        z_s_dot_data = y_data[1]  # sprung mass velocity
        pitch_data = y_data[2]  # pitch angle
        pitch_dot_data = y_data[3]  # pitch angular velocity
        z_u_f_data = y_data[4]  # front unsprung displacement
        z_u_f_dot_data = y_data[5]  # front unsprung velocity
        z_u_r_data = y_data[6]  # rear unsprung displacement
        z_u_r_dot_data = y_data[7]  # rear unsprung velocity

        # Calculate accelerations
        z_s_ddot_data = np.gradient(z_s_dot_data, time_data)  # sprung mass acceleration
        z_u_f_ddot_data = np.gradient(z_u_f_dot_data, time_data)  # front unsprung acceleration
        z_u_r_ddot_data = np.gradient(z_u_r_dot_data, time_data)  # rear unsprung acceleration
        pitch_ddot_data = np.gradient(pitch_dot_data, time_data)  # pitch angular acceleration

        # Update params with calculated metrics
        self.params.acc_ms_max = max(abs(z_s_ddot_data))
        self.params.vel_ms_max = max(abs(z_s_dot_data))
        self.params.disp_ms_max = max(abs(z_s_data))
        self.params.acc_mu_f_max = max(abs(z_u_f_ddot_data))
        self.params.acc_mu_r_max = max(abs(z_u_r_ddot_data))
        self.params.disp_pitch_max = max(abs(pitch_data*180/np.pi))
        self.params.vel_pitch_max = max(abs(pitch_dot_data))
        self.params.acc_pitch_max = max(abs(pitch_ddot_data))
        
        self.params.vel_mu_f_max = max(abs(z_u_f_dot_data))
        self.params.vel_mu_r_max = max(abs(z_u_r_dot_data))

        self.params.vel_mu_f_max = max(abs(z_u_f_dot_data))
        self.params.vel_mu_r_max = max(abs(z_u_r_dot_data))
        
        self.params.disp_mu_f_max = max(abs(z_u_f_data))
        self.params.disp_mu_r_max = max(abs(z_u_r_data))


        self.params.rms_acc_ms = np.sqrt(np.mean(z_s_ddot_data**2))
        self.params.rms_acc_pitch = np.sqrt(np.mean(pitch_ddot_data**2))
        
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
        print("- -"*10)
        print(f"{'Pitch Angle (max):':<20} {self.params.disp_pitch_max:>.{sig_figs['displacement']}f} Deg")
        print(f"{'Velocity (max):':<20} {self.params.vel_pitch_max:>.{sig_figs['velocity']}f} rad/s")
        print(f"{'Acceleration (max):':<20} {self.params.acc_pitch_max:>.{sig_figs['acceleration']}f} rad/s²")
        print(f"{'RMS Acceleration:':<20} {self.params.rms_acc_pitch:>.{sig_figs['acceleration']}f} m/s²")
        
        
        print("\nUnsprung Mass Metrics:")
        print("-"*30)
        print(f"{'Front Displacement (max):':<25} {self.params.disp_mu_f_max:>.{sig_figs['displacement']}f} m")
        print(f"{'Front Velocity (max):':<25} {self.params.vel_mu_f_max:>.{sig_figs['velocity']}f} m/s")
        print(f"{'Front Acceleration (max):':<25} {self.params.acc_mu_f_max:>.{sig_figs['acceleration']}f} m/s²")
        print("- -"*10)
        print(f"{'Rear Displacement (max):':<25} {self.params.disp_mu_r_max:>.{sig_figs['displacement']}f} m")
        print(f"{'Rear Velocity (max):':<25} {self.params.vel_mu_r_max:>.{sig_figs['velocity']}f} m/s")
        print(f"{'Rear Acceleration (max):':<25} {self.params.acc_mu_r_max:>.{sig_figs['acceleration']}f} m/s²")
        print("\n")




