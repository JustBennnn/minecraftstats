"""All stats for bedwars.

This also includes overall bedwars stats.
"""
from .minecraftstats import get_user_stats

overall_bedwars_functions = [
    "get_games_played",
    "get_beds_lost",
    "get_coins",
    "get_deaths",
    "get_diamonds_collected",
    "get_final_deaths",
    "get_gold_collected",
    "get_iron_collected",
    "get_losses",
    "get_total_resources_collected",
    "get_void_deaths",
    "get_void_final_deaths",
    "get_entity_final_deaths",
    "get_emeralds_collected",
    "get_entity_deaths",
    "get_entity_kills",
    "get_kills",
    "get_beds_broken",
    "get_fall_damage_deaths",
    "get_current_winstreak",
    "get_entity_final_kills",
    "get_final_kills",
    "get_wins",
    "get_void_kills",
    "get_void_final_kills",
    "get_fall_damage_kills",
    "get_fall_damage_final_deaths",
    "get_fall_damage_final_kills",
    "get_explosion_deaths",
    "get_explosion_final_deaths",
    "get_explosion_final_kills"
]

__all__ = [
    "OverallBedwarsStats",
    "overall_bedwars_functions"
]

player_stats = None

class OverallBedwarsStats():
    """Overall stats for every mode in bedwars.
    
    All of the functions in here were created in the order that the API returned them,
    which is why they are in a random order.
    """
    def __init__(self):
        global player_stats

        if player_stats == None:
            player_stats = get_user_stats()["Bedwars"]

    def get_games_played(self):
        return player_stats["games_played_bedwars"]

    def get_beds_lost(self):
        return player_stats["beds_lost_bedwars"]

    def get_coins(self):
        return player_stats["coins"]

    def get_deaths(self):
        return player_stats["deaths_bedwars"]

    def get_diamonds_collected(self):
        return player_stats["diamond_resources_collected_bedwars"]

    def get_final_deaths(self):
        return player_stats["final_deaths_bedwars"]

    def get_gold_collected(self):
        return player_stats["gold_resources_collected_bedwars"]

    def get_iron_collected(self):
        return player_stats["iron_resources_collected_bedwars"]

    def get_losses(self):
        return player_stats["losses_bedwars"]

    def get_total_resources_collected(self):
        return player_stats["resources_collected_bedwars"]

    def get_void_deaths(self):
        return player_stats["void_deaths_bedwars"]

    def get_void_final_deaths(self):
        return player_stats["void_final_deaths_bedwars"]

    def get_entity_final_deaths(self): #for example killed by an iron golem or a fireball
        return player_stats["entity_attack_final_deaths_bedwars"]

    def get_emeralds_collected(self):
        return player_stats["emeral_resources_collected_bedwars"]

    def get_entity_deaths(self):
        return player_stats["entity_attack_deaths_bedwars"]

    def get_entity_kills(self):
        return player_stats["entity_attack_kills_bedwars"]

    def get_kills(self):
        return player_stats["kills_bedwars"]

    def get_beds_broken(self):
        return player_stats["beds_broken_bedwars"]

    def get_fall_damage_deaths(self):
        return player_stats["fall_deaths_bedwars"]

    def get_current_winstreak(self):
        return player_stats["winstreak"]

    def get_entity_final_kills(self):
        return player_stats["entity_attack_final_kills_bedwars"]

    def get_final_kills(self):
        return player_stats["final_kills_bedwars"]

    def get_wins(self):
        return player_stats["wins_bedwars"]

    def get_void_kills(self):
        return player_stats["void_kills_bedwars"]

    def get_void_final_kills(self):
        return player_stats["void_final_kills_bedwars"]

    def get_fall_damage_kills(self):
        return player_stats["fall_kills_bedwars"]

    def get_fall_damage_final_deaths(self):
        return player_stats["fall_final_deaths_bedwars"]

    def get_fall_damage_final_kills(self):
        return player_stats["fall_final_kills_bedwars"]

    def get_explosion_deaths(self):
        return player_stats["entity_explosion_deaths_bedwars"]

    def get_explosion_final_deaths(self):
        return player_stats["entity_explosion_final_deaths_bedwars"]

    def get_explosion_final_kills(self):
        return player_stats["entity_explosion_final_kills_bedwars"]