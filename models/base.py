from abc import ABC, abstractmethod
import numpy as np


class VehicleModel(ABC):
    """Abstract base class for vehicle models."""

    def __init__(self, params: dict[str, float], initial_conditions: list[float]):
        """
        Initialize the vehicle model with parameters and initial conditions.

        Args:
            params (dict[str, float]): Model parameters.
            initial_conditions (list[float]): Initial conditions for the model.
        """
        self.params = params
        self.initial_conditions = initial_conditions

    def __repr__(self):
        return f"Parameters of this vehicle: {self.params} \n and initial conditions: {self.initial_conditions}"

    @abstractmethod
    def equations_of_motion(self, y: np.ndarray, t: float, u: callable) -> np.ndarray:
        """
        Abstract method to compute the equations of motion for the vehicle model.

        Args:
            y (np.ndarray): State vector.
            t (float): Time variable.
            u (callable): Function to provide road input.

        Returns:
            np.ndarray: Derivatives of the state vector.
        """
        pass
