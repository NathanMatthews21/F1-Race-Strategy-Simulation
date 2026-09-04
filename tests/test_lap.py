from unittest.mock import patch

from simulator.models.circuit import Circuit
from simulator.models.driver import Driver
from simulator.models.car import Car
from simulator.models.tyre import Tyre

from simulator.engine.lap import calculate_lap_time


def test_lap_time():

    circuit = Circuit(
        name="Test Circuit",
        country="Test",
        laps=50,
        lap_distance_km=5.0,
        base_lap_time=90.0,
        pit_lane_loss=22.0,
        fuel_effect_per_kg=0.035,
    )

    driver = Driver(
        name="Test Driver",
        pace_delta=-0.2,
        consistency=0.1,
    )

    car = Car(
        team="Test Team",
        pace_delta=-0.3,
    )

    tyre = Tyre(
        compound="MEDIUM",
        base_pace_delta=0.0,
        degradation_per_lap=0.05,
        age=10,
    )

    with patch(
        "simulator.engine.lap.random.gauss",
        return_value=0.0,
    ):

        lap_time = calculate_lap_time(
            circuit=circuit,
            driver=driver,
            car=car,
            tyre=tyre,
            fuel_remaining=100.0,
        )

    expected = (
        90.0
        - 0.2
        - 0.3
        + 0.0
        + 0.5
        + 3.5
    )

    assert lap_time == expected