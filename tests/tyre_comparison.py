from unittest.mock import patch

from simulator.models.circuit import Circuit
from simulator.models.driver import Driver
from simulator.models.car import Car
from simulator.analysis.tyre_comparison import (
    simulate_compound,
    compare_compounds,
)


def create_test_circuit():
    return Circuit(
        name="Test Circuit",
        country="Test",
        laps=10,
        lap_distance_km=5.0,
        base_lap_time=90.0,
        pit_lane_loss=22.0,
        fuel_effect_per_kg=0.035,
    )


def create_test_driver():
    return Driver(
        name="Test Driver",
        pace_delta=0.0,
        consistency=0.0,
    )


def create_test_car():
    return Car(
        team="Test Team",
        pace_delta=0.0,
        tyre_degradation_multiplier=1.0,
    )


def test_compound_simulation_has_correct_number_of_laps():

    circuit = create_test_circuit()
    driver = create_test_driver()
    car = create_test_car()

    with patch(
        "simulator.engine.lap.random.gauss",
        return_value=0.0,
    ):

        result = simulate_compound(
            circuit=circuit,
            driver=driver,
            car=car,
            compound="MEDIUM",
        )

    assert len(result.lap_times) == circuit.laps


def test_compound_total_time_equals_lap_sum():

    circuit = create_test_circuit()
    driver = create_test_driver()
    car = create_test_car()

    with patch(
        "simulator.engine.lap.random.gauss",
        return_value=0.0,
    ):

        result = simulate_compound(
            circuit=circuit,
            driver=driver,
            car=car,
            compound="MEDIUM",
        )

    assert result.total_time == sum(result.lap_times)


def test_all_three_compounds_are_compared():

    circuit = create_test_circuit()
    driver = create_test_driver()
    car = create_test_car()

    with patch(
        "simulator.engine.lap.random.gauss",
        return_value=0.0,
    ):

        results = compare_compounds(
            circuit=circuit,
            driver=driver,
            car=car,
        )

    compounds = [
        result.compound
        for result in results
    ]

    assert compounds == [
        "SOFT",
        "MEDIUM",
        "HARD",
    ]


def test_soft_is_fastest_on_new_tyre():

    circuit = create_test_circuit()
    driver = create_test_driver()
    car = create_test_car()

    with patch(
        "simulator.engine.lap.random.gauss",
        return_value=0.0,
    ):

        soft = simulate_compound(
            circuit,
            driver,
            car,
            "SOFT",
        )

        hard = simulate_compound(
            circuit,
            driver,
            car,
            "HARD",
        )

    assert soft.lap_times[0] < hard.lap_times[0]


def test_hard_degrades_less_than_soft():

    circuit = create_test_circuit()
    driver = create_test_driver()
    car = create_test_car()

    with patch(
        "simulator.engine.lap.random.gauss",
        return_value=0.0,
    ):

        soft = simulate_compound(
            circuit,
            driver,
            car,
            "SOFT",
        )

        hard = simulate_compound(
            circuit,
            driver,
            car,
            "HARD",
        )

    soft_degradation = (
        soft.lap_times[-1]
        - soft.lap_times[0]
    )

    hard_degradation = (
        hard.lap_times[-1]
        - hard.lap_times[0]
    )

    assert hard_degradation < soft_degradation