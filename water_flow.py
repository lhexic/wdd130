from pytest import approx
import pytest

def water_column_height(tower_height, tank_height):
    """
    Calculates the height of a column of water from a tower height and a tank wall height.

    Args:
        tower_height (float): Height of the tower.
        tank_height (float): Height of the tank walls.

    Returns:
        float: Height of the water column.
    """
    return tower_height + 3 * tank_height / 4

def pressure_gain_from_water_height(height):
    """
    Calculates the pressure caused by Earth’s gravity pulling on the water stored in an elevated tank.

    Args:
        height (float): Height of the water column in meters.

    Returns:
        float: Pressure in kilopascals.
    """
    g = 9.80665
    rho = 998.2
    return rho * g * height / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    Calculates the water pressure lost because of the friction between the water and the walls of a pipe.

    Args:
        pipe_diameter (float): Diameter of the pipe in meters.
        pipe_length (float): Length of the pipe in meters.
        friction_factor (float): Pipe's friction factor.
        fluid_velocity (float): Velocity of the water flowing through the pipe in meters/second.

    Returns:
        float: Pressure loss in kilopascals.
    """
    rho = 998.2
    return -(friction_factor * pipe_length * rho * fluid_velocity**2) / (2000 * pipe_diameter)
