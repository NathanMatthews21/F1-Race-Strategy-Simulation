from dataclasses import dataclass


@dataclass
class Tyre:
    compound: str
    base_pace_delta: float
    degradation_per_lap: float
    age: int = 0

    def lap_degradation(self, car_multiplier: float = 1.0) -> float:
        """
        Calculate the time penalty caused by tyre age.

        Age 0 = no degradation penalty.
        Age 10 = 10 × degradation_per_lap.
        """

        return self.age * self.degradation_per_lap * car_multiplier

    def advance(self) -> None:
        """Age the tyre by one lap."""
        self.age += 1