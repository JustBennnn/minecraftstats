"""All stats for duels.

This also includes overall duel stats.
"""
from .errors import StatError
from .minecraftstats import get_user_stats

overall_functions = [
    "get_recent_games",
    "get_games_played",
    "get_current_winstreak",
    "get_bow_shots",
    "get_bow_hits",
    "get_coins",
    "get_damage_dealt",
    "get_deaths",
    "get_health_regenerated",
    "get_losses",
    "get_melee_hits",
    "get_melee_swings",
    "get_best_winstreak",
    "get_kills",
    "get_wins",
    "get_blocks_placed",
    "get_golden_apples_eaten",
    "get_goals"
]

classic_duel_functions = [
    "get_current_winstreak",
    "get_bow_shots",
    "get_bow_hits",
    "get_damage_dealt",
    "get_deaths",
    "get_health_regenerated",
    "get_losses",
    "get_melee_hits",
    "get_melee_swings",
    "get_games_played",
    "get_best_winstreak",
    "get_kills",
    "get_wins"
]

op_duel_functions = [
    "get_current_winstreak",
    "get_damage_dealt",
    "get_deaths",
    "get_health_regenerated",
    "get_losses",
    "get_melee_hits",
    "get_melee_swings",
    "get_games_played",
    "get_best_winstreak",
    "get_kills",
    "get_wins",
]

uhc_duel_functions = [
    "get_current_winstreak",
    "get_bow_shots",
    "get_bow_hits",
    "get_damage_dealt",
    "get_deaths",
    "get_health_regenerated",
    "get_losses",
    "get_melee_hits",
    "get_melee_swings",
    "get_games_played",
    "get_best_winstreak",
    "get_kills",
    "get_wins",
    "get_blocks_placed",
    "get_golden_apples_eaten"
]

sumo_duel_functions = [
    "get_current_winstreak",
    "get_deaths",
    "get_losses",
    "get_melee_hits",
    "get_melee_swings",
    "get_games_played",
    "get_best_winstreak",
    "get_kills",
    "get_wins"
]

bridge_duel_functions = [
    "get_current_winstreak",
    "get_blocks_placed",
    "get_bow_hits",
    "get_bow_shots",
    "get_deaths",
    "get_kills",
    "get_damage_dealt",
    "get_health_regenerated",
    "get_losses",
    "get_melee_hits",
    "get_melee_swings",
    "get_games_played",
    "get_goals",
    "get_best_winstreak",
    "get_wins"
]

skywars_duel_functions = [
    "get_current_winstreak",
    "get_blocks_placed",
    "get_damage_dealt",
    "get_deaths",
    "get_health_regenerated",
    "get_losses",
    "get_melee_hits",
    "get_melee_swings",
    "get_games_played",
    "get_best_winstreak",
    "get_wins",
    "get_kills"
]

__all__ = [
    "OverallDuelStats",
    "ClassicDuelStats",
    "OPDuelStats",
    "UHCDuelStats",
    "SumoDuelStats",
    "BridgeDuelStats",
    "SkyWarsDuelStats",
    "overall_functions",
    "classic_duel_functions",
    "op_duel_functions",
    "uhc_duel_functions",
    "sumo_duel_functions",
    "bridge_duel_functions",
    "skywars_duel_functions"
]

player_stats = None

