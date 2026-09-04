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
        """

        return (
            self.age
            * self.degradation_per_lap
            * car_multiplier
        )

    def advance(self) -> None:
        """Age the tyre by one lap."""

        self.age += 1

    def clone(self) -> "Tyre":
        """
        Create a fresh set of the same compound.

        Used later when implementing pit stops.
        """

        return Tyre(
            compound=self.compound,
            base_pace_delta=self.base_pace_delta,
            degradation_per_lap=self.degradation_per_lap,
        )


def create_tyre(compound: str) -> Tyre:
    """
    Create a fresh tyre set using the default V0.2.1
    compound characteristics.
    """

    compounds = {
        "SOFT": {
            "base_pace_delta": -0.8,
            "degradation_per_lap": 0.075,
        },
        "MEDIUM": {
            "base_pace_delta": -0.4,
            "degradation_per_lap": 0.045,
        },
        "HARD": {
            "base_pace_delta": 0.0,
            "degradation_per_lap": 0.030,
        },
    }

    compound = compound.upper()

    if compound not in compounds:
        raise ValueError(
            f"Unknown tyre compound: {compound}"
        )

    data = compounds[compound]

    return Tyre(
        compound=compound,
        base_pace_delta=data["base_pace_delta"],
        degradation_per_lap=data["degradation_per_lap"],
    )