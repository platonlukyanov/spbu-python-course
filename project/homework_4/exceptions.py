class SplitError(Exception):
    """Exception raised when trying to split a hand with more than two cards"""

    message = "Hand must contain exactly two identical value cards"
