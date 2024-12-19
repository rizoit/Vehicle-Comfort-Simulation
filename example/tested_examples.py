import numpy as np
from models import *
from simulation import *
from road import *
import os

# from ..visualizer import *


def quarter_car():
    """
    Vehicle model parameters are taken from the postgraduate thesis named The modelling and analysing of
    the vehicle seat vibrations to ride comfort
    """

    sesion_name = "quarter_car_ThesisWork.json"

    def first_run(sesion_name):

        # Vehicle parameters
        car_parameters = QuarterCarParams(ms=270, mu=60, ks=27000, ku=200000, cs=2000)

        initial_conditions = QuarterCarInitialConditions()

        quarter_car = QuarterCarModel(car_parameters, initial_conditions)

        # Road profiles
        road_profile_step = RoadProfile(
            profile_type="step", amplitude=0.05, activation_time=1
        )
        road_profile_sinusoidal = RoadProfile(
            profile_type="sinusoidal", amplitude=0.05, frequency=1
        )
        road_profile_chirp = RoadProfile(
            profile_type="chirp",
            amplitude=0.01,
            initial_frequency=0,
            final_frequency=20,
            end_time=5,
        )

        sc_step = SimulationControl(
            quarter_car,
            road_profile_step,
            (0, 3),
            np.linspace(0, 3, 5000),
            name="Step Road",
        )
        sc_sinusoidal = SimulationControl(
            quarter_car,
            road_profile_sinusoidal,
            (0, 3),
            np.linspace(0, 3, 5000),
            name="Sinusoidal Road",
        )
        sc_chirp = SimulationControl(
            quarter_car,
            road_profile_chirp,
            (0, 5),
            np.linspace(0, 5, 50000),
            name="Chirp Road",
        )

        # Run simulations
        sc_step.run_simulation()
        sc_sinusoidal.run_simulation()
        sc_chirp.run_simulation()

        # Collect results
        results_collector = SimulationCollector()
        results_collector.add_analysis(sc_step)
        results_collector.add_analysis(sc_sinusoidal)
        results_collector.add_analysis(sc_chirp)
        results_collector.export_results(sesion_name)

    first_run(sesion_name)

    result_collector = SimulationCollector()
    result_collector.import_results(sesion_name)

    # Visualize results
    ## Step Road
    result_visualization = ResultsVisualization(
        result_collector.get_analyses("Step Road")
    )
    result_visualization.calculate_performance_metrics()
    result_visualization.plot_results()
    result = result_visualization.performance_metric_strategy.params

    ## Sinusoidal Road
    result_visualization = ResultsVisualization(
        result_collector.get_analyses("Sinusoidal Road")
    )
    result_visualization.calculate_performance_metrics()
    result_visualization.plot_results()

    ## Chirp Road
    result_visualization = ResultsVisualization(
        result_collector.get_analyses("Chirp Road")
    )
    result_visualization.calculate_performance_metrics()
    result_visualization.plot_results()


def seat_added_quarter_car():
    """
    Vehicle model parameters are taken from the postgraduate thesis named The modelling and analysing of
    the vehicle seat vibrations to ride comfort, But results of thesis work contains arguable results, so the results
    are cheched by using MSC ADAMS software.
    Even though, the reult of the code might be 5% higher than MSC ADAMS results, when simulation include high frequency.
    """
    ## TODO: Add adams model to documentations

    sesion_name = "seat_added_quarter_car_ThesisWork.json"

    def first_run(sesion_name):

        # Vehicle parameters
        car_parameters = SeatAddedQuarterCarParams(
            ms=270,
            mu=60,
            m_seat=88,
            ks=27000,
            ku=200000,
            k_seat=16000,
            cs=2000,
            c_seat=500,
        )

        initial_conditions = SeatAddedQuarterCarModelInitialConditions()

        seat_added_quarter_car = SeatAddedQuarterCarModel(
            car_parameters, initial_conditions
        )

        # Road profiles
        road_profile_step = RoadProfile(
            profile_type="step", amplitude=0.05, activation_time=1
        )
        road_profile_sinusoidal = RoadProfile(
            profile_type="sinusoidal", amplitude=0.05, frequency=1
        )
        road_profile_chirp = RoadProfile(
            profile_type="chirp",
            amplitude=0.01,
            initial_frequency=0,
            final_frequency=20,
            end_time=5,
        )

        sc_step = SimulationControl(
            seat_added_quarter_car,
            road_profile_step,
            (0, 3),
            np.linspace(0, 3, 25000),
            name="Step Road",
        )
        sc_sinusoidal = SimulationControl(
            seat_added_quarter_car,
            road_profile_sinusoidal,
            (0, 3),
            np.linspace(0, 3, 25000),
            name="Sinusoidal Road",
        )
        sc_chirp = SimulationControl(
            seat_added_quarter_car,
            road_profile_chirp,
            (0, 5),
            np.linspace(0, 5, 50000),
            name="Chirp Road",
        )

        # Run simulations
        sc_step.run_simulation()
        sc_sinusoidal.run_simulation()
        sc_chirp.run_simulation()

        # Collect results
        results_collector = SimulationCollector()
        results_collector.add_analysis(sc_step)
        results_collector.add_analysis(sc_sinusoidal)
        results_collector.add_analysis(sc_chirp)
        results_collector.export_results(sesion_name)

    first_run(sesion_name)

    result_collector = SimulationCollector()
    result_collector.import_results(sesion_name)

    # Visualize results
    ## Step Road
    result_visualization = ResultsVisualization(
        result_collector.get_analyses("Step Road")
    )
    result_visualization.calculate_performance_metrics()
    result_visualization.plot_results()

    ## Sinusoidal Road
    result_visualization = ResultsVisualization(
        result_collector.get_analyses("Sinusoidal Road")
    )
    result_visualization.calculate_performance_metrics()
    result_visualization.plot_results()

    ## Chirp Road
    result_visualization = ResultsVisualization(
        result_collector.get_analyses("Chirp Road")
    )
    result_visualization.calculate_performance_metrics()
    result_visualization.plot_results()


