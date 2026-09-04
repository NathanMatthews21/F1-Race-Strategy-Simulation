from dataclasses import dataclass


@dataclass
class Driver:
    name: str

    # Pace relative to the circuit baseline.
    # Negative = faster.
    pace_delta: float = 0.0

    # Standard deviation of lap-to-lap variation.
    consistency: float = 0.10