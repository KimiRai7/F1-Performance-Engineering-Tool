from pathlib import Path

import fastf1

CACHE_DIR = Path("data/cache")

def load_session(year: int, grand_prix: str, session_type: str):
    """
    Load an F1 session using the FastF1 library, with caching enabled.
    
    Parameters
    ----------
    year : int
        The year of the F1 season.
    grand_prix : str
        The name of the Grand Prix (e.g., 'Monaco').
    session_type : str
        The type of session (e.g., 'FP1', 'FP2', 'FP3', 'Q', 'R').
        
    Returns
    -------
    fastf1.core.Session
        The loaded F1 session.
    """
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    fastf1.Cache.enable_cache(CACHE_DIR)

    session = fastf1.get_session(year, grand_prix, session_type)

    session.load()  # Load the session data

    return session
