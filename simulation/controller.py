from scipy.integrate import solve_ivp
from datetime import datetime

class SimulationControl:
    """Class for controlling and running vehicle model simulations."""

    def __init__(self, vehicle_model, road_profile, t_span, t_eval, name="Unnamed Simulation"):
        """
        Initialize the SimulationControl with a vehicle model, road profile, and time settings.

        Args:
            vehicle_model (VehicleModel): The vehicle model to simulate.
            road_profile (RoadProfile): The road profile for the simulation.
            t_span (tuple): The time span for the simulation.
            t_eval (np.ndarray): The time points at which to evaluate the solution.
            name (str): The name of the simulation.
        """
        self.vehicle_model = vehicle_model
        self.road_profile = road_profile
        self.t_span = t_span
        self.t_eval = t_eval
        self.results = None
        self.name = name
        self.execution_date = None

    def run_simulation(self):
        """Run the simulation using the specified vehicle model and road profile."""
        def ode_wrapper(t, y):
            return self.vehicle_model.equations_of_motion(y, t, self.road_profile.get_profile)

        self.results = solve_ivp(
            ode_wrapper,
            self.t_span,
            self.vehicle_model.initial_conditions,
            t_eval=self.t_eval,
            method='RK45'
        )
    
        # Add road profile to the results
        self.results.road_profile = self.road_profile.get_profile(self.results.t)

        # Update execution date
        self.execution_date = datetime.now().isoformat()
        

