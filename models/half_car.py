import numpy as np
from dataclasses import asdict
from .base import VehicleModel
from .parameters import HalfCarModelParams, HalfCarModelInitialConditions


class HalfCarModel(VehicleModel):
    """Model representing a half car for dynamic analysis."""

    def __init__(
        self,
        params: HalfCarModelParams = HalfCarModelParams(),
        initial_conditions: HalfCarModelInitialConditions = HalfCarModelInitialConditions(),
    ):
        """
        Initialize the HalfCarModel with parameters and initial conditions.

        Args:
            params (HalfCarModelParams): Parameters for the half car model.
            initial_conditions (HalfCarModelInitialConditions): Initial conditions for the model.
        """
        super().__init__(
            params=asdict(params),
            initial_conditions=list(asdict(initial_conditions).values()),
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
        ms, I = self.params["ms"], self.params["I"]
        mu_f, mu_r = self.params["mu_f"], self.params["mu_r"]
        ks_f, ks_r = self.params["ks_f"], self.params["ks_r"]
        cs_f, cs_r = self.params["cs_f"], self.params["cs_r"]
        ku_f, ku_r = self.params["ku_f"], self.params["ku_r"]
        a, b = self.params["a"], self.params["b"]
        longitudinal_velocity = self.params["longitudial_velocity"]

        x_s, x_s_dot, theta, theta_dot, x_u_f, x_u_f_dot, x_u_r, x_u_r_dot = y

        # external displacements of tires
        delay_time = (a + b) / longitudinal_velocity
        x_g_f = u(t)  # front tire external displacement
        x_g_r = u(max(0, t - delay_time))  # rear tire external displacement with delay

        # Calculate accelerations
        F_u_r = ku_r * (x_g_r - x_u_r)
        F_u_f = ku_f * (x_g_f - x_u_f)
        F_s_r = ks_r * (x_u_r - x_s + b * theta) + cs_r * (
            x_u_r_dot - x_s_dot + b * theta_dot
        )
        F_s_f = ks_f * (x_u_f - x_s - a * theta) + cs_f * (
            x_u_f_dot - x_s_dot - a * theta_dot
        )

        # Calculate accelerations
        x_u_r_ddot = (F_u_r - F_s_r) / mu_r
        x_u_f_ddot = (F_u_f - F_s_f) / mu_f
        x_s_ddot = (F_s_r + F_s_f) / ms
        theta_ddot = (a * F_s_f - b * F_s_r) / I

        return np.array(
            [
                x_s_dot,
                x_s_ddot,
                theta_dot,
                theta_ddot,
                x_u_f_dot,
                x_u_f_ddot,
                x_u_r_dot,
                x_u_r_ddot,
            ]
        )
