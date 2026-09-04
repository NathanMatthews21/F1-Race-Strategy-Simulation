import random

from simulator.models.circuit import Circuit
from simulator.models.driver import Driver
from simulator.models.car import Car
from simulator.models.tyre import Tyre


def calculate_lap_time(
    circuit: Circuit,
    driver: Driver,
    car: Car,
    tyre: Tyre,
    fuel_remaining: float,
) -> float:
    """
    Calculate the lap time for a single lap.

    Returns:
        Lap time in seconds.
    """

    base_time = circuit.base_lap_time

    driver_effect = driver.pace_delta

    car_effect = car.pace_delta

    tyre_effect = tyre.base_pace_delta

    degradation_effect = tyre.lap_degradation(
        car.tyre_degradation_multiplier
    )

    fuel_effect = fuel_remaining * circuit.fuel_effect_per_kg

    random_effect = random.gauss(
        0,
        driver.consistency
    )

    lap_time = (
        base_time
        + driver_effect
        + car_effect
        + tyre_effect
        + degradation_effect
        + fuel_effect
        + random_effect
    )

    return lap_time