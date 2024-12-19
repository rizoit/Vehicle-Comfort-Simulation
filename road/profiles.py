import numpy as np
import matplotlib.pyplot as plt


class RoadProfile:
    """Class representing different types of road profiles."""

    def __init__(self, profile_type, **kwargs):
        """
        Initialize the RoadProfile with a specific type and parameters.

        Args:
            profile_type (str): Type of the road profile (e.g., 'sinusoidal', 'step', 'chirp').
            **kwargs: Additional parameters for the road profile.
        """
        self.profile_type = profile_type
        self.params = kwargs

    def get_profile(self, t):
        """
        Get the road profile value at a given time.

        Args:
            t (float): Time variable.

        Returns:
            float: Road profile displacement at time t.

        Raises:
            ValueError: If the road profile type is unsupported.
        """
        if self.profile_type == "sinusoidal":
            return self.params["amplitude"] * np.sin(
                2 * np.pi * self.params["frequency"] * t
            )
        elif self.profile_type == "step":
            return self.params["amplitude"] * (t >= self.params["activation_time"])
        elif self.profile_type == "chirp":
            return self.params["amplitude"] * np.sin(
                2
                * np.pi
                * (
                    self.params["initial_frequency"]
                    + (
                        self.params["final_frequency"]
                        - self.params["initial_frequency"]
                    )
                    / (2 * self.params["end_time"])
                    * t
                )
                * t
            )
        else:
            raise ValueError("Unsupported road profile type")

    def plot_profile(self, t):
        """
        Plot the road profile over time.

        Args:
            t (np.ndarray): Array of time values.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(t, self.get_profile(t))
        plt.title(f"{self.profile_type.capitalize()} Road Profile")
        plt.xlabel("Time [s]")
        plt.ylabel("Displacement [m]")
        plt.grid(True)
        plt.show()
