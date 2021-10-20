"""Stats for skywars.

This also includes overall skywars stats.
"""
from pydantic import BaseModel, Field

__all__ = []

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
    blocks_broken: int = 0
    blocks_placed: int = 0
    wins: int = 0