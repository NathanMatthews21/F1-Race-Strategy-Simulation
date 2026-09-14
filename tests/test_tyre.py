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

def test_linear_degradation():

    tyre = Tyre(
        compound="TEST",
        base_pace_delta=0.0,
        degradation_per_lap=0.05,
        degradation_exponent=1.0,
        age=10,
    )

    assert tyre.lap_degradation() == pytest.approx(0.5)


def test_accelerating_degradation():

    tyre = Tyre(
        compound="TEST",
        base_pace_delta=0.0,
        degradation_per_lap=0.05,
        degradation_exponent=1.10,
        age=10,
    )

    assert tyre.lap_degradation() > 0.5


def test_degradation_respects_car_multiplier():

    tyre = Tyre(
        compound="MEDIUM",
        base_pace_delta=0.0,
        degradation_per_lap=0.05,
        degradation_exponent=1.0,
        age=10,
    )

    normal = tyre.lap_degradation(
        car_multiplier=1.0
    )

    bad_management = tyre.lap_degradation(
        car_multiplier=1.5
    )

    assert bad_management == pytest.approx(
        normal * 1.5
    )


def test_fresh_tyre_has_zero_degradation():

    tyre = create_tyre("SOFT")

    assert tyre.age == 0
    assert tyre.lap_degradation() == 0.0

def test_clone_creates_fresh_tyre():

    tyre = create_tyre("SOFT")

    tyre.advance()
    tyre.advance()
    tyre.advance()

    clone = tyre.clone()

    assert clone.compound == tyre.compound
    assert clone.base_pace_delta == tyre.base_pace_delta
    assert clone.degradation_per_lap == tyre.degradation_per_lap
    assert clone.degradation_exponent == tyre.degradation_exponent

    assert clone.age == 0