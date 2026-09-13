from dataclasses import dataclass
from typing import List

from simulator.models.circuit import Circuit
from simulator.models.driver import Driver
from simulator.models.car import Car
from simulator.models.tyre import create_tyre
from simulator.engine.lap import calculate_lap_time


@dataclass
class CompoundComparison:
    compound: str
    lap_times: List[float]
    total_time: float
    average_lap_time: float


def simulate_compound(
    circuit: Circuit,
    driver: Driver,
    car: Car,
    compound: str,
    starting_fuel: float = 110.0,
) -> CompoundComparison:

    tyre = create_tyre(compound)

    fuel_remaining = starting_fuel
    lap_times = []

    for _ in range(circuit.laps):

        lap_time = calculate_lap_time(
            circuit=circuit,
            driver=driver,
            car=car,
            tyre=tyre,
            fuel_remaining=fuel_remaining,
        )

        lap_times.append(lap_time)

        fuel_remaining -= starting_fuel / circuit.laps

        if fuel_remaining < 0:
            fuel_remaining = 0

        tyre.advance()

    total_time = sum(lap_times)

    average_lap_time = total_time / circuit.laps

    return CompoundComparison(
        compound=compound.upper(),
        lap_times=lap_times,
        total_time=total_time,
        average_lap_time=average_lap_time,
    )


def compare_compounds(
    circuit: Circuit,
    driver: Driver,
    car: Car,
    starting_fuel: float = 110.0,
) -> List[CompoundComparison]:

    compounds = [
        "SOFT",
        "MEDIUM",
        "HARD",
    ]

    return [
        simulate_compound(
            circuit=circuit,
            driver=driver,
            car=car,
            compound=compound,
            starting_fuel=starting_fuel,
        )
        for compound in compounds
    ]