import json
from datetime import datetime

class SimulationCollector:
    """Class for collecting and managing simulation analyses."""

    def __init__(self):
        """Initialize the SimulationCollector with an empty analyses dictionary."""
        self.analyses = {}

    def add_analysis(self, simulation_control):
        """
        Add a simulation analysis to the collector.

        Args:
            simulation_control (SimulationControl): The simulation control object containing analysis data.
        """
        analysis_data = {
            "name": simulation_control.name,
            "execution_date": simulation_control.execution_date or datetime.now().isoformat(),
            "vehicle_model": {
                "type": type(simulation_control.vehicle_model).__name__,
                "params": simulation_control.vehicle_model.params,
                "initial_conditions": simulation_control.vehicle_model.initial_conditions
            },
            "road_profile": {
                "type": simulation_control.road_profile.profile_type,
                "params": simulation_control.road_profile.params
            },
            "results": {
                "t": simulation_control.results.t.tolist(),
                "y": simulation_control.results.y.tolist(),
                "road_profile": simulation_control.results.road_profile.tolist()
            },
            "t_span": simulation_control.t_span,
            "t_eval": simulation_control.t_eval.tolist()
        }
        
        self.analyses[simulation_control.name] = analysis_data

    def get_analysis(self, name):
        """
        Retrieve an analysis by name.

        Args:
            name (str): The name of the analysis.

        Returns:
            dict: The analysis data, or None if not found.
        """
        return self.analyses.get(name)

    def list_analyses(self):
        """
        List all analysis names in the collector.

        Returns:
            list: A list of analysis names.
        """
        return list(self.analyses.keys())

    def export_results(self, filename):
        """
        Export all analyses to a JSON file.

        Args:
            filename (str): The filename to export the results to.
        """
        with open(filename, 'w') as f:
            json.dump(self.analyses, f, indent=2)

    def import_results(self, filename):
        """
        Import results from a JSON file and add them to the current collector.

        Args:
            filename (str): The filename to import results from.
        """
        with open(filename, 'r') as f:
            data = json.load(f)
        
        for name, analysis in data.items():
            self.analyses[name] = analysis

    def compare_analyses(self, analysis_names):
        """
        Compare multiple analyses by their names.

        Args:
            analysis_names (list): List of analysis names to compare.

        Returns:
            dict: A dictionary of the selected analyses.
        """
        return {name: self.analyses[name] for name in analysis_names if name in self.analyses}

    def add_analysis_from_data(self, analysis_data):
        """
        Add analysis directly from a data dictionary.

        Args:
            analysis_data (dict): The analysis data dictionary.

        Raises:
            ValueError: If the analysis data format is invalid.
        """
        if not isinstance(analysis_data, dict) or "name" not in analysis_data:
            raise ValueError("Invalid analysis data format")
            
        self.analyses[analysis_data["name"]] = analysis_data

    def get_analyses(self, name=None):
        """
        Retrieve simulation results by name or the last added analysis if name is not provided.

        Args:
            name (str, optional): The name of the analysis. Defaults to None.

        Returns:
            dict: The analysis data. Returns the last added analysis if name is None,
                 or None if no analyses exist or the specified name is not found.
        """
        if name is None:
            # Return the last added analysis if exists
            if not self.analyses:
                return None
            return list(self.analyses.values())[-1]
        
        # Return the specified analysis
        return self.analyses.get(name)

