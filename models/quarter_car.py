import numpy as np
from dataclasses import asdict
from .base import VehicleModel
from .parameters import QuarterCarParams, QuarterCarInitialConditions


class QuarterCarModel(VehicleModel):
    """Model representing a quarter car for dynamic analysis."""

    def __init__(
        self, params: QuarterCarParams, initial_conditions: QuarterCarInitialConditions
    ):
        """
        Initialize the QuarterCarModel with parameters and initial conditions.

        Args:
            params (QuarterCarParams): Parameters for the quarter car model.
            initial_conditions (QuarterCarInitialConditions): Initial conditions for the model.
        """
        super().__init__(
            params=asdict(params),
            initial_conditions=list(asdict(initial_conditions).values()),
        )

    def equations_of_motion(self, y: np.ndarray, t: float, u: callable) -> np.ndarray:
        """
        Compute the equations of motion for the quarter car model.

        Args:
            y (np.ndarray): State vector.
            t (float): Time variable.
            u (callable): Function to provide road input.

        Returns:
            np.ndarray: Derivatives of the state vector.
        """
        z_s, z_s_dot, z_u, z_u_dot = y

        # Extract parameters
        ms, mu = self.params["ms"], self.params["mu"]
        ks, cs = self.params["ks"], self.params["cs"]
        ku = self.params["ku"]
        z_ur = u(t)

        # Calculate accelerations
        z_s_ddot = (-ks * (z_s - z_u) - cs * (z_s_dot - z_u_dot)) / ms
        z_u_ddot = (
            ks * (z_s - z_u) + cs * (z_s_dot - z_u_dot) - ku * (z_u - z_ur)
        ) / mu

        return np.array([z_s_dot, z_s_ddot, z_u_dot, z_u_ddot])
