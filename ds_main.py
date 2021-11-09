"""
Diamond square algorithm for random terrain generation.
Python version 3.4.3
numpy version 1.11.2
matplotlib version 1.5.3
requires mpl_toolkits.mplot3d library for 3d plots.
"""
from diamond_square.methods import *


if __name__ == "__main__":
    # Inputs here. Recommend ds_steps = 3 up to 11 for 2d and 3 - 5 for 3d.
    ds_steps = 5  # Number of levels. Grid points = ((ds_steps^2)+1)^2.
    max_rnd = 1.0  # Min & Max random value.
    plot_type = "3d"  # "3d" for 3d.  Makes 2d plot for any other input.
    # Inputs end.
    max_index = 2 ** ds_steps
    seeded_map = f_seed_grid(2**ds_steps + 1, max_rnd)
    Final_height_map = f_dsmain(seeded_map, ds_steps, max_index, max_rnd)  # Calcs.
    f_plotting(Final_height_map, max_index, plot_type)  # Plotting.
