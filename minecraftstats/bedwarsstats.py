"""Stats for bedwars.

This also includes overall bedwars stats.
"""
from pydantic import BaseModel, Field, root_validator
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

class BedwarsStatsModel(StatsModel):
    """Base class for some of the bedwars game modes, since a lot of the stats repeat.
    The stats to do with hearts are measured in halves, and the ones to do with fire
    damage are fire tick damage.
    """
    _prefix: str = ""
    _suffix: str = ""
    _game_mode: str = ""
    _game_modes: List[str] = game_modes

    current_winstreak: int = Field(0, alias="winstreak")
    beds_lost: int = 0
    deaths: int = 0
    final_deaths: int = 0
    games_played: int = 0
    gold_collected: int = Field(0, alias="gold_resources_collected")
    iron_collected: int = Field(0, alias="iron_resources_collected")
    items_purchased: int = 0
    losses: int = 0
    total_resources_collected: int = Field(0, alias="resources_collected")
    void_deaths: int = 0
    entity_final_deaths: int = Field(0, alias="entity_attack_final_deaths")
    permanent_items_purchased: int = 0
    entity_deaths: int = Field(0, alias="entity_attack_deaths")
    entity_kills: int = Field(0, alias="entity_attack_kills")
    kills: int = 0
    entity_final_kills: int = Field(0, alias="entity_attack_final_kills")
    final_kills: int = 0
    void_kills: int = 0
    wins: int = 0

class OverallBedwarsStats(BedwarsStatsModel):
    """Overall bedwars stats."""
    _suffix: str = "_bedwars"

    coins: int = 0
    projectile_kills: int = 0
    fire_damage_deaths: int = Field(0, alias="fire_tick_deaths")
    projectile_deaths: int = 0
    explosion_kills: int = Field(0, alias="entity_explosion_kills")
    explosion_final_kills: int = Field(0, alias="entity_explosion_final_kills")
    suffocation_final_deaths: int = 0
    fire_damage_final_kills: int = Field(0, alias="fire_tick_final_kills")
    emeralds_collected: int = Field(0, alias="emerald_resources_collected")
    diamonds_collected: int = Field(0, alias="diamond_resources_collected")
    void_final_deaths: int = 0
    beds_broken: int = 0
    fall_damage_deaths: int = Field(0, alias="fall_deaths")
    void_final_kills: int = 0
    fall_damage_kills: int = Field(0, alias="fall_kills")
    fire_damage_kills: int = Field(0, alias="fire_tick_kills")
    explosion_deaths: int = Field(0, alias="entity_explosion_deaths")
    fall_damage_final_kills: int = Field(0, alias="fall_final_kills")
    fall_damage_final_deaths: int = Field(0, alias="fall_final_deaths")
    fire_damage_final_deaths: int = Field(0, alias="fire_final_deaths")
    explosion_final_deaths: int = Field(0, alias="entity_explosion_final_deaths")

class SoloBedwarsStats(BedwarsStatsModel):
    """Solo bedwars stats."""
    _prefix: str = "eight_one_"
    _suffix: str = "_bedwars"
    _game_mode: str = "eight_one"

    explosion_final_kills: int = Field(0, alias="entity_explosion_final_kills")
    suffocation_final_deaths: int = 0
    emeralds_collected: int = Field(0, alias="emerald_resources_collected")
    diamonds_collected: int = Field(0, alias="diamond_resources_collected")
    void_final_deaths: int = 0
    beds_broken: int = 0
    fall_damage_deaths: int = Field(0, alias="fall_deaths")
    void_final_kills: int = 0
    fall_damage_kills: int = Field(0, alias="fall_kills")
    fire_damage_kills: int = Field(0, alias="fire_tick_kills")
    explosion_deaths: int = Field(0, alias="entity_explosion_deaths")
    fall_damage_final_kills: int = Field(0, alias="fall_final_kills")
    fall_damage_final_deaths: int = Field(0, alias="fall_final_deaths")
    fire_damage_final_deaths: int = Field(0, alias="fire_final_deaths")
    explosion_final_deaths: int = Field(0, alias="entity_explosion_final_deaths")

