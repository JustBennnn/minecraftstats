# minecraftstats

[![Downloads](https://pepy.tech/badge/minecraftstats)](https://pepy.tech/project/minecraftstats)
[![Downloads/Month](https://pepy.tech/badge/minecraftstats/month)](https://pepy.tech/project/minecraftstats)
[![PyPI Version](https://img.shields.io/pypi/v/minecraftstats)](https://pypi.org/project/minecraftstats/)
[![Last Commit](https://img.shields.io/github/last-commit/justbennnn/minecraftstats)](https://github.com/JustBennnn/minecraftstats/commits/master)
[![Repository Size](https://img.shields.io/github/repo-size/justbennnn/minecraftstats)](https://github.com/JustBennnn/minecraftstats)
[![License MIT](https://img.shields.io/github/license/justbennnn/minecraftstats)](https://github.com/JustBennnn/minecraftstats/blob/master/LICENSE)
[![Discord Profile](https://img.shields.io/badge/chat-discord-blue)](https://discordapp.com/users/801460768577945681)

Minecraftstats is an API wrapper for the Minecraft server Hypixel. The library only currently allows the user to get
duel and bedwars stats.

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

**Important**: An API key can be obtained by logging onto the Hypixel server, and typing `/api new`.\
**Note**: The main framework for this project is [Pydantic](https://github.com/samuelcolvin/pydantic "").

## duels
This example shows how to get stats from the duels lobby.

```python
import minecraftstats as ms

ms.set_username("your_username")
ms.set_api_key("your_api_key")

data = ms.get_user_stats()
duelData = data["Duels"]
overallStats = ms.OverallDuelStats(**duelData)

print(list(overallStats.__fields__.keys())) #show all available stats for the OverallDuelStats class

print("Total wins:", overallStats.wins)
print("Total kills:", overallStats.kills)
print("Most recent game mode played:", overallStats.recent_games[0])
```

> Remember to use the ["Duels"] key to filter the data before you enter it.

> Any stats that return hearts are measured in halves.

The easiest way to retrieve stats is by getting the data returned by the API with `get_user_stats()`, and then passing 
that as a kwarg into the desired class. Then you can access the stats as attributes to the class.

The next example shows getting stats from an individual game mode in the duels lobby.

```python
uhcStats = ms.UHCDuelStats(**duelData)

print(list(uhcStats.__fields__.keys())) #show all available stats for the UHCDuelStats class

print("UHC wins:", uhcStats.wins)
print("Best UHC winstreak:", uhcStats.best_winstreak)
print("UHC golden apples eaten", uhcStats.golden_apples_eaten)
```

## bedwars
This example shows how to get stats from the bedwars lobby.

```python
bedwarsData = data["Bedwars"]
overallStats = ms.OverallBedwarsStats(**bedwarsData)

print(list(overallStats.__fields__.keys())) #show all available stats for the OverallBedwarsStats class

print("Total wins:", overallStats.wins)
print("Total kills:", overallStats.kills)
print("Total beds broken:", overallStats.beds_broken)
```

As shown above, most of the key concepts are the same as the duels stats example.

# CHANGELOG

## 1.0.7

* Fixed kwarg filter error.

## 1.0.6

* Created stats model and kwarg filter(for prefixes/suffixes).
* Created requirements.txt.

## 1.0.5

* Created CHANGELOG.
* Added SkyWars duel stats.

## 1.0.4

* Changed mainframe to Pydantic.
* Removed the `available_functions` variables.