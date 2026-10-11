REQUIRED_CHANNELS = [
    "Time",
    "Distance",
    "Speed",
    "Throttle",
    "Brake",
    "nGear",
    "RPM",
    "DRS"    
]

def extract_telemetry(lap):
    """
    Extract lap car telemetry with distance.
    """

    telemetry = lap.get_car_data().add_distance()

    if telemetry.empty:
        raise ValueError(f"No telemetry data found for lap {lap['LapNumber']}.")

    missing = [
        channel
        for channel in REQUIRED_CHANNELS
        if channel not in telemetry.columns
    ]

    if missing:
        raise ValueError(f"Missing required telemetry channels: {', '.join(missing)}")

    return telemetry[REQUIRED_CHANNELS].copy()