"""All stats for bedwars.

This also includes overall bedwars stats.
"""
from pydantic import BaseModel, Field

__all__ = [
    "OverallBedwarsStats"
]

game_modes = [
    "eight_one",
    "eight_two",
    "four_four",
    "two_four",
    "four_three"
]

def filter_kwargs(_prefix, _suffix, _game_mode, **kwargs):
    """Filter the kwargs to the specific gamemode and remove any prefixes or suffixes."""
    global game_modes

    if _game_mode == "":
        kwargs = {k: v for k, v in kwargs.items() if game_modes[0] not in k 
                    and game_modes[1] not in k and game_modes[2] not in k 
                    and game_modes[3] not in k and game_modes[4] not in k}
    else:
        kwargs = {k: v for k, v in kwargs.items() if _game_mode in k}
   
    ps_kwargs = {}
    prefix_kwargs = {}
    suffix_kwargs = {}
    extra_kwargs = {}

    completed_values = []
    if _prefix != "" and _suffix != "":
        for k, v in kwargs.items():
            if k not in completed_values:

                if k.find(_prefix) == 0 and k.rfind(_suffix) != -1 and k.rfind(_suffix)+len(_suffix) == len(k):
                    ps_kwargs[k[len(_prefix):len(k)-len(_suffix)]] = v
                    completed_values.append(k)

    if _prefix != "":
        for k, v in kwargs.items():
            if k not in completed_values:
                
                if k.find(_prefix) == 0:
                    prefix_kwargs[k[len(_prefix):len(k)]] = v
                    completed_values.append(k)

    if _suffix != "":
        for k, v in kwargs.items():
            if k not in completed_values:

                if k.rfind(_suffix) != -1 and k.rfind(_suffix)+len(_suffix) == len(k):
                    suffix_kwargs[k[0:k.rfind(_suffix)]] = v
                    completed_values.append(k)

    for k, v in kwargs.items():
        if k not in completed_values:
            extra_kwargs[k] = v

    kwargs = {**ps_kwargs, **prefix_kwargs, **suffix_kwargs, **extra_kwargs}
    return kwargs

class StatsModel(BaseModel):
    """Base Model for other classes."""
    _prefix: str = ""
    _suffix: str = ""
    _game_mode: str = ""
    def __init__(self, **kwargs):
        super().__init__(**filter_kwargs(self._prefix, self._suffix, self._game_mode, **kwargs))

class OverallBedwarsStats(StatsModel):
    """Overall bedwars stats."""
    _suffix: str = "_bedwars"

    games_played: int
    beds_lost: int
    coins: int
    deaths: int
    diamonds_collected: int = Field(alias="diamond_resources_collected")
    final_deaths: int
    gold_collected: int = Field(alias="gold_resources_collected")
    iron_collected: int = Field(alias="iron_resources_collected")
    losses: int
    total_resources_collected: int = Field(alias="resources_collected")
    void_deaths: int
    void_final_deaths: int
    entity_final_deaths: int = Field(alias="entity_attack_final_deaths")
    emeralds_collected: int = Field(alias="emerald_resources_collected")
    entity_deaths: int = Field(alias="entity_attack_deaths")
    entity_kills: int = Field(alias="entity_attack_kills")
    kills: int
    beds_broken: int
    fall_damage_deaths: int = Field(alias="fall_deaths")
    current_winstreak: int = Field(alias="winstreak")
    entity_final_kills: int = Field(alias="entity_attack_final_kills")
    final_kills: int
    wins: int
    void_kills: int
    void_final_kills: int
    fall_damage_kills: int = Field(alias="fall_kills")
    fall_damage_final_deaths: int = Field(alias="fall_final_deaths")
    fall_damage_final_kills: int = Field(alias="fall_final_kills")