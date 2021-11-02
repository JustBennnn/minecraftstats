"""Wrapper for the Hypixel Minecraft server mc.hypixel.net

Functions include getting duel and bedwars stats.
"""
from __future__ import annotations

import requests
from mojang import MojangAPI
from pydantic import BaseModel

from .bedwarsstats import (
    CosmeticBedwarsStats,
    DuoBedwarsStats,
    FourVersusFourBedwarsStats,
    OverallBedwarsStats,
    PracticeBedwarsStats,
    SoloBedwarsStats,
    SquadBedwarsStats,
    TrioBedwarsStats
)
from .duelstats import (
    BowDuelStats,
    BridgeDoubleStats,
    BridgeDuelStats, 
    ClassicDuelStats,
    ComboDuelStats,
    OPDoubleStats,
    OPDuelStats, 
    OverallDuelStats, 
    SkyWarsDuelStats, 
    SumoDuelStats,
    UHCDoubleStats,
    UHCDuelStats,
    UHCMeetupStats
)
from .generalstats import (
    GeneralStats
)
from .skywarsstats import (
    OverallSkywarsStats,
    SoloSkywarsStats
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

def get_user_stats() -> MinecraftStats:
    """Get the user stats with the set username and api key."""
    if username != "" and api_key != "":
        uuid = MojangAPI.get_uuid(username)
        data = requests.get(f"https://api.hypixel.net/player?key={api_key}&uuid={uuid}").json()
        if data["success"] == False:
            raise DataError(f"Unable to retrieve data. Cause: {data['cause']}.")

        if data["success"] == True and data["player"] == "null":
            raise DataError(f"Player data is null.")

        playerData = data["player"]
        statsData = playerData["stats"]
        duelData = statsData["Duels"]
        bedwarsData = statsData["Bedwars"]
        bedwarsPracticeData = bedwarsData.get("practice", {})
        skywarsData = statsData["SkyWars"]

        stats_object = MinecraftStats(
            general=playerData,

            overall_duels=duelData,
            classic_duels=duelData,
            op_duels=duelData,
            uhc_duels=duelData,
            sumo_duels=duelData,
            bridge_duels=duelData,
            skywars_duels=duelData,
            uhc_double=duelData,
            bridge_double=duelData,
            op_double=duelData,
            uhc_meetup=duelData,
            bow_duel=duelData,
            combo_duel=duelData,

            overall_bedwars=bedwarsData,
            practice_bedwars=bedwarsPracticeData,
            cosmetics_bedwars=bedwarsData,
            solo_bedwars=bedwarsData,
            duo_bedwars=bedwarsData,
            trio_bedwars=bedwarsData,
            squad_bedwars=bedwarsData,
            fourvfour_bedwars=bedwarsData,
            
            overall_skywars=skywarsData,
            solo_skywars=skywarsData
        )

        return stats_object
        
    else:
        raise DataError("Username and/or API key must not be none.")

class MinecraftStats(BaseModel):
    """Container class for all stats."""
    general: GeneralStats

    overall_duels: OverallDuelStats
    classic_duels: ClassicDuelStats 
    op_duels: OPDuelStats
    uhc_duels: UHCDuelStats
    sumo_duels: SumoDuelStats
    bridge_duels: BridgeDuelStats
    skywars_duels: SkyWarsDuelStats
    uhc_double: UHCDoubleStats
    bridge_double: BridgeDoubleStats
    op_double: OPDoubleStats
    uhc_meetup: UHCMeetupStats
    bow_duel: BowDuelStats
    combo_duel: ComboDuelStats

    overall_bedwars: OverallBedwarsStats
    practice_bedwars: PracticeBedwarsStats
    cosmetics_bedwars: CosmeticBedwarsStats
    solo_bedwars: SoloBedwarsStats
    duo_bedwars: DuoBedwarsStats
    trio_bedwars: TrioBedwarsStats
    squad_bedwars: SquadBedwarsStats
    fourvfour_bedwars: FourVersusFourBedwarsStats

    overall_skywars: OverallSkywarsStats
    solo_skywars: SoloSkywarsStats