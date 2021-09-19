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

game_modes = [
    "classic",
    "op",
    "uhc",
    "sumo",
    "bridge",
    "sw"
]

def filter_kwargs(_prefix, _suffix, _game_mode, **kwargs):
    """Filter the kwargs to the specific gamemode and remove any prefixes or suffixes."""
    global game_modes

    if _game_mode == "":
        kwargs = {k: v for k, v in kwargs.items() if game_modes[0] not in k 
                    and game_modes[1] not in k and game_modes[2] not in k 
                    and game_modes[3] not in k and game_modes[4] not in k
                    and game_modes[5] not in k}
    else:
        kwargs = {k: v for k, v in kwargs.items() if _game_mode in k}
   
    ps_kwargs = {}
    prefix_kwargs = {}
    suffix_kwargs = {}
    extra_kwargs = {}

    completed_values = []
    if _prefix != "" and _suffix != "":
        for k, v in kwargs.items():
            if k not in completed_values:

                if k.find(_prefix) == 0 and k.rfind(_suffix) != -1 and k.rfind(_suffix)+len(_suffix) == len(k):
                    ps_kwargs[k[len(_prefix):len(k)-len(_suffix)]] = v
                    completed_values.append(k)

    if _prefix != "":
        for k, v in kwargs.items():
            if k not in completed_values:
                
                if k.find(_prefix) == 0:
                    prefix_kwargs[k[len(_prefix):len(k)]] = v
                    completed_values.append(k)

    if _suffix != "":
        for k, v in kwargs.items():
            if k not in completed_values:

                if k.rfind(_suffix) != -1 and k.rfind(_suffix)+len(_suffix) == len(k):
                    suffix_kwargs[k[0:k.rfind(_suffix)]] = v
                    completed_values.append(k)

    for k, v in kwargs.items():
        if k not in completed_values:
            extra_kwargs[k] = v

    kwargs = {**ps_kwargs, **prefix_kwargs, **suffix_kwargs, **extra_kwargs}
    return kwargs

class StatsModel(BaseModel):
    """Base Model for other classes."""
    _prefix: str = ""
    _suffix: str = ""
    _game_mode: str = ""
    def __init__(self, **kwargs):
        super().__init__(**filter_kwargs(self._prefix, self._suffix, self._game_mode, **kwargs))

class OverallDuelStats(BaseModel):
    """Overall duel stats.
    
    Any stat to do with hearts is measured in halves.
    """
    recent_games_object: str = Field(alias="duels_recently_played2")
    @property
    def recent_games(self) -> list[str]:
        return self.recent_games_object.lower().split("#")
    games_played: int = Field(alias="games_played_duels")
    current_winstreak: int
    bow_shots: int
    bow_hits: int
    coins: int
    damage_dealt: int
    deaths: int
    health_regenerated: int
    losses: int
    melee_hits: int
    melee_swings: int
    best_winstreak: int = Field(alias="best_overall_winstreak")
    kills: int
    wins: int
    blocks_placed: int
    golden_apples_eaten: int
    goals: int

class ClassicDuelStats(StatsModel):
    """Classic duel stats.
    
    Any stats to do with hearts are measured in halves.
    """
    _prefix: str = "classic_duel_"
    _suffix: str = "_mode_classic_duel"
    _game_mode: str = "classic_duel"

    current_winstreak: int
    bow_shots: int
    bow_hits: int
    damage_dealt: int
    deaths: int
    health_regenerated: int
    losses: int
    melee_hits: int
    melee_swings: int
    games_played: int = Field(alias="rounds_played")
    best_winstreak: int
    kills: int
    wins: int

class OPDuelStats(StatsModel):
    """OP duel stats.

    Any stats to do with hearts are measured in halves.
    """
    _prefix: str = "op_duel_"
    _suffix: str = "_mode_op_duel"
    _game_mode: str = "op_duel"

    current_winstreak: int
    damage_dealt: int
    deaths: int
    health_regenerated: int
    losses: int
    melee_hits: int
    melee_swings: int
    games_played: int = Field(alias="rounds_played")
    best_winstreak: int
    kills: int
    wins: int

class UHCDuelStats(StatsModel):
    """UHC duel stats.

    Any stats to do with hearts are measured in halves.
    """
    _prefix: str = "uhc_duel_"
    _suffix: str = "_mode_uhc_duel"
    _game_mode: str = "uhc_duel"

    current_winstreak: int
    bow_shots: int
    bow_hits: int
    damage_dealt: int
    deaths: int
    health_regenerated: int
    losses: int
    melee_hits: int
    melee_swings: int
    games_played: int = Field(alias="rounds_played")
    best_winstreak: int
    kills: int
    wins: int
    blocks_placed: int
    golden_apples_eaten: int

class SumoDuelStats(StatsModel):
    """Sumo duel stats."""
    _prefix: str = "sumo_duel_"
    _suffix: str = "_mode_sumo_duel"
    _game_mode: str = "sumo_duel"

    current_winstreak: int
    deaths: int
    losses: int
    melee_hits: int
    melee_swings: int
    games_played: int = Field(alias="rounds_played")
    best_winstreak: int
    kills: int
    wins: int

class BridgeDuelStats(StatsModel):
    """Bridge duel stats.

    Any stats to do with hearts are measured in halves.
    """
    _prefix: str = "bridge_duel_"
    _suffix: str = "_mode_sumo_duel"
    _game_mode: str = "sumo_duel"

    current_winstreak: int
    bow_shots: int
    bow_hits: int
    damage_dealt: int
    deaths: int = Field(alias="bridge_deaths")
    health_regenerated: int
    losses: int
    melee_hits: int
    melee_swings: int
    games_played: int = Field(alias="rounds_played")
    best_winstreak: int
    kills: int = Field(alias="bridge_kills")
    wins: int
    blocks_placed: int
    goals: int

class SkyWarsDuelStats(StatsModel):
    """Skywars duel stats.

    Any stats to do with hearts are measured in halves.
    """
    _prefix: str = "sw_duel_"
    _suffix: str = "_mode_sw_duel"
    _game_mode: str = "sw_duel"

    current_winstreak: int
    blocks_placed: int
    damage_dealt: int
    deaths: int
    health_regenerated: int
    losses: int
    melee_hits: int
    melee_swings: int
    games_played: int = Field(alias="rounds_played")
    best_winstreak: int
    wins: int
    kills: int