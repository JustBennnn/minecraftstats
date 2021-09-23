"""Wrapper for the Hypixel Minecraft server mc.hypixel.net

Functions include getting duel and bedwars stats.
"""
import requests
from pydantic import BaseModel
from typing import Any, Dict

from .bedwarsstats import (
    OverallBedwarsStats,
    PracticeBedwarsStats
)
from .duelstats import (
    BridgeDuelStats, 
    ClassicDuelStats, 
    OPDuelStats, 
    OverallDuelStats, 
    SkyWarsDuelStats, 
    SumoDuelStats, 
    UHCDuelStats
)
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
            data = data["player"]["stats"]
            duelData = data["Duels"]
            bedwarsData = data["Bedwars"]

            stats_object = MinecraftStats(
                overall_duels=duelData,
                classic_duels=duelData,
                op_duels=duelData,
                uhc_duels=duelData,
                sumo_duels=duelData,
                bridge_duels=duelData,
                skywars_duels=duelData,
                overall_bedwars=bedwarsData,
                practice_bedwars=bedwarsData["practice"]
            )

            return stats_object
    else:
        raise DataError("Username and/or API key must not be none.")

class MinecraftStats(BaseModel):
    """Container class for all stats."""
    overall_duels: OverallDuelStats
    classic_duels: ClassicDuelStats 
    op_duels: OPDuelStats
    uhc_duels: UHCDuelStats
    sumo_duels: SumoDuelStats
    bridge_duels: BridgeDuelStats
    skywars_duels: SkyWarsDuelStats

    overall_bedwars: OverallBedwarsStats
    practice_bedwars: PracticeBedwarsStats