"""All stats for bedwars.

This also includes overall bedwars stats.
"""
from pydantic import BaseModel, Field

__all__ = [
    "OverallBedwarsStats"
]

class OverallBedwarsStats(BaseModel):
    """Overall bedwars stats."""
    games_played: int = Field(alias="games_played_bedwars")
    beds_lost: int = Field(alias="beds_lost_bedwars")
    coins: int = Field(alias="coins")
    deaths: int = Field(alias="deaths_bedwars")
    diamonds_collected: int = Field(alias="diamond_resources_collected_bedwars")
    final_deaths: int = Field(alias="final_deaths_bedwars")
    gold_collected: int = Field(alias="gold_resources_collected_bedwars")
    iron_collected: int = Field(alias="iron_resources_collected_bedwars")
    losses: int = Field(alias="losses_bedwars")
    total_resources_collected: int = Field(alias="resources_collected_bedwars")
    void_deaths: int = Field(alias="void_deaths_bedwars")
    void_final_deaths: int = Field(alias="void_final_deaths_bedwars")
    entity_final_deaths: int = Field(alias="entity_attack_final_deaths_bedwars")
    emeralds_collected: int = Field(alias="emerald_resources_collected_bedwars")
    entity_deaths: int = Field(alias="entity_attack_deaths_bedwars")
    entity_kills: int = Field(alias="entity_attack_kills_bedwars")
    kills: int = Field(alias="kills_bedwars")
    beds_broken: int = Field(alias="beds_broken_bedwars")
    fall_damage_deaths: int = Field(alias="fall_deaths_bedwars")
    current_winstreak: int = Field(alias="winstreak")
    entity_final_kills: int = Field(alias="entity_attack_final_kills_bedwars")
    final_kills: int = Field(alias="final_kills_bedwars")
    wins: int = Field(alias="wins_bedwars")
    void_kills: int = Field(alias="void_kills_bedwars")
    void_final_kills: int = Field(alias="void_final_kills_bedwars")
    fall_damage_kills: int = Field(alias="fall_kills_bedwars")
    fall_damage_final_deaths: int = Field(alias="fall_final_deaths_bedwars")
    fall_damage_final_kills: int = Field(alias="fall_final_kills_bedwars")