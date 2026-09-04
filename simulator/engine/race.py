from dataclasses import dataclass, field
from typing import List

from simulator.models.circuit import Circuit
from simulator.models.driver import Driver
from simulator.models.car import Car
from simulator.models.tyre import Tyre

from simulator.engine.lap import calculate_lap_time


@dataclass
class LapResult:
    lap_number: int
    lap_time: float
    tyre_age: int
    fuel_remaining: float


@dataclass
class RaceResult:
    circuit: str
    driver: str
    team: str
    total_time: float
    average_lap_time: float
    laps: List[LapResult] = field(default_factory=list)


class Race:
    def __init__(
        self,
        circuit: Circuit,
        driver: Driver,
        car: Car,
        tyre: Tyre,
        starting_fuel: float = 110.0,
    ):
        self.circuit = circuit
        self.driver = driver
        self.car = car
        self.tyre = tyre
        self.starting_fuel = starting_fuel

    def run(self) -> RaceResult:
        """Run the complete race."""

        fuel_remaining = self.starting_fuel
        total_time = 0.0

        lap_results = []

        for lap_number in range(1, self.circuit.laps + 1):

            lap_time = calculate_lap_time(
                circuit=self.circuit,
                driver=self.driver,
                car=self.car,
                tyre=self.tyre,
                fuel_remaining=fuel_remaining,
            )

            total_time += lap_time

            lap_results.append(
                LapResult(
                    lap_number=lap_number,
                    lap_time=lap_time,
                    tyre_age=self.tyre.age,
                    fuel_remaining=fuel_remaining,
                )
            )

            # Fuel consumption.
            fuel_remaining -= self._fuel_consumption()

            if fuel_remaining < 0:
                fuel_remaining = 0

            # Age tyres after completing the lap.
            self.tyre.advance()

        average_lap_time = total_time / self.circuit.laps

        return RaceResult(
            circuit=self.circuit.name,
            driver=self.driver.name,
            team=self.car.team,
            total_time=total_time,
            average_lap_time=average_lap_time,
            laps=lap_results,
        )

    def _fuel_consumption(self) -> float:
        """Return fuel consumed per lap."""

        return self.starting_fuel / self.circuit.laps