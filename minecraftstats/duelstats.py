"""All stats for duels.

This also includes overall duel stats.
"""
from pydantic import BaseModel, Field

__all__ = [
    "OverallDuelStats",
    "ClassicDuelStats",
    "OPDuelStats",
    "UHCDuelStats",
    "SumoDuelStats",
    "BridgeDuelStats",
    "SkyWarsDuelStats"
]

class OverallDuelStats(BaseModel):
    """Overall duel stats.
    
    Any stat to do with hearts is measured in halves.
    """
    recent_games_object: str = Field(alias="duels_recently_played2")
    @property
    def recent_games(self) -> list[str]:
        return self.recent_games_object.lower().split("#")
    games_played: int = Field(alias="games_played_duels")
    current_winstreak: int = Field(alias="current_winstreak")
    bow_shots: int = Field(alias="bow_shots")
    bow_hits: int = Field(alias="bow_hits")
    coins: int = Field(alias="coins")
    damage_dealt: int = Field(alias="damage_dealt") 
    deaths: int = Field(alias="deaths")
    health_regenerated: int = Field(alias="health_regenerated")
    losses: int = Field(alias="losses")
    melee_hits: int = Field(alias="melee_hits")
    melee_swings: int = Field(alias="melee_swings")
    best_winstreak: int = Field(alias="best_overall_winstreak")
    kills: int = Field(alias="kills")
    wins: int = Field(alias="wins")
    blocks_placed: int = Field(alias="blocks_placed")
    golden_apples_eaten: int = Field(alias="golden_apples_eaten")
    goals: int = Field(alias="goals")

class ClassicDuelStats(BaseModel):
    """Classic duel stats.
    
    Any stats to do with hearts are measured in halves.
    """
    current_winstreak: int = Field(alias="current_winstreak_mode_classic_duel")
    bow_shots: int = Field(alias="classic_duel_bow_shots")
    bow_hits: int = Field(alias="classic_duel_bow_hits")
    damage_dealt: int = Field(alias="classic_duel_damage_dealt")
    deaths: int = Field(alias="classic_duel_deaths")
    health_regenerated: int = Field(alias="classic_duel_health_regenerated")
    losses: int = Field(alias="classic_duel_losses")
    melee_hits: int = Field(alias="classic_duel_melee_hits")
    melee_swings: int = Field(alias="classic_duel_melee_swings")
    games_played: int = Field(alias="classic_duel_rounds_played")
    best_winstreak: int = Field(alias="best_winstreak_mode_classic_duel")
    kills: int = Field(alias="classic_duel_kills")
    wins: int = Field(alias="classic_duel_wins")

class OPDuelStats(BaseModel):
    """OP duel stats.

    Any stats to do with hearts are measured in halves.
    """
    current_winstreak: int = Field(alias="current_winstreak_mode_op_duel")
    damage_dealt: int = Field(alias="op_duel_damage_dealt")
    deaths: int = Field(alias="op_duel_deaths")
    health_regenerated: int = Field(alias="op_duel_health_regenerated")
    losses: int = Field(alias="op_duel_losses")
    melee_hits: int = Field(alias="op_duel_melee_hits")
    melee_swings: int = Field(alias="op_duel_melee_swings")
    games_played: int = Field(alias="op_duel_rounds_played")
    best_winstreak: int = Field(alias="best_winstreak_mode_op_duel")
    kills: int = Field(alias="op_duel_kills")
    wins: int = Field(alias="op_duel_wins")

class UHCDuelStats(BaseModel):
    """UHC duel stats.

    Any stats to do with hearts are measured in halves.
    """
    current_winstreak: int = Field(alias="current_winstreak_mode_uhc_duel")
    bow_shots: int = Field(alias="uhc_duel_bow_shots")
    bow_hits: int = Field(alias="uhc_duel_bow_hits")
    damage_dealt: int = Field(alias="uhc_duel_damage_dealt")
    deaths: int = Field(alias="uhc_duel_deaths")
    health_regenerated: int = Field(alias="uhc_duel_health_regenerated")
    losses: int = Field(alias="uhc_duel_losses")
    melee_hits: int = Field(alias="uhc_duel_melee_hits")
    melee_swings: int = Field(alias="uhc_duel_melee_swings")
    games_played: int = Field(alias="uhc_duel_rounds_played")
    best_winstreak: int = Field(alias="best_winstreak_mode_uhc_duel")
    kills: int = Field(alias="uhc_duel_kills")
    wins: int = Field(alias="uhc_duel_wins")
    blocks_placed: int = Field(alias="uhc_duel_blocks_placed")
    golden_apples_eaten: int = Field(alias="uhc_duel_golden_apples_eaten")

class SumoDuelStats(BaseModel):
    """Sumo duel stats."""
    current_winstreak: int = Field(alias="current_winstreak_mode_sumo_duel")
    deaths: int = Field(alias="sumo_duel_deaths")
    losses: int = Field(alias="sumo_duel_losses")
    melee_hits: int = Field(alias="sumo_duel_melee_hits")
    melee_swings: int = Field(alias="sumo_duel_melee_swings")
    games_played: int = Field(alias="sumo_duel_rounds_played")
    best_winstreak: int = Field(alias="best_winstreak_mode_sumo_duel")
    kills: int = Field(alias="sumo_duel_kills")
    wins: int = Field(alias="sumo_duel_wins")

class BridgeDuelStats(BaseModel):
    """Bridge duel stats.

    Any stats to do with hearts are measured in halves.
    """
    current_winstreak: int = Field(alias="current_winstreak_mode_bridge_duel")
    bow_shots: int = Field(alias="bridge_duel_bow_shots")
    bow_hits: int = Field(alias="bridge_duel_bow_hits")
    damage_dealt: int = Field(alias="bridge_duel_damage_dealt")
    deaths: int = Field(alias="bridge_duel_bridge_deaths")
    health_regenerated: int = Field(alias="bridge_duel_health_regenerated")
    losses: int = Field(alias="bridge_duel_losses")
    melee_hits: int = Field(alias="bridge_duel_melee_hits")
    melee_swings: int = Field(alias="bridge_duel_melee_swings")
    games_played: int = Field(alias="bridge_duel_rounds_played")
    best_winstreak: int = Field(alias="best_winstreak_mode_bridge_duel")
    kills: int = Field(alias="bridge_duel_bridge_kills")
    wins: int = Field(alias="bridge_duel_wins")
    blocks_placed: int = Field(alias="bridge_duel_blocks_placed")
    goals: int = Field(alias="bridge_duel_goals")

class SkyWarsDuelStats(BaseModel):
    """Skywars duel stats.

    Any stats to do with hearts are measured in halves.
    """
    current_winstreak: int = Field(alias="current_winstreak_mode_sw_duel")
    blocks_placed: int = Field(alias="sw_duel_blocks_placed")
    damage_dealt: int = Field(alias="sw_duel_damage_dealt")
    deaths: int = Field(alias="sw_duel_deaths")
    health_regenerated: int = Field(alias="sw_duel_health_regenerated")
    losses: int = Field(alias="sw_duel_losses")
    melee_hits: int = Field(alias="sw_duel_melee_hits")
    melee_swings: int = Field(alias="sw_duel_melee_swings")
    games_played: int = Field(alias="sw_duel_rounds_played")
    best_winstreak: int = Field(alias="best_winstreak_mode_sw_duel")
    wins: int = Field(alias="sw_duel_wins")
    kills: int = Field(alias="sw_duel_kills")