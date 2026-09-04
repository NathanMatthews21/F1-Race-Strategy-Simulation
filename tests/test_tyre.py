from simulator.models.tyre import Tyre


def test_new_tyre_has_no_degradation():

    tyre = Tyre(
        compound="MEDIUM",
        base_pace_delta=0.0,
        degradation_per_lap=0.05,
    )

    assert tyre.lap_degradation() == 0.0


def test_tyre_degrades_with_age():

    tyre = Tyre(
        compound="MEDIUM",
        base_pace_delta=0.0,
        degradation_per_lap=0.05,
        age=10,
    )

    assert tyre.lap_degradation() == 0.5


def test_tyre_advances():

    tyre = Tyre(
        compound="MEDIUM",
        base_pace_delta=0.0,
        degradation_per_lap=0.05,
    )

    tyre.advance()

    assert tyre.age == 1