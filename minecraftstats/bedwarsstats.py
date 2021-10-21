"""Stats for bedwars.

This also includes overall bedwars stats.
"""
from pydantic import BaseModel, Field
from typing import Dict, List

from .utils import StatsModel

__all__ = []

game_modes = [
    "eight_one",
    "eight_two",
    "four_four",
    "two_four",
    "four_three"
]

class OverallBedwarsStats(StatsModel):
    """Overall bedwars stats."""
    _suffix: str = "_bedwars"
    _game_modes: List[str] = game_modes

    games_played: int = 0
    items_purchased: int = 0
    permanent_items_purchased: int = 0
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

class PracticeBedwarsStats(BaseModel):
    """Practice mode stats. Doesn't inherit from the stats model because nothing needs to be filtered."""
    selected_mode: str = Field("", alias="selected")
    records_object: Dict[str, int] = Field({}, alias="records")
    bridging_object: Dict[str, int] = Field({}, alias="bridging")
    mlg_object: Dict[str, int] = Field({}, alias="mlg")
    fireball_jumping_object: Dict[str, int] = Field({}, alias="fireball_jumping")

    class Records(BaseModel):
        bridging_record_object: int = Field(0, alias="bridging_distance_30:elevation_NONE:angle_STRAIGHT:")
        @property
        def bridging_record(self) -> int:
            return self.bridging_record_object / 1000

    class BridgingStats(BaseModel):
        blocks_placed: int = 0
        failed_attempts: int = 0
        successful_attempts: int = 0

    class MLGStats(BaseModel):
        failed_attempts: int = 0
        successful_attempts: int = 0

    class FireballJumpingStats(BaseModel):
        successful_attempts: int = 0
        failed_attempts: int = 0

    @property
    def records(self) -> Records:
        return self.Records(**self.records_object)
    @property
    def bridging(self) -> BridgingStats:
        return self.BridgingStats(**self.bridging_object)
    @property
    def mlg(self) -> MLGStats:
        return self.MLGStats(**self.mlg_object)
    @property
    def fireball_jumping(self) -> FireballJumpingStats:
        return self.FireballJumpingStats(**self.fireball_jumping_object)

class CosmeticBedwarsStats(BaseModel):
    """Bedwars cosmetic stats. Doesn't inherit from the stats model because nothing needs to be filtered."""
    projectile_trail: str = Field("", alias="activeProjectileTrail")
    victory_dance: str = Field("", alias="activeVictoryDance")
    bed_destroy: str = Field("", alias="activeBedDestroy")
    kill_message: str = Field("", alias="activeKillMessages")
    glyph: str = Field("", alias="activeGlyph")