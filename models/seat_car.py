import numpy as np
from dataclasses import asdict
from .base import VehicleModel
from .parameters import SeatAddedQuarterCarParams, SeatAddedQuarterCarModelInitialConditions

class SeatAddedQuarterCarModel(VehicleModel):
    """Model representing a quarter car with an added seat for dynamic analysis."""

    def __init__(self, 
                 params: SeatAddedQuarterCarParams = SeatAddedQuarterCarParams(),
                 initial_conditions: SeatAddedQuarterCarModelInitialConditions = SeatAddedQuarterCarModelInitialConditions()):
        """
        Initialize the SeatAddedQuarterCarModel with parameters and initial conditions.

        Args:
            params (SeatAddedQuarterCarParams): Parameters for the seat added quarter car model.
            initial_conditions (SeatAddedQuarterCarModelInitialConditions): Initial conditions for the model.
        """
        super().__init__(
            params=asdict(params),
            initial_conditions=list(asdict(initial_conditions).values())
        )

    def equations_of_motion(self, y: np.ndarray, t: float, u: callable) -> np.ndarray:
        """
        Compute the equations of motion for the seat added quarter car model.

        Args:
            y (np.ndarray): State vector.
            t (float): Time variable.
            u (callable): Function to provide road input.

        Returns:
            np.ndarray: Derivatives of the state vector.
        """
        z_seat, z_seat_dot, z_s, z_s_dot, z_u, z_u_dot = y
        
        # Extract parameters
        ms, m_seat, mu = self.params['ms'], self.params['m_seat'], self.params['mu']
        ks, cs = self.params['ks'], self.params['cs']
        k_seat, c_seat = self.params['k_seat'], self.params['c_seat']
        ku = self.params['ku']
        z_r = u(t)
        
        # Calculate accelerations
        z_seat_ddot = (-k_seat * (z_seat - z_s) - c_seat * (z_seat_dot - z_s_dot)) / m_seat
        z_s_ddot = (k_seat * (z_seat - z_s) + c_seat * (z_seat_dot - z_s_dot) - ks * (z_s - z_u) - cs * (z_s_dot - z_u_dot)) / ms
        z_u_ddot = (ks * (z_s - z_u) + cs * (z_s_dot - z_u_dot) - ku * (z_u - z_r)) / mu
        
        return np.array([z_seat_dot, z_seat_ddot, z_s_dot, z_s_ddot, z_u_dot, z_u_ddot])

