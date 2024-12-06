import unittest
import numpy as np
from models import *
from simulation import *
from road import *
from plotting import *


class TestQuarterCar(unittest.TestCase):

    # Test constants for step road
    STEP_ROAD_EXPECTED = {
        'max_sprung_acceleration': 15.386916361628323,
        'max_unsprung_acceleration': 171.60065388963767,
        'max_sprung_displacement': 0.07390742168018162,
        'max_unsprung_displacement': 0.06714602293214444,
        'max_sprung_velocity': 0.554060203059533,
        'max_unsprung_velocity': 1.9309438353238166,
        'displacement_range': 0.07390742168018162
    }

    SINUSOIDAL_ROAD_EXPECTED = {
        'max_sprung_acceleration': 3.5591494252038913,
        'max_unsprung_acceleration': 12.068842052417153,
        'max_sprung_displacement': 0.08011198494030058,
        'max_unsprung_displacement': 0.05486751905605679,
        'max_sprung_velocity': 0.5199219600697521,
        'max_unsprung_velocity': 0.4131121720109896,
        'displacement_range': 0.1621008775870691
    }

    CHIRP_ROAD_EXPECTED = {
        'max_sprung_acceleration': 7.474427720331205,
        'max_unsprung_acceleration': 61.594736646897005,
        'max_sprung_displacement': 0.01276413585710415,
        'max_unsprung_displacement': 0.016527832606433836,
        'max_sprung_velocity': 0.1763552214450166,
        'max_unsprung_velocity': 0.9668079157116246,
        'displacement_range': 0.02754548767244589
    }


    def setUp(self):
        self.car_parameters = QuarterCarParams(
            ms=270,
            mu=60,
            ks=27000,
            ku=200000,
            cs=2000
        )
        self.initial_conditions = QuarterCarInitialConditions()
        self.quarter_car = QuarterCarModel(self.car_parameters, self.initial_conditions)

    def _run_simulation_and_get_results(self, road_profile, time_range, time_points, name):
        simulation_control = SimulationControl(
            self.quarter_car, 
            road_profile, 
            time_range, 
            time_points, 
            name=name
        )
        simulation_control.run_simulation()
        
        collector = SimulationCollector()
        collector.add_analysis(simulation_control)
        
        result_visualization = ResultsVisualization(collector.get_analyses())
        result_visualization.calculate_performance_metrics()
        return result_visualization.performance_metric_strategy.params

    def test_quarter_car_step_road(self):

        """
        Vehicle model parameters are taken from the postgraduate thesis named The modelling and analysing of 
        the vehicle seat vibrations to ride comfort
        """

        road_profile_step = RoadProfile(profile_type="step", amplitude=0.05, activation_time = 1)
        result = self._run_simulation_and_get_results(road_profile_step, (0,3), np.linspace(0,3,5000), "Step Road")

        self.assertAlmostEqual(result.acc_mu_max, self.STEP_ROAD_EXPECTED['max_unsprung_acceleration'])
        self.assertAlmostEqual(result.acc_ms_max, self.STEP_ROAD_EXPECTED['max_sprung_acceleration'])
        self.assertAlmostEqual(result.vel_ms_max, self.STEP_ROAD_EXPECTED['max_sprung_velocity'])
        self.assertAlmostEqual(result.vel_mu_max, self.STEP_ROAD_EXPECTED['max_unsprung_velocity'])
        self.assertAlmostEqual(result.disp_ms_max, self.STEP_ROAD_EXPECTED['max_sprung_displacement'])
        self.assertAlmostEqual(result.disp_mu_max, self.STEP_ROAD_EXPECTED['max_unsprung_displacement'])
        self.assertAlmostEqual(result.disp_range, self.STEP_ROAD_EXPECTED['displacement_range'])

    def test_quarter_car_sinusoidal_road(self):

        """
        Vehicle model parameters are taken from the postgraduate thesis named The modelling and analysing of 
        the vehicle seat vibrations to ride comfort
        """    

        road_profile_sinusoidal = RoadProfile(profile_type="sinusoidal", amplitude=0.05, frequency = 1)
        result = self._run_simulation_and_get_results(road_profile_sinusoidal, (0,3), np.linspace(0,3,5000), "Sinusoidal Road")

        self.assertAlmostEqual(result.acc_mu_max, self.SINUSOIDAL_ROAD_EXPECTED['max_unsprung_acceleration'])
        self.assertAlmostEqual(result.acc_ms_max, self.SINUSOIDAL_ROAD_EXPECTED['max_sprung_acceleration'])
        self.assertAlmostEqual(result.vel_ms_max, self.SINUSOIDAL_ROAD_EXPECTED['max_sprung_velocity'])
        self.assertAlmostEqual(result.vel_mu_max, self.SINUSOIDAL_ROAD_EXPECTED['max_unsprung_velocity'])
        self.assertAlmostEqual(result.disp_ms_max, self.SINUSOIDAL_ROAD_EXPECTED['max_sprung_displacement'])
        self.assertAlmostEqual(result.disp_mu_max, self.SINUSOIDAL_ROAD_EXPECTED['max_unsprung_displacement'])
        self.assertAlmostEqual(result.disp_range, self.SINUSOIDAL_ROAD_EXPECTED['displacement_range'])

    def test_quarter_car_chirp_road(self):
        """
        Vehicle model parameters are taken from the postgraduate thesis named The modelling and analysing of 
        the vehicle seat vibrations to ride comfort
        """


        road_profile_chirp = RoadProfile(profile_type="chirp", amplitude=0.01, initial_frequency=0, final_frequency=20, end_time=5)
        result = self._run_simulation_and_get_results(road_profile_chirp, (0,5), np.linspace(0,5,50000), "Chirp Road")

        self.assertAlmostEqual(result.acc_mu_max, self.CHIRP_ROAD_EXPECTED['max_unsprung_acceleration'])
        self.assertAlmostEqual(result.acc_ms_max, self.CHIRP_ROAD_EXPECTED['max_sprung_acceleration'])
        self.assertAlmostEqual(result.vel_ms_max, self.CHIRP_ROAD_EXPECTED['max_sprung_velocity'])
        self.assertAlmostEqual(result.vel_mu_max, self.CHIRP_ROAD_EXPECTED['max_unsprung_velocity'])
        self.assertAlmostEqual(result.disp_ms_max, self.CHIRP_ROAD_EXPECTED['max_sprung_displacement'])
        self.assertAlmostEqual(result.disp_mu_max, self.CHIRP_ROAD_EXPECTED['max_unsprung_displacement'])
        self.assertAlmostEqual(result.disp_range, self.CHIRP_ROAD_EXPECTED['displacement_range'])

if __name__ == '__main__':
    unittest.main()

    