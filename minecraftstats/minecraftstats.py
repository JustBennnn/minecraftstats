"""Wrapper for the Hypixel Minecraft server mc.hypixel.net

Functions include getting duel and bedwars stats.
"""
import requests
from typing import Any, Dict

from .errors import DataError

__all__ = [
    "set_username",
    "set_api_key",
    "get_user_stats"
]

username = ""
api_key = ""

def set_username(user_name) -> None:
    """Set the username to get the stats from."""
    global username

    if isinstance(user_name, str):
        username = user_name
    else:
        raise TypeError(f"Input must be type str, not type {type(user_name).__name__}.")

def set_api_key(apikey) -> None:
    """Set the api key which is given to the user by Hypixel."""
    global api_key

    if isinstance(apikey, str):
        api_key = apikey
    else:
        raise TypeError(f"Input must be type str, not type {type(apikey).__name__}.")

def get_user_stats() -> Dict[str, Any]:
    """Get the user stats with the set username and api key."""
    if username != "" and api_key != "":
        data = requests.get(f"https://api.hypixel.net/player?key={api_key}&name={username}").json()
        if data["success"] == False:
            raise DataError(f"Unable to retrieve data. Cause: {data['cause']}.")
        else:
            return data["player"]["stats"]

    else:
        raise DataError("Username and/or API key must not be none.")    