from dataclasses import dataclass

@dataclass
class QuarterCarParams:
    """
    Parameters for a quarter-car vehicle suspension model.
    
    This model represents a basic 2-DOF system with sprung and unsprung masses,
    connected by suspension elements (spring and damper) and a tire spring.
    """
    ms: float = 250  # Sprung mass [kg]
    mu: float = 50   # Unsprung mass [kg]
    ks: float = 15000  # Sprung stiffness [N/m]
    cs: float = 1000   # Sprung damping [Ns/m]
    ku: float = 150000 # Unsprung stiffness [N/m]

@dataclass
class QuarterCarInitialConditions:
    """
    Initial conditions for the quarter-car model simulation.
    
    Defines the initial displacements and velocities for both
    the sprung and unsprung masses.
    """
    z_s    : float = 0  # Sprung displacement [m]
    z_s_dot: float = 0  # Sprung velocity [m/s]
    z_u    : float = 0  # Unsprung displacement [m]
    z_u_dot: float = 0  # Unsprung velocity [m/s]

@dataclass
class SeatAddedQuarterCarParams:
    """
    Parameters for an enhanced quarter-car model that includes a seat suspension.
    
    This 3-DOF model extends the basic quarter-car model by adding
    a seat mass with its own suspension elements.
    """
    ms    : float = 250     # Sprung mass [kg]
    m_seat: float = 35      # Seat mass [kg]
    k_seat: float = 1000    # Seat suspension stiffness [N/m]
    c_seat: float = 500     # Seat suspension damping [Ns/m]
    mu    : float = 50      # Unsprung mass [kg]
    ks    : float = 15000   # Sprung stiffness [N/m]
    cs    : float = 1000    # Sprung damping [Ns/m]
    ku    : float = 150000  # Unsprung stiffness [N/m]

@dataclass
class SeatAddedQuarterCarModelInitialConditions:
    """
    Initial conditions for the quarter-car model with seat suspension.
    
    Defines the initial displacements and velocities for the seat mass,
    sprung mass, and unsprung mass.
    """
    z_seat    : float = 0  # Seat displacement [m]
    z_seat_dot: float = 0  # Seat velocity [m/s]
    z_s       : float = 0  # Sprung displacement [m]
    z_s_dot   : float = 0  # Sprung velocity [m/s]
    z_u       : float = 0  # Unsprung displacement [m]
    z_u_dot   : float = 0  # Unsprung velocity [m/s]

@dataclass
class HalfCarModelParams:
    """
    Parameters for a half-car vehicle suspension model.
    
    This 4-DOF model represents the vehicle's pitch motion and vertical
    displacement, with separate front and rear suspension systems.
    """
    ms  : float = 500    # Sprung mass [kg]
    I   : float = 1000   # Mass moment of inertia [kg⋅m²]
    mu_f: float = 25     # Front unsprung mass [kg]
    ks_f: float = 10000  # Front sprung stiffness [N/m]
    cs_f: float = 1000    # Front sprung damping [Ns/m]
    ku_f: float = 75000  # Front unsprung stiffness [N/m]
    mu_r: float = 25     # Rear unsprung mass [kg]
    ks_r: float = 10000  # Rear sprung stiffness [N/m]
    cs_r: float = 1000    # Rear sprung damping [Ns/m]
    ku_r: float = 70000  # Rear unsprung stiffness [N/m]
    a   : float = 0.5    # Front distance [m]
    b   : float = 0.5    # Rear distance [m]
    longitudial_velocity : float = 12 # Longitudinal velocity [m/s]

@dataclass
class HalfCarModelInitialConditions:
    """
    Initial conditions for the half-car model simulation.
    
    Defines the initial displacements, velocities, angles, and angular
    velocities for the sprung mass and both front and rear unsprung masses.
    """
    z_s       : float = 0  # Sprung mass displacement [m]
    z_s_dot   : float = 0  # Sprung mass velocity [m/s]
    theta     : float = 0  # Pitch angle [rad]
    theta_dot : float = 0  # Pitch angular velocity [rad/s]
    z_u_f     : float = 0  # Front unsprung displacement [m]
    z_u_f_dot : float = 0  # Front unsprung velocity [m/s]
    z_u_r     : float = 0  # Rear unsprung displacement [m]
    z_u_r_dot : float = 0  # Rear unsprung velocity [m/s]

