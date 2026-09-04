from simulator.models.circuit import Circuit
from simulator.models.driver import Driver
from simulator.models.car import Car
from simulator.models.tyre import Tyre
from simulator.engine.race import Race


def test_race_completes():

    circuit = Circuit(
        name="Test Circuit",
        country="Test",
        laps=10,
        lap_distance_km=5.0,
        base_lap_time=90.0,
        pit_lane_loss=22.0,
        fuel_effect_per_kg=0.035,
    )

    driver = Driver(
        name="Test Driver",
        pace_delta=0.0,
        consistency=0.0,
    )

    car = Car(
        team="Test Team",
        pace_delta=0.0,
        tyre_degradation_multiplier=1.0,
    )

    tyre = Tyre(
        compound="MEDIUM",
        base_pace_delta=0.0,
        degradation_per_lap=0.05,
    )

    race = Race(
        circuit=circuit,
        driver=driver,
        car=car,
        tyre=tyre,
        starting_fuel=100.0,
    )

    result = race.run()

    assert len(result.laps) == 10
    assert result.total_time > 0
    assert result.average_lap_time > 0


def test_tyre_ages_through_race():

    circuit = Circuit(
        name="Test Circuit",
        country="Test",
        laps=10,
        lap_distance_km=5.0,
        base_lap_time=90.0,
        pit_lane_loss=22.0,
        fuel_effect_per_kg=0.035,
    )

    driver = Driver(
        name="Test Driver",
        consistency=0.0,
    )

    car = Car(team="Test Team")

    tyre = Tyre(
        compound="MEDIUM",
        base_pace_delta=0.0,
        degradation_per_lap=0.05,
    )

    race = Race(
        circuit=circuit,
        driver=driver,
        car=car,
        tyre=tyre,
        starting_fuel=100.0,
    )

    result = race.run()

    assert result.laps[0].tyre_age == 0
    assert result.laps[-1].tyre_age == 9
    assert tyre.age == 10