class DuoBedwarsStats(BedwarsStatsModel):
    """Duo bedwars stats."""
    _prefix: str = "eight_two_"
    _suffix: str = "_bedwars"
    _game_mode: str = "eight_two"

    projectile_kills: int = 0
    explosion_kills: int = Field(0, alias="entity_explosion_kills")
    fire_damage_final_kills: int = Field(0, alias="fire_tick_final_kills")
    fire_damage_deaths: int = Field(0, alias="fire_deaths")
    emeralds_collected: int = Field(0, alias="emerald_resources_collected")
    diamonds_collected: int = Field(0, alias="diamond_resources_collected")
    void_final_deaths: int = 0
    beds_broken: int = 0
    fall_damage_deaths: int = Field(0, alias="fall_deaths")
    void_final_kills: int = 0
    fall_damage_kills: int = Field(0, alias="fall_kills")
    fire_damage_kills: int = Field(0, alias="fire_tick_kills")
    explosion_deaths: int = Field(0, alias="entity_explosion_deaths")
    fall_damage_final_kills: int = Field(0, alias="fall_final_kills")
    fall_damage_final_deaths: int = Field(0, alias="fall_final_deaths")
    fire_damage_final_deaths: int = Field(0, alias="fire_final_deaths")
    explosion_final_deaths: int = Field(0, alias="entity_explosion_final_deaths")

class SquadBedwarsStats(BedwarsStatsModel):
    """Squad bedwars stats."""
    _prefix: str = "four_four_"
    _suffix: str = "_bedwars"
    _game_mode: str = "four_four"

    fire_damage_deaths: int = Field(0, alias="fire_tick_deaths")
    projectile_deaths: int = 0
    explosion_kills: int = Field(0, alias="entity_explosion_kills")
    emeralds_collected: int = Field(0, alias="emerald_resources_collected")
    diamonds_collected: int = Field(0, alias="diamond_resources_collected")
    void_final_deaths: int = 0
    beds_broken: int = 0
    fall_damage_deaths: int = Field(0, alias="fall_deaths")
    void_final_kills: int = 0
    fall_damage_kills: int = Field(0, alias="fall_kills")
    fire_damage_kills: int = Field(0, alias="fire_tick_kills")
    fall_damage_final_kills: int = Field(0, alias="fall_final_kills")
    fall_damage_final_deaths: int = Field(0, alias="fall_final_deaths")
    fire_damage_final_deaths: int = Field(0, alias="fire_final_deaths")
    explosion_final_deaths: int = Field(0, alias="entity_explosion_final_deaths")

class FourVersusFourBedwarsStats(BedwarsStatsModel):
    """Four versus four bedwars stats."""
    _prefix: str = "two_four_"
    _suffix: str = "_bedwars"
    _game_mode: str = "two_four"

    emeralds_collected: int = Field(0, alias="emerald_resources_collected")
    fall_damage_deaths: int = Field(0, alias="fall_deaths")
    fall_damage_kills: int = Field(0, alias="fall_kills")
    fire_damage_kills: int = Field(0, alias="fire_tick_kills")

class TrioBedwarsStats(BedwarsStatsModel):
    """Trio bedwars stats."""
    _prefix: str = "four_three_"
    _suffix: str = "_bedwars"
    _game_mode: str = "four_three"

    diamonds_collected: int = Field(0, alias="diamond_resources_collected")
    void_final_deaths: int = 0
    beds_broken: int = 0
    void_final_kills: int = 0
    explosion_final_deaths: int = Field(0, alias="entity_explosion_final_deaths")

