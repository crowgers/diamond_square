# Standard Library Imports
import random
from typing import List


def get_average_of(numbers: List[float]) -> float:
    """Takes in arbitrary arguments and computes their average."""
    return float(sum(numbers)) / float(len(numbers))


def get_random_float(min_height: int, max_height: int) -> float:
    """Returns a random number between max and min height."""
    return random.uniform(min_height, max_height)