class OverallDuelStats():
    """Overall stats for every duel. All stats in here are totals from every duel mode.

    Some of the functions return data to do with hearts, which are measured in halves.
    """
    def __init__(self):
        global player_stats

        if player_stats == None:
            player_stats = get_user_stats()["Duels"]

    def get_recent_games(self):
        """Gets the 3 most recent modes played.

        The most recent mode will be returned at the start of the list, and the 3rd most recent
        at the end of the list.
        """
        recent_games = player_stats["duels_recently_played2"]
        mode1 = recent_games[0:recent_games.find("#")]
        mode2 = recent_games[recent_games.find("#")+1:recent_games.rfind("#")]
        mode3 = recent_games[recent_games.rfind("#")+1:len(recent_games)]
        return [mode1, mode2, mode3]

    def get_games_played(self):
        return player_stats["games_played_duels"]

    def get_current_winstreak(self):
        return player_stats["current_winstreak"]

    def get_bow_shots(self):
        return player_stats["bow_shots"]

    def get_bow_hits(self):
        return player_stats["bow_hits"]

    def get_coins(self):
        return player_stats["coins"]

    def get_damage_dealt(self):
        return player_stats["damage_dealt"]

    def get_deaths(self):
        return player_stats["deaths"]

    def get_health_regenerated(self):
        return player_stats["health_regenerated"]

    def get_losses(self):
        """A loss doesn't necessarily mean a death. You can loose a bridge duel for example without dying."""
        return player_stats["losses"]

    def get_melee_hits(self):
        return player_stats["melee_hits"]

    def get_melee_swings(self):
        return player_stats["melee_swings"]

    def get_best_winstreak(self):
        return player_stats["best_overall_winstreak"]

    def get_kills(self):
        return player_stats["kills"]

    def get_wins(self):
        return player_stats["wins"]

    def get_blocks_placed(self):
        return player_stats["blocks_placed"]

    def get_golden_apples_eaten(self):
        return player_stats["golden_apples_eaten"]

    def get_goals(self):
        return player_stats["goals"]

class DuelStats():
    """A base class for duel stats. Another class calls this class, and enters a mode 
    to get the stats from.
    
    The functions in here were created in the same order that the API returns the data, 
    which is why some of them are in a random order.
    Some of the functions return data to do with hearts, which are measured in halves.
    """
    def __init__(self, mode=None, allowed_functions=[]):
        global player_stats

        if player_stats == None:
            player_stats = get_user_stats()["Duels"]

        self.mode = mode
        self.allowed_functions = allowed_functions

    def get_current_winstreak(self):
        if "get_current_winstreak" in self.allowed_functions:
            return player_stats[f"current_winstreak_mode_{self.mode}"]
        else:
            raise StatError(f"Cannot get current_winstreak stat from {self.mode} mode.")

    def get_bow_shots(self):
        if "get_bow_shots" in self.allowed_functions:
            return player_stats[f"{self.mode}_bow_shots"]
        else:
            raise StatError(f"Cannot get bow_shots stat from {self.mode} mode.")

    def get_bow_hits(self):
        if "get_bow_hits" in self.allowed_functions:
            return player_stats[f"{self.mode}_bow_hits"]
        else:
            raise StatError(f"Cannot get bow_hits stat from {self.mode} mode.")
    
    def get_damage_dealt(self):
        if "get_damage_dealt" in self.allowed_functions:
            return player_stats[f"{self.mode}_damage_dealt"]
        else:
            raise StatError(f"Cannot get damage_dealt stat from {self.mode} mode.")

    def get_deaths(self):
        if "get_deaths" in self.allowed_functions:
            if self.mode == "bridge_duel":
                return player_stats[f"{self.mode}_bridge_deaths"]
            else:
                return player_stats[f"{self.mode}_deaths"]
        else:
            raise StatError(f"Cannot get  stat from {self.mode} mode.")

    def get_health_regenerated(self):
        if "get_health_regenerated" in self.allowed_functions:
            return player_stats[f"{self.mode}_health_regenerated"]
        else:
            raise StatError(f"Cannot get health_regenerated stat from {self.mode} mode.")

    def get_losses(self):
        """For some duel modes, a loss isn't necessarily from dying. For example, in a bridge duel you can loose without dying.
        Or you can loose my leaving mid duel.
        """
        if "get_losses" in self.allowed_functions:
            return player_stats[f"{self.mode}_losses"]
        else:
            raise StatError(f"Cannot get losses stat from {self.mode} mode.")

    def get_melee_hits(self):
        if "get_melee_hits" in self.allowed_functions:
            return player_stats[f"{self.mode}_melee_hits"]
        else:
            raise StatError(f"Cannot get melee_hits stat from {self.mode} mode.")

    def get_melee_swings(self):
        if "get_melee_swings" in self.allowed_functions:
            return player_stats[f"{self.mode}_melee_swings"]
        else:
            raise StatError(f"Cannot get melee_swings stat from {self.mode} mode.")

    def get_games_played(self):
        if "get_games_played" in self.allowed_functions:
            return player_stats[f"{self.mode}_rounds_played"]
        else:
            raise StatError(f"Cannot get games_played stat from {self.mode} mode.")

    def get_best_winstreak(self):
        if "get_best_winstreak" in self.allowed_functions:
            return player_stats[f"best_winstreak_mode_{self.mode}"]
        else:
            raise StatError(f"Cannot get best_winstreak stat from {self.mode} mode.")

    def get_kills(self):
        if "get_kills" in self.allowed_functions:
            if self.mode == "bridge_duel":
                return player_stats[f"{self.mode}_bridge_kills"]
            else:
                return player_stats[f"{self.mode}_kills"]
        else:
            raise StatError(f"Cannot get kills stat from {self.mode} mode.")

    def get_wins(self):
        if "get_wins" in self.allowed_functions:
            return player_stats[f"{self.mode}_wins"]
        else:
            raise StatError(f"Cannot get wins stat from {self.mode} mode.")

    def get_blocks_placed(self):
        if "get_blocks_placed" in self.allowed_functions:
            return player_stats[f"{self.mode}_blocks_placed"]
        else:
            raise StatError(f"Cannot get blocks_placed stat from {self.mode} mode.")

    def get_golden_apples_eaten(self):
        if "get_golden_apples_eaten" in self.allowed_functions:
            return player_stats[f"{self.mode}_golden_apples_eaten"]
        else:
            raise StatError(f"Cannot get golden_apples_eaten stat from {self.mode} mode.")

    def get_goals(self):
        if "get_goals" in self.allowed_functions:
            return player_stats[f"{self.mode}_goals"]
        else:
            raise StatError(f"Cannot get goals stat from {self.mode} mode.")

