from src.f1_performance.session_loader import load_session
from src.f1_performance.lap_selector import select_fastest_lap  
from src.f1_performance.telemetry_loader import extract_telemetry

def main():

        session = load_session(2025, "Monza", "Q")

        drivers = ["VER", "LEC"]

        for driver in drivers:
              lap = select_fastest_lap(session, driver)
              telemetry = extract_telemetry(lap)

              print(f"\nDRIVER: {driver}")
              print(f"Lap number: {lap['LapNumber']}")
              print(f"Lap time: {lap['LapTime']}")
              print(f"Telemetry samples: {len(telemetry)}")

              print("\nFirst 5 telemetry samples:")
              print(telemetry.head())

if __name__ == "__main__":
    main()  
