from plotting.strategies import QuarterCarPlottingStrategy, SeatAddedQuarterCarPlottingStrategy, HalfCarPlottingStrategy
import numpy as np
from plotting.strategies import QuarterCarPerformanceMetricsStrategy, SeatAddedQuarterCarPerformanceMetricsStrategy, HalfCarPerformanceMetricsStrategy

class ResultsVisualization:
    """Class for visualizing simulation results using different plotting strategies."""

    def __init__(self, analysis_data):
        """
        Initialize the ResultsVisualization with analysis data.

        Args:
            analysis_data (dict): The data from the simulation analysis.
        """
        self.analysis_data = analysis_data
        self.plotting_strategy = self._get_plotting_strategy()
        self.performance_metric_strategy = self._get_metrics_strategy()

    def _get_plotting_strategy(self):
        """
        Determine the appropriate plotting strategy based on the vehicle model type.

        Returns:
            PlottingStrategy: An instance of the appropriate plotting strategy.
        
        Raises:
            ValueError: If the vehicle model type is unsupported.
        """
        model_type = self.analysis_data['vehicle_model']['type']
        if model_type == 'QuarterCarModel':
            return QuarterCarPlottingStrategy()
        elif model_type == 'SeatAddedQuarterCarModel':
            return SeatAddedQuarterCarPlottingStrategy()
        elif model_type == 'HalfCarModel':
            return HalfCarPlottingStrategy()
        else:
            raise ValueError("Unsupported vehicle model for plotting")

    def _get_metrics_strategy(self):
        """
        Determine the appropriate performance metrics strategy based on the vehicle model type.

        Returns:
            PerformanceMetricsStrategy: An instance of the appropriate performance metrics strategy.
        
        Raises:
            ValueError: If the vehicle model type is unsupported.
        """
        model_type = self.analysis_data['vehicle_model']['type']
        if model_type == 'QuarterCarModel':
            return QuarterCarPerformanceMetricsStrategy()
        if model_type == 'SeatAddedQuarterCarModel':
            return SeatAddedQuarterCarPerformanceMetricsStrategy()
        if model_type == 'HalfCarModel':
            return HalfCarPerformanceMetricsStrategy()
        else:
            raise ValueError("Unsupported vehicle model for performance metrics calculation")
    
    def plot_results(self):
        """Plot the results using the selected plotting strategy."""
        self.plotting_strategy.plot(self.analysis_data)

    def calculate_performance_metrics(self):
        """Calculate performance metrics for the simulation results."""
        self.performance_metric_strategy.calculate_performance_metrics(self.analysis_data)
        