class ClassicDuelStats(DuelStats):
    """Stats for Classic duels. All stats in here are just related to Classic duels."""
    def __init__(self):
        self.allowed_functions = classic_duel_functions
        super().__init__(mode="classic_duel", allowed_functions=self.allowed_functions)

class OPDuelStats(DuelStats):
    """Stats for OP duels. All stats in here are just related to OP duels."""
    def __init__(self):
        self.allowed_functions = op_duel_functions
        super().__init__(mode="op_duel", allowed_functions=self.allowed_functions)

class UHCDuelStats(DuelStats):
    """Stats for UHC duels. All stats in here are just related to UHC duels, not 2v2 or 4v4."""
    def __init__(self):
        self.allowed_functions = uhc_duel_functions
        super().__init__(mode="uhc_duel", allowed_functions=self.allowed_functions)

class SumoDuelStats(DuelStats):
    """Stats for Sumo duels. All stats in here are just related to Sumo duels."""
    def __init__(self):
        self.allowed_functions = sumo_duel_functions
        super().__init__(mode="sumo_duel", allowed_functions=self.allowed_functions)

class BridgeDuelStats(DuelStats):
    """Stats for Bridge duels. All stats in here are just related to Bridge duels."""
    def __init__(self):
        self.allowed_functions = bridge_duel_functions
        super().__init__(mode="bridge_duel", allowed_functions=self.allowed_functions)

class SkyWarsDuelStats(DuelStats):
    """Stats for SkyWars duels. All stats in here are just related to SkyWars duels."""
    def __init__(self):
        self.allowed_functions = skywars_duel_functions
        super().__init__(mode="sw_duel", allowed_functions=self.allowed_functions)
