def select_fastest_lap(session, driver: str):
    """
    Select the fastest valid timed lap for a driver.
    
    Parameters
    -----------
    session : fastf1.core.Session
        Loaded: FastF1 session.
    driver : str
        Three-letter driver abbreviation.

    Returns
    -------
    fasf1.core.Lap
        Fastest valid timed lap for the driver.
    """

    driver = driver.upper()

    driver_laps = session.laps.pick_driver(driver)
    valid_laps = driver_laps.dropna(subset=["LapTime"])

    if valid_laps.empty:
        raise ValueError(f"No valid timed laps found for driver {driver}.")

    return valid_laps.pick_fastest()