"""
Diamond square algorithm for random terrain generation.
Python version 3.4.3
numpy version 1.11.2
matplotlib version 1.5.3
requires mpl_toolkits.mplot3d library for 3d plots.
"""
from diamond_square.config import config
from diamond_square.algorithm.methods import f_seed_grid, f_dsmain, f_plotting

if __name__ == "__main__":
    # Inputs here. Recommend ds_steps = 3 up to 11 for 2d and 3 - 5 for 3d.
    ds_steps = config.STEPS  # Number of levels. Grid points = ((ds_steps^2)+1)^2.
    max_rnd = config.MAX_HEIGHT  # Min & Max random value.
    plot_type = config.PLOT_TYPE  # "3d" for 3d.  Makes 2d plot for any other input.
    # Inputs end.
    max_index = config.GRID_SIZE

    seeded_map = f_seed_grid(2**ds_steps + 1)
    Final_height_map = f_dsmain(seeded_map, ds_steps, max_index, max_rnd)  # Calcs.
    f_plotting(Final_height_map, max_index, plot_type)  # Plotting.