class PracticeBedwarsStats(BaseModel):
    """Practice mode stats. Doesn't inherit from the stats model because nothing needs to be filtered."""
    selected_mode: str = Field("", alias="selected")
    records_object: Dict[str, int] = Field({}, alias="records")
    bridging_object: Dict[str, int] = Field({}, alias="bridging")
    mlg_object: Dict[str, int] = Field({}, alias="mlg")
    fireball_jumping_object: Dict[str, int] = Field({}, alias="fireball_jumping")

    class Records(BaseModel):
        bridging_distance_30__elevation_none__angle_straight: int = Field(0, alias="bridging_distance_30:elevation_NONE:angle_STRAIGHT:")
        bridging_distance_50__elevation_none__angle_straight: int = Field(0, alias="bridging_distance_50:elevation_NONE:angle_STRAIGHT:")
        bridging_distance_100__elevation_none__angle_straight: int = Field(0, alias="bridging_distance_100:elevation_NONE:angle_STRAIGHT:")

        bridging_distance_30__elevation_slight__angle_straight: int = Field(0, alias="bridging_distance_30:elevation_SLIGHT:angle_STRAIGHT:")
        bridging_distance_50__elevation_slight__angle_straight: int = Field(0, alias="bridging_distance_50:elevation_SLIGHT:angle_STRAIGHT:")
        bridging_distance_100__elevation_slight__angle_straight: int = Field(0, alias="bridging_distance_100:elevation_SLIGHT:angle_STRAIGHT:")

        bridging_distance_30__elevation_staircase__angle_straight: int = Field(0, alias="bridging_distance_30:elevation_STAIRCASE:angle_STRAIGHT:")
        bridging_distance_50__elevation_staircase__angle_straight: int = Field(0, alias="bridging_distance_50:elevation_STAIRCASE:angle_STRAIGHT:")
        bridging_distance_100__elevation_staircase__angle_straight: int = Field(0, alias="bridging_distance_100:elevation_STAIRCASE:angle_STRAIGHT:")


        bridging_distance_30__elevation_none__angle_diagonal: int = Field(0, alias="bridging_distance_30:elevation_NONE:angle_DIAGONAL:")
        bridging_distance_50__elevation_none__angle_diagonal: int = Field(0, alias="bridging_distance_50:elevation_NONE:angle_DIAGONAL:")
        bridging_distance_100__elevation_none__angle_diagonal: int = Field(0, alias="bridging_distance_100:elevation_NONE:angle_DIAGONAL:")

        bridging_distance_30__elevation_slight__angle_diagonal: int = Field(0, alias="bridging_distance_30:elevation_SLIGHT:angle_DIAGONAL:")
        bridging_distance_50__elevation_slight__angle_diagonal: int = Field(0, alias="bridging_distance_50:elevation_SLIGHT:angle_DIAGONAL:")
        bridging_distance_100__elevation_slight__angle_diagonal: int = Field(0, alias="bridging_distance_100:elevation_SLIGHT:angle_DIAGONAL:")

        bridging_distance_30__elevation_staircase__angle_diagonal: int = Field(0, alias="bridging_distance_30:elevation_STAIRCASE:angle_DIAGONAL:")
        bridging_distance_50__elevation_staircase__angle_diagonal: int = Field(0, alias="bridging_distance_50:elevation_STAIRCASE:angle_DIAGONAL:")
        bridging_distance_100__elevation_staircase__angle_diagonal: int = Field(0, alias="bridging_distance_100:elevation_STAIRCASE:angle_DIAGONAL:")

        @root_validator(pre=False)
        def divide_record_times(cls, dictionary):
            new_dictionary = {}
            for k, v in dictionary.items():
                new_dictionary[k] = v / 1000
            
            return new_dictionary

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
    most_recent_chest_loot: List[str] = Field([], alias="chest_history_new")
    projectile_trail: str = Field("", alias="activeProjectileTrail")
    victory_dance: str = Field("", alias="activeVictoryDance")
    bed_destroy: str = Field("", alias="activeBedDestroy")
    kill_message: str = Field("", alias="activeKillMessages")
    glyph: str = Field("", alias="activeGlyph")