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
**Note**: The main framework for this project is [Pydantic](https://github.com/samuelcolvin/pydantic "").\
**Side Note**: Any stats that return hearts are measured in halves.

## duels
This example shows how to get stats from the duels lobby.

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

The easiest way to retrieve stats is by getting the data returned by the API with `get_user_stats()`, and then passing 
that as a kwarg into the desired class. Then you can access the stats as attributes to the class.

The next example shows getting stats from an individual game mode in the duels lobby.

```python
print(list(stats.uhc_duels.__fields__.keys())) #show all available stats for uhc_duels

print("UHC wins:", stats.uhc_duels.wins)
print("Best UHC winstreak:", stats.uhc_duels.best_winstreak)
print("UHC golden apples eaten", stats.uhc_duels.golden_apples_eaten)
```

## bedwars
This example shows how to get stats from the bedwars lobby.

```python
print(list(stats.overall_bedwars.__fields__.keys())) #show all available functions for overall_bedwars

print("Total wins:", stats.overall_bedwars.wins)
print("Total kills:", stats.overall_bedwars.kills)
print("Total beds broken:", stats.overall_bedwars.beds_broken)
```

As shown above, most of the key concepts are the same as the duels stats example.

# CHANGELOG

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

* Changed mainframe to [Pydantic](https://github.com/samuelcolvin/pydantic "").
* Removed the `available_functions` variables.