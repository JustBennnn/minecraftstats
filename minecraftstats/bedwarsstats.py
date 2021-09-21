"""All stats for bedwars.

This also includes overall bedwars stats.
"""
from pydantic import BaseModel, Field

from .utils import filter_kwargs

__all__ = []

_game_modes = [
    "eight_one",
    "eight_two",
    "four_four",
    "two_four",
    "four_three"
]

class StatsModel(BaseModel):
    """Base Model for other classes."""
    _prefix: str = ""
    _suffix: str = ""
    _game_mode: str = ""
    def __init__(self, **kwargs):
        super().__init__(**filter_kwargs(self._prefix, self._suffix, _game_modes, self._game_mode, **kwargs))

class OverallBedwarsStats(StatsModel):
    """Overall bedwars stats."""
    _suffix: str = "_bedwars"

    games_played: int = 0
    beds_lost: int = 0
    coins: int = 0
    deaths: int = 0
    diamonds_collected: int = Field(0, alias="diamond_resources_collected")
    final_deaths: int = 0
    gold_collected: int = Field(0, alias="gold_resources_collected")
    iron_collected: int = Field(0, alias="iron_resources_collected")
    losses: int = 0
    total_resources_collected: int = Field(0, alias="resources_collected")
    void_deaths: int = 0
    void_final_deaths: int = 0
    entity_final_deaths: int = Field(0, alias="entity_attack_final_deaths")
    emeralds_collected: int = Field(0, alias="emerald_resources_collected")
    entity_deaths: int = Field(0, alias="entity_attack_deaths")
    entity_kills: int = Field(0, alias="entity_attack_kills")
    kills: int = 0
    beds_broken: int = 0
    fall_damage_deaths: int = Field(0, alias="fall_deaths")
    current_winstreak: int = Field(0, alias="winstreak")
    entity_final_kills: int = Field(0, alias="entity_attack_final_kills")
    final_kills: int = 0
    wins: int = 0
    void_kills: int = 0
    void_final_kills: int = 0
    fall_damage_kills: int = Field(0, alias="fall_kills")
    fall_damage_final_deaths: int = Field(0, alias="fall_final_deaths")
    fall_damage_final_kills: int = Field(0, alias="fall_final_kills")