import json
from pathlib import Path

from simulator.models.circuit import Circuit
from simulator.models.driver import Driver
from simulator.models.car import Car
from simulator.models.tyre import Tyre
from simulator.engine.race import Race


def load_circuit(path: str) -> Circuit:
    """Load circuit information from JSON."""

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return Circuit(**data)


def format_time(seconds: float) -> str:
    """Convert seconds into HH:MM:SS.sss format."""

    hours = int(seconds // 3600)

    minutes = int((seconds % 3600) // 60)

    remaining_seconds = seconds % 60

    return f"{hours:02d}:{minutes:02d}:{remaining_seconds:06.3f}"


def main():

    circuit_path = Path(
        "data/circuits/silverstone.json"
    )

    circuit = load_circuit(circuit_path)

    driver = Driver(
        name="Test Driver",
        pace_delta=-0.15,
        consistency=0.08,
    )

    car = Car(
        team="Test Team",
        pace_delta=-0.30,
        tyre_degradation_multiplier=1.0,
    )

    tyre = Tyre(
        compound="MEDIUM",
        base_pace_delta=0.0,
        degradation_per_lap=0.045,
    )

    race = Race(
        circuit=circuit,
        driver=driver,
        car=car,
        tyre=tyre,
        starting_fuel=110.0,
    )

    result = race.run()

    print()
    print("=" * 60)
    print("        F1 RACE STRATEGY SIMULATOR V0.1")
    print("=" * 60)
    print()

    print(f"Circuit:       {result.circuit}")
    print(f"Driver:        {result.driver}")
    print(f"Team:          {result.team}")
    print(f"Race distance: {circuit.race_distance_km:.1f} km")
    print(f"Laps:          {circuit.laps}")
    print()

    print("-" * 60)
    print(
        f"{'Lap':>4} "
        f"{'Time':>10} "
        f"{'Tyre Age':>10} "
        f"{'Fuel':>10}"
    )
    print("-" * 60)

    for lap in result.laps:

        print(
            f"{lap.lap_number:>4} "
            f"{lap.lap_time:>10.3f} "
            f"{lap.tyre_age:>10} "
            f"{lap.fuel_remaining:>10.2f}"
        )

    print("-" * 60)

    print()
    print(f"Total race time:  {format_time(result.total_time)}")
    print(f"Average lap:      {result.average_lap_time:.3f}s")
    print()

    print("=" * 60)


if __name__ == "__main__":
    main()