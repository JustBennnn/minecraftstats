"""General stats for Hypixel.
"""
import datetime
import math
from pydantic import BaseModel, Field
from typing import Any, Dict, List

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

    one_time_achievements: List[str] = Field([], alias="achievementsOneTime") 
    achievement_points: int = Field(0, alias="achievementPoints")

    most_recent_game_mode_object: str = Field("", alias="mostRecentGameType")
    @property 
    def most_recent_game_mode(self):
        return self.most_recent_game_mode_object.lower()

    achievements_object: Dict[Any, Any] = Field({}, alias="achievements")
    class AchievementStats(BaseModel):
        bedwars_level: int = 0
        bedwars_wins: int = 0
        general_wins: int = 0

    @property
    def achivements(self) -> AchievementStats:
        return self.AchievementStats(**self.achievements_object)

    experience: int = Field(0, alias="networkExp")
    @property
    def level(self):
        return math.floor((math.sqrt((2 * self.experience) + 30625) / 50) - 2.5)

    karma: int = 0
    most_recent_game_mode: str = Field("", alias="mostRecentGameType")