def half_car():
    """
    Vehicle model parameters are taken from the postgraduate thesis named The modelling and analysing of
    the vehicle seat vibrations to ride comfort. And results are cheched with msc Adams software simulation.
    Numerical Values might differe acording to steps size or error handling parameters.
    """
    ## TODO: Add adams model to documentations

    sesion_name = "half_car_ThesisWork.json"

    def first_run(sesion_name):

        # Vehicle parameters
        car_parameters = HalfCarModelParams(
            ms=550,
            mu_f=66,
            mu_r=45,
            ku_f=200000,
            ku_r=200000,
            ks_f=27000,
            ks_r=27000,
            cs_f=2000,
            cs_r=950,
            a=0.5,
            b=0.5,
            I=1200,
        )
        car_parameters.longitudial_velocity = 1

        initial_conditions = HalfCarModelInitialConditions()
        half_car = HalfCarModel(car_parameters, initial_conditions)

        # Road profiles
        road_profile_step = RoadProfile(
            profile_type="step", amplitude=0.05, activation_time=1
        )
        road_profile_sinusoidal = RoadProfile(
            profile_type="sinusoidal", amplitude=0.05, frequency=1
        )
        road_profile_chirp = RoadProfile(
            profile_type="chirp",
            amplitude=0.01,
            initial_frequency=0,
            final_frequency=20,
            end_time=5,
        )

        end_time = 3  # seconds, the simulation duration

        sc_step = SimulationControl(
            half_car,
            road_profile_step,
            (0, end_time),
            np.linspace(0, end_time, end_time * 10000),
            name="Step Road",
        )
        sc_sinusoidal = SimulationControl(
            half_car,
            road_profile_sinusoidal,
            (0, 3),
            np.linspace(0, 3, end_time * 10000),
            name="Sinusoidal Road",
        )
        sc_chirp = SimulationControl(
            half_car,
            road_profile_chirp,
            (0, 5),
            np.linspace(0, 5, 10000 * 20),
            name="Chirp Road",
        )

        # Run simulations
        sc_step.run_simulation()
        sc_sinusoidal.run_simulation()
        sc_chirp.run_simulation()

        # Collect results
        results_collector = SimulationCollector()
        results_collector.add_analysis(sc_step)
        results_collector.add_analysis(sc_sinusoidal)
        results_collector.add_analysis(sc_chirp)
        results_collector.export_results(sesion_name)

    first_run(sesion_name)

    result_collector = SimulationCollector()
    result_collector.import_results(sesion_name)

    # Visualize results
    ## Step Road
    result_visualization = ResultsVisualization(
        result_collector.get_analyses("Step Road")
    )
    result_visualization.calculate_performance_metrics()
    result_visualization.plot_results()

    ## Sinusoidal Road
    result_visualization = ResultsVisualization(
        result_collector.get_analyses("Sinusoidal Road")
    )
    result_visualization.calculate_performance_metrics()
    result_visualization.plot_results()

    ## Chirp Road
    result_visualization = ResultsVisualization(
        result_collector.get_analyses("Chirp Road")
    )
    result_visualization.calculate_performance_metrics()
    result_visualization.plot_results()
