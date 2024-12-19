import unittest
import numpy as np
from models import *
from simulation import *
from road import *
from plotting import *


class TestQuarterCar(unittest.TestCase):

    # Test constants for step road
    STEP_ROAD_EXPECTED = {
        "max_sprung_acceleration": 15.38859832396733,
        "max_unsprung_acceleration": 160.89125876494427,
        "max_sprung_displacement": 0.07390710561305074,
        "max_unsprung_displacement": 0.06715420768333684,
        "max_sprung_velocity": 0.5541078222815486,
        "max_unsprung_velocity": 1.9306282383726092,
        "displacement_range": 0.07390710561305074,
    }

    SINUSOIDAL_ROAD_EXPECTED = {
        "max_sprung_acceleration": 3.5582466629346037,
        "max_unsprung_acceleration": 12.065105987809346,
        "max_sprung_displacement": 0.08011192265613985,
        "max_unsprung_displacement": 0.05486710705675937,
        "max_sprung_velocity": 0.5198766140961355,
        "max_unsprung_velocity": 0.41321255862596357,
        "displacement_range": 0.16210081100056986,
    }

    CHIRP_ROAD_EXPECTED = {
        "max_sprung_acceleration": 7.4849665908606475,
        "max_unsprung_acceleration": 61.54989098355391,
        "max_sprung_displacement": 0.012764114722983123,
        "max_unsprung_displacement": 0.01653820707838068,
        "max_sprung_velocity": 0.17634872356693387,
        "max_unsprung_velocity": 0.9677287302895712,
        "displacement_range": 0.027545460568617126,
    }

    def setUp(self):
        self.car_parameters = QuarterCarParams(
            ms=270, mu=60, ks=27000, ku=200000, cs=2000
        )
        self.initial_conditions = QuarterCarInitialConditions()
        self.quarter_car = QuarterCarModel(self.car_parameters, self.initial_conditions)

    def _run_simulation_and_get_results(
        self, road_profile, time_range, time_points, name
    ):
        simulation_control = SimulationControl(
            self.quarter_car, road_profile, time_range, time_points, name=name
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

        road_profile_step = RoadProfile(
            profile_type="step", amplitude=0.05, activation_time=1
        )
        result = self._run_simulation_and_get_results(
            road_profile_step, (0, 3), np.linspace(0, 3, 5000), "Step Road"
        )

        self.assertAlmostEqual(
            result.acc_mu_max, self.STEP_ROAD_EXPECTED["max_unsprung_acceleration"]
        )
        self.assertAlmostEqual(
            result.acc_ms_max, self.STEP_ROAD_EXPECTED["max_sprung_acceleration"]
        )
        self.assertAlmostEqual(
            result.vel_ms_max, self.STEP_ROAD_EXPECTED["max_sprung_velocity"]
        )
        self.assertAlmostEqual(
            result.vel_mu_max, self.STEP_ROAD_EXPECTED["max_unsprung_velocity"]
        )
        self.assertAlmostEqual(
            result.disp_ms_max, self.STEP_ROAD_EXPECTED["max_sprung_displacement"]
        )
        self.assertAlmostEqual(
            result.disp_mu_max, self.STEP_ROAD_EXPECTED["max_unsprung_displacement"]
        )
        self.assertAlmostEqual(
            result.disp_range, self.STEP_ROAD_EXPECTED["displacement_range"]
        )

    def test_quarter_car_sinusoidal_road(self):
        """
        Vehicle model parameters are taken from the postgraduate thesis named The modelling and analysing of
        the vehicle seat vibrations to ride comfort
        """

        road_profile_sinusoidal = RoadProfile(
            profile_type="sinusoidal", amplitude=0.05, frequency=1
        )
        result = self._run_simulation_and_get_results(
            road_profile_sinusoidal, (0, 3), np.linspace(0, 3, 5000), "Sinusoidal Road"
        )

        self.assertAlmostEqual(
            result.acc_mu_max,
            self.SINUSOIDAL_ROAD_EXPECTED["max_unsprung_acceleration"],
        )
        self.assertAlmostEqual(
            result.acc_ms_max, self.SINUSOIDAL_ROAD_EXPECTED["max_sprung_acceleration"]
        )
        self.assertAlmostEqual(
            result.vel_ms_max, self.SINUSOIDAL_ROAD_EXPECTED["max_sprung_velocity"]
        )
        self.assertAlmostEqual(
            result.vel_mu_max, self.SINUSOIDAL_ROAD_EXPECTED["max_unsprung_velocity"]
        )
        self.assertAlmostEqual(
            result.disp_ms_max, self.SINUSOIDAL_ROAD_EXPECTED["max_sprung_displacement"]
        )
        self.assertAlmostEqual(
            result.disp_mu_max,
            self.SINUSOIDAL_ROAD_EXPECTED["max_unsprung_displacement"],
        )
        self.assertAlmostEqual(
            result.disp_range, self.SINUSOIDAL_ROAD_EXPECTED["displacement_range"]
        )

    def test_quarter_car_chirp_road(self):
        """
        Vehicle model parameters are taken from the postgraduate thesis named The modelling and analysing of
        the vehicle seat vibrations to ride comfort
        """

        road_profile_chirp = RoadProfile(
            profile_type="chirp",
            amplitude=0.01,
            initial_frequency=0,
            final_frequency=20,
            end_time=5,
        )
        result = self._run_simulation_and_get_results(
            road_profile_chirp, (0, 5), np.linspace(0, 5, 50000), "Chirp Road"
        )

        self.assertAlmostEqual(
            result.acc_mu_max, self.CHIRP_ROAD_EXPECTED["max_unsprung_acceleration"]
        )
        self.assertAlmostEqual(
            result.acc_ms_max, self.CHIRP_ROAD_EXPECTED["max_sprung_acceleration"]
        )
        self.assertAlmostEqual(
            result.vel_ms_max, self.CHIRP_ROAD_EXPECTED["max_sprung_velocity"]
        )
        self.assertAlmostEqual(
            result.vel_mu_max, self.CHIRP_ROAD_EXPECTED["max_unsprung_velocity"]
        )
        self.assertAlmostEqual(
            result.disp_ms_max, self.CHIRP_ROAD_EXPECTED["max_sprung_displacement"]
        )
        self.assertAlmostEqual(
            result.disp_mu_max, self.CHIRP_ROAD_EXPECTED["max_unsprung_displacement"]
        )
        self.assertAlmostEqual(
            result.disp_range, self.CHIRP_ROAD_EXPECTED["displacement_range"]
        )


class TestSeatAddedQuarterCar(unittest.TestCase):

    STEP_ROAD_EXPECTED = {
        "max_sprung_acceleration": 14.893825422624559,
        "max_unsprung_acceleration": 160.89124264875176,
        "max_sprung_displacement": 0.07178058450651129,
        "max_unsprung_displacement": 0.0669867663934107,
        "max_sprung_velocity": 0.5166384982571068,
        "max_unsprung_velocity": 1.9299889181838727,
        "displacement_range_ms": 0.07178058450651129,
        "displacement_range_seat": 0.09084792213928093,
    }

    SINUSOIDAL_ROAD_EXPECTED = {
        "max_sprung_acceleration": 4.052932843453405,
        "max_unsprung_acceleration": 12.065454414292276,
        "max_sprung_displacement": 0.09919821102123214,
        "max_unsprung_displacement": 0.05760592765872133,
        "max_sprung_velocity": 0.6312383291925634,
        "max_unsprung_velocity": 0.41226217913709345,
        "displacement_range_ms": 0.19773108769632725,
        "displacement_range_seat": 0.2515730408079771,
    }

    CHIRP_ROAD_EXPECTED = {
        "max_sprung_acceleration": 7.6035966336528835,
        "max_unsprung_acceleration": 61.79692507451281,
        "max_sprung_displacement": 0.011682728415670196,
        "max_unsprung_displacement": 0.016626327699072987,
        "max_sprung_velocity": 0.15098154842495703,
        "max_unsprung_velocity": 0.9720534629645587,
        "displacement_range_ms": 0.021046873282359373,
        "displacement_range_seat": 0.03346328781249304,
    }

    def setUp(self):
        self.car_parameters = SeatAddedQuarterCarParams(
            ms=270,
            mu=60,
            m_seat=88,
            ks=27000,
            ku=200000,
            k_seat=16000,
            cs=2000,
            c_seat=500,  # seat damping coefficient
        )

        self.initial_conditions = SeatAddedQuarterCarModelInitialConditions()
        self.seat_added_quarter_car = SeatAddedQuarterCarModel(
            self.car_parameters, self.initial_conditions
        )

    def _run_simulation_and_get_results(
        self, road_profile, time_range, time_points, name
    ):
        simulation_control = SimulationControl(
            self.seat_added_quarter_car,
            road_profile,
            time_range,
            time_points,
            name=name,
        )
        simulation_control.run_simulation()

        collector = SimulationCollector()
        collector.add_analysis(simulation_control)

        result_visualization = ResultsVisualization(collector.get_analyses())
        result_visualization.calculate_performance_metrics()
        return result_visualization.performance_metric_strategy.params

    def test_seat_added_quarter_car_step_road(self):
        """
        Vehicle model parameters are taken from the postgraduate thesis named The modelling and analysing of
        the vehicle seat vibrations to ride comfort
        """
        road_profile_step = RoadProfile(
            profile_type="step", amplitude=0.05, activation_time=1
        )
        result = self._run_simulation_and_get_results(
            road_profile_step, (0, 3), np.linspace(0, 3, 5000), "Step Road"
        )

        self.assertAlmostEqual(
            result.acc_mu_max,
            self.STEP_ROAD_EXPECTED["max_unsprung_acceleration"],
            places=2,
        )
        self.assertAlmostEqual(
            result.acc_ms_max,
            self.STEP_ROAD_EXPECTED["max_sprung_acceleration"],
            places=2,
        )
        self.assertAlmostEqual(
            result.vel_ms_max, self.STEP_ROAD_EXPECTED["max_sprung_velocity"], places=2
        )
        self.assertAlmostEqual(
            result.vel_mu_max,
            self.STEP_ROAD_EXPECTED["max_unsprung_velocity"],
            places=2,
        )
        self.assertAlmostEqual(
            result.disp_ms_max,
            self.STEP_ROAD_EXPECTED["max_sprung_displacement"],
            places=2,
        )
        self.assertAlmostEqual(
            result.disp_mu_max,
            self.STEP_ROAD_EXPECTED["max_unsprung_displacement"],
            places=2,
        )
        self.assertAlmostEqual(
            result.disp_range_ms,
            self.STEP_ROAD_EXPECTED["displacement_range_ms"],
            places=2,
        )
        self.assertAlmostEqual(
            result.disp_range_seat,
            self.STEP_ROAD_EXPECTED["displacement_range_seat"],
            places=2,
        )

    def test_seat_added_quarter_car_sinusoidal_road(self):
        """
        Vehicle model parameters are taken from the postgraduate thesis named The modelling and analysing of
        the vehicle seat vibrations to ride comfort
        """
        road_profile_sinusoidal = RoadProfile(
            profile_type="sinusoidal", amplitude=0.05, frequency=1
        )
        result = self._run_simulation_and_get_results(
            road_profile_sinusoidal, (0, 3), np.linspace(0, 3, 5000), "Sinusoidal Road"
        )

        self.assertAlmostEqual(
            result.acc_mu_max,
            self.SINUSOIDAL_ROAD_EXPECTED["max_unsprung_acceleration"],
            places=2,
        )
        self.assertAlmostEqual(
            result.acc_ms_max,
            self.SINUSOIDAL_ROAD_EXPECTED["max_sprung_acceleration"],
            places=2,
        )
        self.assertAlmostEqual(
            result.vel_ms_max,
            self.SINUSOIDAL_ROAD_EXPECTED["max_sprung_velocity"],
            places=2,
        )
        self.assertAlmostEqual(
            result.vel_mu_max,
            self.SINUSOIDAL_ROAD_EXPECTED["max_unsprung_velocity"],
            places=2,
        )
        self.assertAlmostEqual(
            result.disp_ms_max,
            self.SINUSOIDAL_ROAD_EXPECTED["max_sprung_displacement"],
            places=2,
        )
        self.assertAlmostEqual(
            result.disp_mu_max,
            self.SINUSOIDAL_ROAD_EXPECTED["max_unsprung_displacement"],
            places=2,
        )
        self.assertAlmostEqual(
            result.disp_range_ms,
            self.SINUSOIDAL_ROAD_EXPECTED["displacement_range_ms"],
            places=2,
        )
        self.assertAlmostEqual(
            result.disp_range_seat,
            self.SINUSOIDAL_ROAD_EXPECTED["displacement_range_seat"],
            places=2,
        )

    def test_seat_added_quarter_car_chirp_road(self):
        """
        Vehicle model parameters are taken from the postgraduate thesis named The modelling and analysing of
        the vehicle seat vibrations to ride comfort
        """
        road_profile_chirp = RoadProfile(
            profile_type="chirp",
            amplitude=0.01,
            initial_frequency=0,
            final_frequency=20,
            end_time=5,
        )
        result = self._run_simulation_and_get_results(
            road_profile_chirp, (0, 5), np.linspace(0, 5, 50000), "Chirp Road"
        )

        self.assertAlmostEqual(
            result.acc_mu_max,
            self.CHIRP_ROAD_EXPECTED["max_unsprung_acceleration"],
            places=2,
        )
        self.assertAlmostEqual(
            result.acc_ms_max,
            self.CHIRP_ROAD_EXPECTED["max_sprung_acceleration"],
            places=2,
        )
        self.assertAlmostEqual(
            result.vel_ms_max, self.CHIRP_ROAD_EXPECTED["max_sprung_velocity"], places=2
        )
        self.assertAlmostEqual(
            result.vel_mu_max,
            self.CHIRP_ROAD_EXPECTED["max_unsprung_velocity"],
            places=2,
        )
        self.assertAlmostEqual(
            result.disp_ms_max,
            self.CHIRP_ROAD_EXPECTED["max_sprung_displacement"],
            places=2,
        )
        self.assertAlmostEqual(
            result.disp_mu_max,
            self.CHIRP_ROAD_EXPECTED["max_unsprung_displacement"],
            places=2,
        )
        self.assertAlmostEqual(
            result.disp_range_ms,
            self.CHIRP_ROAD_EXPECTED["displacement_range_ms"],
            places=2,
        )
        self.assertAlmostEqual(
            result.disp_range_seat,
            self.CHIRP_ROAD_EXPECTED["displacement_range_seat"],
            places=2,
        )


if __name__ == "__main__":
    unittest.main()
