"""General stats for Hypixel.
"""
import datetime
from pydantic import BaseModel, Field
from typing import Any, Dict

__all__ = []

class GeneralStats(BaseModel):
    """General Hypixel stats."""
    uuid: str = ""
    first_login_object: int = Field(0, alias="firstLogin")
    @property
    def first_login(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(self.first_login_object // 1000)

    latest_login_object: int = Field(0, alias="lastLogin")
    @property
    def latest_login(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(self.latest_login_object // 1000)

    achievement_points: int = Field(0, alias="achievementPoints")
    bedwars_level: int = 0
    wins: int = 0
    most_recent_game_mode_object: str = Field("", alias="mostRecentGameType")
    @property 
    def most_recent_game_mode(self):
        return self.most_recent_game_mode_object.lower()

    challenges_object: Dict[Any, Any] = Field({}, alias="challenges")
    @property
    def karma(self):
        return self.challenges_object["karma"]