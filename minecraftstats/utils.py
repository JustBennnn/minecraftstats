"""Utils file for extra functions."""
__all__ = []

def filter_kwargs(_prefix, _suffix, _game_modes, _game_mode="", **kwargs):
    """Filter the kwargs to the specific gamemode and remove any prefixes or suffixes."""
    breaker = False
    filtered_kwargs = {}

    """Get the stats relative to the stats the user is looking for."""
    if _game_mode == "":
        for k, v in kwargs.items():
            for mode in _game_modes:
                if mode in k:
                    breaker = True
                    break

            if breaker == True:
                breaker = False
                continue

            filtered_kwargs[k] = v
    else:
        filtered_kwargs = {k: v for k, v in kwargs.items() if _game_mode in k}
                
    prefix_kwargs = {k[len(_prefix):]: v for k, v in filtered_kwargs.items() if k.startswith(_prefix) == True and k.endswith(_suffix) == False} #remove prefixes from keys
    suffix_kwargs = {k[0:len(k)-len(_suffix)]: v for k, v in filtered_kwargs.items() if k.endswith(_suffix) == True and k.startswith(_prefix) == False} #remove suffixes from keys
    ps_kwargs = {k[len(_prefix):len(k)-len(_suffix)]: v for k, v in filtered_kwargs.items() if k.startswith(_prefix) == True and k.endswith(_suffix) == True} #remove prefixes and suffixes from keys
    extra_kwargs = {k: v for k, v in filtered_kwargs.items() if k.startswith(_prefix) == False and k.endswith(_suffix) == False} #keep keys that don't have prefixes or suffixes

    kwargs = {**prefix_kwargs, **suffix_kwargs, **ps_kwargs, **extra_kwargs}
    return kwargs