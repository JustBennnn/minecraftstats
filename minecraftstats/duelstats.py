"""All stats for duels.

This also includes overall duel stats.
"""
from pydantic import BaseModel, Field

from .utils import filter_kwargs, StatsModel

__all__ = []

game_modes = [
    "classic",
    "op",
    "uhc",
    "sumo",
    "bridge",
    "sw"
]

class OverallDuelStats(BaseModel):
    """Overall duel stats.
    
    Any stat to do with hearts is measured in halves.
    """
    recent_games_object: str = Field("", alias="duels_recently_played2")
    @property
    def recent_games(self) -> list[str]:
        return self.recent_games_object.lower().split("#")
    games_played: int = Field(0, alias="games_played_duels")
    current_winstreak: int = 0
    bow_shots: int = 0
    bow_hits: int = 0
    coins: int = 0
    damage_dealt: int = 0
    deaths: int = 0
    health_regenerated: int = 0
    losses: int = 0
    melee_hits: int = 0
    melee_swings: int = 0
    best_winstreak: int = Field(0, alias="best_overall_winstreak")
    kills: int = 0
    wins: int = 0
    blocks_placed: int = 0
    golden_apples_eaten: int = 0
    goals: int = 0

class ClassicDuelStats(StatsModel):
    """Classic duel stats.
    
    Any stats to do with hearts are measured in halves.
    """
    _prefix: str = "classic_duel_"
    _suffix: str = "_mode_classic_duel"
    _game_mode: str = "classic_duel"
    _game_modes = game_modes

    current_winstreak: int = 0
    bow_shots: int = 0
    bow_hits: int = 0
    damage_dealt: int = 0
    deaths: int = 0
    health_regenerated: int = 0
    losses: int = 0
    melee_hits: int = 0
    melee_swings: int = 0
    games_played: int = Field(0, alias="rounds_played")
    best_winstreak: int = 0
    kills: int = 0
    wins: int = 0

class OPDuelStats(StatsModel):
    """OP duel stats.

    Any stats to do with hearts are measured in halves.
    """
    _prefix: str = "op_duel_"
    _suffix: str = "_mode_op_duel"
    _game_mode: str = "op_duel"
    _game_modes = game_modes

    current_winstreak: int = 0
    damage_dealt: int = 0
    deaths: int = 0
    health_regenerated: int = 0
    losses: int = 0
    melee_hits: int = 0
    melee_swings: int = 0
    games_played: int = Field(0, alias="rounds_played")
    best_winstreak: int = 0
    kills: int = 0
    wins: int = 0

class UHCDuelStats(StatsModel):
    """UHC duel stats.

    Any stats to do with hearts are measured in halves.
    """
    _prefix: str = "uhc_duel_"
    _suffix: str = "_mode_uhc_duel"
    _game_mode: str = "uhc_duel"
    _game_modes = game_modes

    current_winstreak: int = 0
    bow_shots: int = 0
    bow_hits: int = 0
    damage_dealt: int = 0
    deaths: int = 0
    health_regenerated: int = 0
    losses: int = 0
    melee_hits: int = 0
    melee_swings: int = 0
    games_played: int = Field(0, alias="rounds_played")
    best_winstreak: int = 0
    kills: int = 0
    wins: int = 0
    blocks_placed: int = 0
    golden_apples_eaten: int = 0

class SumoDuelStats(StatsModel):
    """Sumo duel stats."""
    _prefix: str = "sumo_duel_"
    _suffix: str = "_mode_sumo_duel"
    _game_mode: str = "sumo_duel"
    _game_modes = game_modes

    current_winstreak: int = 0
    deaths: int = 0
    losses: int = 0
    melee_hits: int = 0
    melee_swings: int = 0
    games_played: int = Field(0, alias="rounds_played")
    best_winstreak: int = 0
    kills: int = 0
    wins: int = 0

class BridgeDuelStats(StatsModel):
    """Bridge duel stats.

    Any stats to do with hearts are measured in halves.
    """
    _prefix: str = "bridge_duel_"
    _suffix: str = "_mode_bridge_duel"
    _game_mode: str = "bridge_duel"
    _game_modes = game_modes

    current_winstreak: int = 0
    bow_shots: int = 0
    bow_hits: int = 0
    damage_dealt: int = 0
    deaths: int = Field(0, alias="bridge_deaths")
    health_regenerated: int = 0
    losses: int = 0
    melee_hits: int = 0
    melee_swings: int = 0
    games_played: int = Field(0, alias="rounds_played")
    best_winstreak: int = 0
    kills: int = Field(0, alias="bridge_kills")
    wins: int = 0
    blocks_placed: int = 0
    goals: int = 0

class SkyWarsDuelStats(StatsModel):
    """Skywars duel stats.

    Any stats to do with hearts are measured in halves.
    """
    _prefix: str = "sw_duel_"
    _suffix: str = "_mode_sw_duel"
    _game_mode: str = "sw_duel"
    _game_modes = game_modes

    current_winstreak: int = 0
    blocks_placed: int = 0
    damage_dealt: int = 0
    deaths: int = 0
    health_regenerated: int = 0
    losses: int = 0
    melee_hits: int = 0
    melee_swings: int = 0
    games_played: int = Field(0, alias="rounds_played")
    best_winstreak: int = 0
    wins: int = 0
    kills: int = 0

#Doubles Stats
class UHCDoubleStats(StatsModel):
    """UHC doubles stats.
    
    Any stats to do with hearts are measured in halves.
    """
    _prefix: str = "uhc_doubles_"
    _suffix: str = "_mode_uhc_doubles"
    _game_mode: str = "uhc_doubles"
    _game_modes = game_modes

    current_winstreak: int = 0
    blocks_placed: int = 0
    bow_hits: int = 0
    bow_shots: int = 0
    damage_dealt: int = 0
    deaths: int = 0
    golden_apples_eaten: int = 0
    health_regenerated: int = 0
    losses: int = 0
    melee_hits: int = 0
    melee_swings: int = 0
    rounds_played: int = 0
    best_winstreak: int = 0
    kills: int = 0
    wins: int = 0

class BridgeDoubleStats(StatsModel):
    """Bridge doubles stats.
    
    Any stats to do with hearts are measured in halves.
    """
    _prefix: str = "bridge_doubles_"
    _suffix: str = "_mode_bridge_doubles"
    _game_mode: str = "bridge_doubles"
    _game_modes = game_modes

    current_winstreak: int = 0
    blocks_placed: int = 0
    bow_hits: int = 0
    bow_shots: int = 0
    deaths: int = Field(0, alias="bridge_deaths")
    kills: int = Field(0, alias="bridge_kills")
    damage_dealt: int = 0
    goals: int = 0
    health_regenerated: int = 0
    losses: int = 0
    melee_hits: int = 0
    melee_swings: int = 0
    games_played: int = Field(0, alias="rounds_played")
    best_winstreak: int = 0
    wins: int = 0