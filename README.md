# minecraftstats
Minecraftstats is an API wrapper for the Minecraft server Hypixel. The library only currently allows the user to get
duel stats.

## installation
using [pip](https://pypi.org/project/minecraftstats "")

```
pip install minecraftstats
```

using setup.py to install

```
git clone https://github.com/justbennnn/minecraftstats.git
cd minecraftstats
python setup.py install
```

## usage
The following examples show all of the current available functions in minecraftstats.

**Important**: An API key can be obtained by logging onto the Hypixel server, and typing `/api new`.

## duels
This example shows how to get stats from the duels lobby.

```python
import minecraftstats as ms

ms.set_username("your_username")
ms.set_api_key("c4797b3c-2411-4da8-b81d-5e71d47de1f5")

print(ms.overall_duel_functions) #all available functions for overall duel stats

overallStats = ms.OverallDuelStats() #create an instance of the class and call get functions from there
print("Duel stats info: ")
print("Most recent gamemode:", overallStats.get_recent_games()[0]) #can go up to 3rd most recent game mode
print("Total games played:", overallStats.get_games_played())
print("Current winstreak:", overallStats.get_current_winstreak()) #the winstreak can be from any game mode
print("Total bow shots:", overallStats.get_bow_shots())
print("Total bow hits:", overallStats.get_bow_hits())
print("Coins:", overallStats.get_coins())
print("Damage Dealt:", overallStats.get_damage_dealt()) 
print("Total deaths:", overallStats.get_deaths())
print("Total health regenerated:", overallStats.get_health_regenerated())
print("Total losses:", overallStats.get_losses())
print("Total melee hits:", overallStats.get_melee_hits()) 
print("Total melee swings:", overallStats.get_melee_swings())
print("Best winstreak:", overallStats.get_best_winstreak())
print("Total kills:", overallStats.get_kills())
print("Total wins:", overallStats.get_wins())
print("Total blocks placed:", overallStats.get_blocks_placed())
print("Total golden apples eaten:", overallStats.get_golden_apples_eaten())
print("Total goals:", overallStats.get_goals()) #goals are from bridge duels
```

> Any stats that return hearts are measured in halves.

The easiest way to retrieve stats is by creating an instance of the `OverallDuelStats` class and use the get functions 
to get the stats demonstrated in the example.

The next example shows getting stats from an individual game mode in the duels lobby.

```python
print(ms.uhc_duel_functions) #all available functions for uhc duel stats

uhcDuelStats = ms.UHCDuelStats()
print("Kills:", uhcDuelStats.get_kills())
print("Wins:", uhcDuelStats.get_wins())
```

## bedwars
This example shows how to get stats from the bedwars lobby.

```python
print(ms.overall_bedwars_functions) #all available functions for overall bedwars stats

overallStats = ms.OverallBedwarsStats()
print("Bedwars stats info: ")
print("Total games played:", overallStats.get_games_played())
print("Total beds lost:", overallStats.get_beds_lost())
print("Coins:", overallStats.get_coins())
print("Total diamonds collected:", overallStats.get_diamonds_collected())
print("Total wins:", overallStats.get_wins())
print("Total kills:", overallStats.get_kills())
```

As shown above, most of the key concepts are the same as the duels stats example.