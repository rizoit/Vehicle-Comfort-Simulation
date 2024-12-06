import numpy as np
from models import *
from simulation import *
from road import *
#from ..visualizer import *

def test():
    """
    Vehicle model parameters are taken from the postgraduate thesis named The modelling and analysing of 
    the vehicle seat vibrations to ride comfort
    """

    sesion_name = 'quarter_car_ThesisWork.json'
    def first_run(sesion_name):

        # Vehicle parameters
        car_parameters = QuarterCarParams(ms=270,
                                        mu=60,
                                        ks=27000,
                                        ku=200000,
                                        cs=2000)

        initial_conditions = QuarterCarInitialConditions()

        quarter_car = QuarterCarModel(car_parameters, initial_conditions)

        # Road profiles
        road_profile_step = RoadProfile(profile_type="step", amplitude=0.05, activation_time = 1)
        road_profile_sinusoidal = RoadProfile(profile_type="sinusoidal", amplitude=0.05, frequency = 1)
        road_profile_chirp = RoadProfile(profile_type="chirp", amplitude=0.01, initial_frequency=0, final_frequency=20, end_time=5)

        sc_step = SimulationControl(quarter_car, road_profile_step, (0,3), np.linspace(0,3,5000), name="Step Road")
        sc_sinusoidal = SimulationControl(quarter_car, road_profile_sinusoidal, (0,3), np.linspace(0,3,5000), name="Sinusoidal Road")   
        sc_chirp = SimulationControl(quarter_car, road_profile_chirp, (0,5), np.linspace(0,5,50000), name="Chirp Road")

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
    result_visualization = ResultsVisualization(result_collector.get_analyses("Step Road"))
    result_visualization.calculate_performance_metrics()
    result_visualization.plot_results()
    result = result_visualization.performance_metric_strategy.params

 

    ## Sinusoidal Road  
    result_visualization = ResultsVisualization(result_collector.get_analyses("Sinusoidal Road"))
    result_visualization.calculate_performance_metrics()
    result_visualization.plot_results()


    ## Chirp Road
    result_visualization = ResultsVisualization(result_collector.get_analyses("Chirp Road"))
    result_visualization.calculate_performance_metrics()
    result_visualization.plot_results()


