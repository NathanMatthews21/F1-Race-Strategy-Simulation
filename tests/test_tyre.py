import pytest

from simulator.models.tyre import Tyre, create_tyre


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

    assert tyre.lap_degradation() == pytest.approx(0.5)


def test_tyre_advances():

    tyre = Tyre(
        compound="MEDIUM",
        base_pace_delta=0.0,
        degradation_per_lap=0.05,
    )

    tyre.advance()

    assert tyre.age == 1


def test_soft_is_faster_than_medium():

    soft = create_tyre("SOFT")
    medium = create_tyre("MEDIUM")

    assert soft.base_pace_delta < medium.base_pace_delta


def test_medium_is_faster_than_hard():

    medium = create_tyre("MEDIUM")
    hard = create_tyre("HARD")

    assert medium.base_pace_delta < hard.base_pace_delta


def test_soft_degrades_faster_than_medium():

    soft = create_tyre("SOFT")
    medium = create_tyre("MEDIUM")

    assert soft.degradation_per_lap > medium.degradation_per_lap


def test_medium_degrades_faster_than_hard():

    medium = create_tyre("MEDIUM")
    hard = create_tyre("HARD")

    assert medium.degradation_per_lap > hard.degradation_per_lap


def test_unknown_compound_raises_error():

    with pytest.raises(ValueError):

        create_tyre("INTERMEDIATE")