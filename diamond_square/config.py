from dataclasses import dataclass


@dataclass
class _Config:
    DATETIME_FORMAT: str = ""
    MAX_HEIGHT: int = 1.0
    MIN_HEIGHT: int = -1.0
    PLOT_TYPE: str = "3d"
    STEPS: int = 5

    # Composite Variable
    GRID_SIZE: int = 2 ** STEPS


# Effectively a singleton
config = _Config()
