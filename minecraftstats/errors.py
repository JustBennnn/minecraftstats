"""MinecraftStats error messages

These are custom error messages.
"""
class MinecraftStatsException(Exception):
    """Base class for other custom exceptions."""
    pass

class DataError(MinecraftStatsException):
    """An error for any invalid data entered or received."""
    pass

class StatError(MinecraftStatsException):
    """An error called when the user tries to get a stat that isn't from the mode."""
    pass