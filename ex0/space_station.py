from pydantic import BaseModel, Field, ValidationError  # type: ignore
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)
    print("Valid station created:")
    station = SpaceStation(
        station_id="SS-001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=90.0,
        last_maintenance=datetime(2024, 5, 1),
        is_operational=True,
        notes="All systems nominal."
    )
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew Size: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    status = "Operational" if station.is_operational else "Non-operational"
    print(f"Status: {status}\n")
    print("=" * 40)
    try:
        SpaceStation(
            station_id="ISS002",
            name="Test",
            crew_size=99,
            power_level=50.0,
            oxygen_level=50.0,
            last_maintenance=datetime(2024, 5, 1),
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
