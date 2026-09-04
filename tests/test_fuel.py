import pytest

from simulator.models.circuit import Circuit

def test_fuel_effect():

    circuit = Circuit(
        name="Test Circuit",
        country="Test",
        laps=50,
        lap_distance_km=5.0,
        base_lap_time=90.0,
        pit_lane_loss=22.0,
        fuel_effect_per_kg=0.035,
    )

    fuel = 100.0

    expected_effect = 3.5

    actual_effect = fuel * circuit.fuel_effect_per_kg

    assert actual_effect == pytest.approx(expected_effect)