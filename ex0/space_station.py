from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50 )
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)

def main() -> None:
    station_valid = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=20,
        power_level=85.5,
        oxygen_level=92.3,
        #last_maintenance=datetime(2024, 1, 15, 10, 0, 0),
        last_maintenance="2024-01-15T10:00:00",
        is_operational=True,
        #notes="Operational",
    )
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    print(f"ID: {station_valid.station_id}")
    print(f"Name: {station_valid.name}")
    print(f"Crew: {station_valid.crew_size} people")
    print(f"Power: {station_valid.power_level}%")
    print(f"Oxygen: {station_valid.oxygen_level}%")
    print(f"Status: {station_valid.notes}")

    print()
    print("========================================")
    print("Expected validation error:")

    try:
        station_invalid = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=0,
            power_level=85.5,
            oxygen_level=92.3,
            #last_maintenance=datetime(2024, 1, 15, 10, 0, 0),
            last_maintenance="2024-01-15T10:00:00",
            is_operational=True,
            #notes="Operational",
        )
    except ValidationError as e:
        print(e)

if __name__ == "__main__":
    main()