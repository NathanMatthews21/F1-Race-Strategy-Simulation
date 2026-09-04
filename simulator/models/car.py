from dataclasses import dataclass


@dataclass
class Car:
    team: str

    # Pace relative to the circuit baseline.
    # Negative = faster.
    pace_delta: float = 0.0

    # Multiplier applied to tyre degradation.
    # 1.0 = neutral
    # <1.0 = better tyre management
    # >1.0 = worse tyre management
    tyre_degradation_multiplier: float = 1.0