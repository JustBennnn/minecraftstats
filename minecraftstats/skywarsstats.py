"""Stats for skywars.

This also includes overall skywars stats.
"""
from pydantic import BaseModel, Field, validator
from typing import List

from .utils import StatsModel

__all__ = []

game_modes = [
    "solo"
]

skywars_experience_totals = [20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000] #the experience totals for each skywars level, after a certain point the amounts just go up in 10000.

class OverallSkywarsStats(BaseModel):
    """Overall skywars stats."""
    souls: int = 0
    games_played: int = Field(0, alias="games_played_skywars")
    chests_opened: int = 0
    coins: int = 0
    deaths: int = 0
    latest_mode_object: str = Field("", alias="lastMode")
    @property
    def latest_mode(self):
        return self.latest_mode_object.lower()

    losses: int = 0
    quits: int = 0
    current_winstreak: int = Field(0, alias="win_streak")
    experience: int = Field(0, alias="skywars_experience")
    level: int = Field(0, alias="skywars_experience") #this variable will go through a validator
    blocks_broken: int = 0
    blocks_placed: int = 0
    wins: int = 0

    @validator("level", pre=False)
    def convert_experience_to_level(cls, total_experience):
        """The following code checks the skywars level by going through the experience totals list.
        Every time the loop moves onto the next value, a new value is added to the end of the list(10000 above the last value)
        in case that the level of the player is above one of the totals in the list. It also saves having to create a list 
        with tens of values, and is dynamic for player's with higher levels.
        """
        current_index = 0
        while True:

            if total_experience < skywars_experience_totals[current_index]:
                return current_index + 1

            elif total_experience == skywars_experience_totals[current_index]:
                return current_index + 2
                
            elif total_experience > skywars_experience_totals[current_index]:
                skywars_experience_totals.append(skywars_experience_totals[-1] + 10000)
                current_index = current_index + 1

class SoloSkywarsStats(StatsModel):
    """Solo skywars stats."""
    _suffix: str = "_solo"
    _game_mode: str = "solo"
    _game_modes: List[str] = game_modes
    
    chests_opened: int = 0
    deaths: int = 0
    losses: int = 0
    wins: int = 0