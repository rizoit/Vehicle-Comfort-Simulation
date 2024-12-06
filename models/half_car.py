import numpy as np
from dataclasses import asdict
from .base import VehicleModel
from .parameters import HalfCarModelParams, HalfCarModelInitialConditions

class HalfCarModel(VehicleModel):
    """Model representing a half car for dynamic analysis."""

    def __init__(self,
                 params: HalfCarModelParams = HalfCarModelParams(),
                 initial_conditions: HalfCarModelInitialConditions = HalfCarModelInitialConditions()):
        """
        Initialize the HalfCarModel with parameters and initial conditions.

        Args:
            params (HalfCarModelParams): Parameters for the half car model.
            initial_conditions (HalfCarModelInitialConditions): Initial conditions for the model.
        """
        super().__init__(
            params=asdict(params),
            initial_conditions=list(asdict(initial_conditions).values())
        )

    def equations_of_motion(self, y: np.ndarray, t: float, u: callable) -> np.ndarray:
        """
        Compute the equations of motion for the half car model.

        Args:
            y (np.ndarray): State vector.
            t (float): Time variable.
            u (callable): Function to provide road input.

        Returns:
            np.ndarray: Derivatives of the state vector.
        """
        z_s, z_s_dot, theta, theta_dot, z_u_f, z_u_f_dot, z_u_r, z_u_r_dot = y
        
        # Extract parameters
        ms, I = self.params['ms'], self.params['I']
        mu_f, mu_r = self.params['mu_f'], self.params['mu_r']
        ks_f, ks_r = self.params['ks_f'], self.params['ks_r']
        cs_f, cs_r = self.params['cs_f'], self.params['cs_r']
        kt_f, kt_r = self.params['kt_f'], self.params['kt_r']
        a, b = self.params['a'], self.params['b']
        
        # Road inputs
        z_r_f, z_r_r = u(t)
        
        # Calculate forces
        F_s_f = ks_f * (z_s - z_u_f + a * theta) + cs_f * (z_s_dot - z_u_f_dot + a * theta_dot)
        F_s_r = ks_r * (z_s - z_u_r - b * theta) + cs_r * (z_s_dot - z_u_r_dot - b * theta_dot)
        F_t_f = kt_f * (z_u_f - z_r_f)
        F_t_r = kt_r * (z_u_r - z_r_r)
        
        # Calculate accelerations
        z_s_ddot = (-F_s_f - F_s_r) / ms
        theta_ddot = (a * F_s_f - b * F_s_r) / I
        z_u_f_ddot = (F_s_f - F_t_f) / mu_f
        z_u_r_ddot = (F_s_r - F_t_r) / mu_r
        
        return np.array([z_s_dot, z_s_ddot, theta_dot, theta_ddot, z_u_f_dot, z_u_f_ddot, z_u_r_dot, z_u_r_ddot])

