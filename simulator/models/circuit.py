from dataclasses import dataclass


@dataclass
class Circuit:
    name: str
    country: str
    laps: int
    lap_distance_km: float
    base_lap_time: float
    pit_lane_loss: float
    fuel_effect_per_kg: float

    @property
    def race_distance_km(self) -> float:
        """Return total race distance in kilometres."""
        return self.laps * self.lap_distance_km