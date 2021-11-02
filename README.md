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

**Important**: An API key can be obtained by logging onto the Hypixel server, and typing `/api new`.\
**Note**: The main framework for this project is [Pydantic](https://github.com/samuelcolvin/pydantic "").\
**Side Note**: Any stats that return hearts are measured in halves.

## general
This example shows how to access general data from the Hypixel lobby.

```python
import minecraftstats as ms

ms.set_username("username") #the username for the account that you want to get the stats from
ms.set_api_key("your_api_key")

stats = ms.get_user_stats()

print(list(stats.general.__fields__.keys())) #show all available attributes for general stats

first_login = stats.general.first_login #returns a datetime object
print("First login (day/month/year):", str(first_login.day) + "/" + str(first_login.month) + "/" + str(first_login.year))
print("Achievements:", stats.general.achievement_points)
print("Hypixel level:", stats.general.level)
```

The next set of examples will show how to get stats from different game modes.

## duels

```python
import minecraftstats as ms

ms.set_username("username") #the username for the account that you want to get the stats from
ms.set_api_key("your_api_key")

stats = ms.get_user_stats()

print(list(stats.overall_duels.__fields__.keys())) #show all available functions for overall_duels

print("Total wins:", stats.overall_duels.wins)
print("Total kills:", stats.overall_duels.kills)
print("Most recent game mode played:", stats.overall_duels.recent_games[0])
```

The best way to retrieve stats is by creating a variable which uses `ms.get_user_stats()` to get the Hypixel 
user's data, and then accessing different stats as attributes to the variable.

The next examples show how those attributes can be accessed.

```python
print(list(stats.uhc_duels.__fields__.keys())) #show all available stats for uhc_duels

print("UHC wins:", stats.uhc_duels.wins)
print("Best UHC winstreak:", stats.uhc_duels.best_winstreak)
print("UHC golden apples eaten", stats.uhc_duels.golden_apples_eaten)
```

## bedwars

```python
print(list(stats.overall_bedwars.__fields__.keys())) #show all available functions for overall_bedwars

print("Total wins:", stats.overall_bedwars.wins)
print("Total kills:", stats.overall_bedwars.kills)
print("Total beds broken:", stats.overall_bedwars.beds_broken)
```

As shown above, all of the key concepts are the same as the duels stats example.

## bedwars practice mode

```python
print(list(stats.practice_bedwars.__fields__.keys())) #show all available functions for practice_bedwars

print("Bridging record:", stats.practice_bedwars.records.bridging_record)
print("Bridging blocks placed:", stats.practice_bedwars.bridging.blocks_placed)
print("Successful MLG attempts:",stats.practice_bedwars.mlg.successful_attempts)
```

## skywars 

```python 
print(list(stats.overall_skywars.__fields__.keys()))

print("Wins:", stats.overall_skywars.wins)
print("Games played:", stats.overall_skywars.games_played)
print("Coins:", stats.overall_skywars.coins)
```

# CHANGELOG

## 1.1.5

* Skywars stats updates:
    * Created a Solo Skywars stats class.
    * Added a Skywars level stat.

* Added more stats to the General stats file.

* Created more efficient models.

* Added the following Bedwars stats classes:
    * Solo
    * Duos
    * Trios
    * Squads
    * Four Versus Four

* Added the following Duels stats classes:
    * OP Doubles
    * UHC Meetup(Deathmatch)

## 1.1.4

* The API link now uses the user's uuid instead of player name.

* Created a General Hypixel stats file.

* Removed unnecessary imports from `__init__.py`.

* Updated annotations on several files.

* Added [`mojang`](https://github.com/summer/mojang "") library to `requirements.txt`.

## 1.1.3

* Fixed Practice stats bug.

## 1.1.2

* Added UHC and Bridge double stats.

## 1.1.1

* Added Bedwars cosmetic stats.

## 1.1.0

* Added Bedwars practice stats.
* Small changes to `utils.py`.

## 1.0.9

* Added `StatsModel` class to `utils.py`.

## 1.0.8

* The user no longer has to create an instance of the class model.
* Fixed bridge_duel suffix typo.

## 1.0.7

* Fixed kwarg filter error.

## 1.0.6

* Created stats model and kwarg filter(for prefixes/suffixes).
* Created requirements.txt.

## 1.0.5

* Created CHANGELOG.
* Added SkyWars duel stats.

## 1.0.4

* Changed mainframe to [`Pydantic`](https://github.com/samuelcolvin/pydantic "").
* Removed the `available_functions` variables.