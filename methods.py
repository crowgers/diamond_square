import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import random
import time


def f_avg(*args):
    """Takes in arbitray arguments and computes their average."""
    return float(sum(args)) / float(len(args))


def f_rnjesus(rand):
    """Returns uniformly distributed presudo-random value between +/- rand."""
    return random.uniform(-rand, rand)

def f_rngauss(rand):  # Incomplete.  Experimenting with.
    return random.gauss(0, 2*rand/5)


def f_seed_grid(grid_size, max_rnd):
    """Initialisation function. Creates and seeds 4 corners of grid."""
    height_map = np.zeros((grid_size, grid_size), dtype=float)
    height_map[0, 0] = f_rnjesus(max_rnd)
    height_map[0, grid_size - 1] = f_rnjesus(max_rnd)
    height_map[grid_size - 1, 0] = f_rnjesus(max_rnd)
    height_map[grid_size - 1, grid_size - 1] = f_rnjesus(max_rnd)
    return height_map


def f_plotting(height_map, max_index, plot_type):
    """Function plots either 2D or 3D heatmap."""
    timestr = time.strftime("%Y%m%d-%H%M%S")

    if plot_type == "3d":
        x_index = [i for i in range(0, max_index + 1)]
        y_index = [i for i in range(0, max_index + 1)]
        x_vals, y_vals = np.meshgrid(x_index, y_index)
        fig = plt.figure()
        p2 = fig.add_subplot(111, projection="3d")
        p2.set_title("Diamond Square 3D Surface Plot")
        p2.set_aspect("equal")
        p2.plot_surface(x_vals, y_vals, height_map, rstride=1, cstride=1, cmap=cm.jet)
        plt.savefig("3D_dS%s.png" % timestr, bbox_inches="tight")
        plt.show()
    else:
        fig = plt.figure()
        p3 = fig.add_subplot(111)
        p3.set_title("Diamond Square 2D Terrain Heatmap")
        p3.set_aspect("equal")
        plt.imshow(height_map, origin="lower", cmap=cm.jet)
        plt.savefig("2D_dS%s.png" % timestr, bbox_inches="tight")
        plt.show()


def f_square_step(height_map, grid_split, shape_length, lo_rnd):
    """Function computes square step (reference points form square)."""
    for i in range(grid_split):
        for j in range(grid_split):
            # REDEFINE STEP SIZE INCREMENTER & SHAPE INDICES.
            half_v_grid_size = shape_length // 2
            i_min = i * shape_length
            i_max = (i + 1) * shape_length
            j_min = j * shape_length
            j_max = (j + 1) * shape_length
            i_mid = i_min + half_v_grid_size
            j_mid = j_min + half_v_grid_size
            # ASSIGN REFERENCE POINTS & DO SQUARE STEP.
            north_west = height_map[i_min, j_min]
            north_east = height_map[i_min, j_max]
            south_west = height_map[i_max, j_min]
            south_east = height_map[i_max, j_max]
            height_map[i_mid, j_mid] = f_avg(north_west, north_east, \
            south_east, south_west) + f_rnjesus(lo_rnd)
    return height_map


def f_diamond_step(height_map, grid_split, shape_length, lo_rnd, max_index):
    """Function computes diamond step (reference points form diamond)."""
    for i in range(grid_split):
        for j in range(grid_split):
            # REDEFINE STEP SIZE INCREMENTER & SHAPE INDICES.
            half_v_grid_size = shape_length // 2
            i_min = i * shape_length
            i_max = (i + 1) * shape_length
            j_min = j * shape_length
            j_max = (j + 1) * shape_length
            i_mid = i_min + half_v_grid_size
            j_mid = j_min + half_v_grid_size
            center = height_map[i_mid, j_mid]
            north_west = height_map[i_min, j_min]
            north_east = height_map[i_min, j_max]
            south_west = height_map[i_max, j_min]
            south_east = height_map[i_max, j_max]
            # DO DIAMOND STEP.
            # Top Diamond - wraps if at edge.
            if i_min == 0:
                temp = max_index - half_v_grid_size
            else:
                temp = i_min - half_v_grid_size
            # If Top value exists then skip else compute.
            if height_map[i_min, j_mid] == 0:
                height_map[i_min, j_mid] = f_avg(center, north_west, \
                north_east, height_map[temp, j_mid]) + f_rnjesus(lo_rnd)

            # Left Diamond - wraps if at edge.
            if j_min == 0:
                temp = max_index - half_v_grid_size
            else:
                temp = j_min - half_v_grid_size
            # If Left value exists then skip else compute.
            if height_map[i_mid, j_min] == 0:
                height_map[i_mid, j_min] = f_avg(center, north_west, \
                south_west, height_map[i_mid, temp]) + f_rnjesus(lo_rnd)

            # Right Diamond - wraps if at edge.
            if j_max == max_index:
                temp = 0 + half_v_grid_size
            else:
                temp = j_max + half_v_grid_size
            height_map[i_mid, j_max] = f_avg(center, north_east, south_east, \
            height_map[i_mid, temp]) + f_rnjesus(lo_rnd)

            # Bottom Diamond - wraps at edge.
            if i_max == max_index:
                temp = 0 + half_v_grid_size
            else:
                temp = i_max + half_v_grid_size
            height_map[i_max, j_mid] = f_avg(center, south_west, south_east, \
            height_map[temp, j_mid]) + f_rnjesus(lo_rnd)
    return height_map


def f_dsmain(height_map, steps, max_index, max_rnd):
    """Main looping function.  Calls methods in proper step."""
    # Set iterators
    shape_length = len(height_map) - 1
    grid_split = 1  # Number of shapes is this number squared.
    for level in range(steps):
        lo_rnd = max_rnd / (level + 1)
        f_square_step(height_map, grid_split, shape_length, lo_rnd)
        f_diamond_step(height_map, grid_split, shape_length, lo_rnd, max_index)
        # Increment iterators for next loop. Use floor divide to force int.
        shape_length //= 2
        grid_split *= 2
    return height_map
