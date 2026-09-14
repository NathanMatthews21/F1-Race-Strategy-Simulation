from dataclasses import dataclass

@dataclass
class Tyre:
    compound: str
    base_pace_delta: float

    # Base degradation rate in seconds per lap.
    degradation_per_lap: float

    # Controls how quickly degradation accelerates with tyre age.
    degradation_exponent: float = 1.0

    age: int = 0

    def lap_degradation(self, car_multiplier: float = 1.0) -> float:
        """
        Calculate the time penalty caused by tyre age.

        Age 0 = no degradation penalty.

        degradation_exponent:
            1.0 = linear degradation
            >1.0 = degradation accelerates with age
            <1.0 = degradation increases more slowly with age
        """

        if self.age <= 0:
            return 0.0

        degradation = (
            self.degradation_per_lap
            * (self.age ** self.degradation_exponent)
            * car_multiplier
        )

        return degradation

    def advance(self) -> None:
        """Age the tyre by one lap."""

        self.age += 1

    def clone(self) -> "Tyre":
        """
        Create a fresh set of the same compound.
        """

        return Tyre(
            compound=self.compound,
            base_pace_delta=self.base_pace_delta,
            degradation_per_lap=self.degradation_per_lap,
            degradation_exponent=self.degradation_exponent,
        )


def create_tyre(compound: str) -> Tyre:
    """
    Create a fresh tyre using the default V0.2.3
    compound characteristics.
    """

    compounds = {
        "SOFT": {
            "base_pace_delta": -0.8,
            "degradation_per_lap": 0.075,
            "degradation_exponent": 1.10,
        },
        "MEDIUM": {
            "base_pace_delta": -0.4,
            "degradation_per_lap": 0.045,
            "degradation_exponent": 1.05,
        },
        "HARD": {
            "base_pace_delta": 0.0,
            "degradation_per_lap": 0.030,
            "degradation_exponent": 1.02,
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
        degradation_exponent=data["degradation_exponent"],
    )