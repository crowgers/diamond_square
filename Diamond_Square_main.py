# Diamond square algorithm for random terrain generation.
import numpy as np  # Using version 1.11.2 print(numpy.__version__)
import matplotlib.pyplot as plt  # Using version 1.5.3 print(matplotlib.__version__)
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import random


def fn_avg(*args):  # Averaging Function.
	return float(sum(args))/float(len(args))


def fn_rnjesus(rnd_max):  # Generates pseudo_random number.
	return random.uniform(-rnd_max, rnd_max)


def fn_heat_plot_2d(height_map):  # Function plots 2D heatmap.
	fig = plt.figure()
	hp = fig.add_subplot(111)
	hp.set_title('Diamond Square 2D Terrain Heatmap')
	hp.set_aspect('equal')
	plt.imshow(height_map, origin='lower')
	plt.savefig('DiamondSquare.png', bbox_inches='tight')
	plt.show()


def fn_mesh_plot_3d(height_map):  # Plots 3D surface map
	x_index = [i for i in range(0, G_MAX_INDEX+1)]
	y_index = [i for i in range(0, G_MAX_INDEX+1)]
	fig = plt.figure()
	mp = fig.add_subplot(111, projection='3d')
	mp.set_title('Diamond Square 3D Surface Plot')
	mp.set_aspect('equal')
	x_coords, y_coords = np.meshgrid(x_index, y_index)
	mp.plot_surface(x_coords, y_coords, height_map, rstride=1, cstride=1, cmap=cm.jet)
	plt.savefig('DiamondSquare3D.png', bbox_inches='tight')
	plt.show()


# Function to compute square step (reference points form square).
def fn_square_step(height_map, grid_split, shape_side_length, level):
	for i in range(grid_split):
		for j in range(grid_split):
			# REDEFINE STEP SIZE INCREMENTER & SHAPE INDICES
			half_v_grid_size = shape_side_length//2
			i_min = i*shape_side_length
			i_max = (i+1)*shape_side_length
			j_min = j*shape_side_length
			j_max = (j+1)*shape_side_length
			i_mid = i_min + half_v_grid_size
			j_mid = j_min + half_v_grid_size
			# ASSIGN REFERENCE POINTS & DO SQUARE STEP
			north_west = height_map[i_min, j_min]
			north_east = height_map[i_min, j_max]
			south_west = height_map[i_max, j_min]
			south_east = height_map[i_max, j_max]
			height_map[i_mid, j_mid] = fn_avg(north_west, north_east, south_east, south_west) + fn_rnjesus(G_MAX_RND/level)
	return height_map


# Function to compute diamond step (reference points form diamond).
def fn_diamond_step(height_map, grid_split, shape_side_length, level):
	for i in range(grid_split):
		for j in range(grid_split):
			# REDEFINE STEP SIZE INCREMENTER & SHAPE INDICES
			half_v_grid_size = shape_side_length // 2
			i_min = i*shape_side_length
			i_max = (i+1)*shape_side_length
			j_min = j*shape_side_length
			j_max = (j+1)*shape_side_length
			i_mid = i_min+half_v_grid_size
			j_mid = j_min+half_v_grid_size
			center = height_map[i_mid, j_mid]
			north_west = height_map[i_min, j_min]
			north_east = height_map[i_min, j_max]
			south_west = height_map[i_max, j_min]
			south_east = height_map[i_max, j_max]
			# DO DIAMOND STEP
			# Top Diamond - wraps if at edge
			if i_min == 0:
				temp = G_MAX_INDEX - half_v_grid_size
			else:
				temp = i_min - half_v_grid_size
			# If Top value exists then skip else compute
			if height_map[i_min, j_mid] == 0:
				height_map[i_min, j_mid] = fn_avg(center, north_west, north_east, height_map[temp, j_mid]) \
											+ fn_rnjesus(G_MAX_RND/level)

			# Left Diamond - wraps if at edge
			if j_min == 0:
				temp = G_MAX_INDEX - half_v_grid_size
			else:
				temp = j_min - half_v_grid_size
			# If Left value exists then skip else compute
			if height_map[i_mid, j_min] == 0:
				height_map[i_mid, j_min] = fn_avg(center, north_west, south_west, height_map[i_mid, temp]) \
											+ fn_rnjesus(G_MAX_RND/level)

			# Right Diamond - wraps if at edge
			if j_max == G_MAX_INDEX:
				temp = 0 + half_v_grid_size
			else:
				temp = j_max + half_v_grid_size
			# If Right value exists then skip else compute
			if height_map[i_mid, j_max] == 0:
				height_map[i_mid, j_max] = fn_avg(center, north_east, south_east, height_map[i_mid, temp]) \
											+ fn_rnjesus(G_MAX_RND/level)

			# Bottom Diamond - wraps at edge
			if i_max == G_MAX_INDEX:
				temp = 0 + half_v_grid_size
			else:
				temp = i_max + half_v_grid_size
			# If Bottom Value exists then skip else compute
			if height_map[i_max, j_mid] == 0:
				height_map[i_max, j_mid] = fn_avg(center, south_west, south_east, height_map[temp, j_mid]) \
											+ fn_rnjesus(G_MAX_RND/level)
	return height_map


def fn_compute_values(height_map):  # Main looping function.  Calls methods.
	# Set iterators
	shape_side_length = G_MAX_INDEX
	grid_split = 1
	for level in range(G_SIZE):
		# level is used to progressively reduce random addition to points
		fn_square_step(height_map, grid_split, shape_side_length, level+1)
		fn_diamond_step(height_map, grid_split, shape_side_length, level+1)
		# Increment iterators for next loop
		shape_side_length //= 2
		grid_split *= 2
	return height_map


def fn_seed_grid(grid_size):  # Seed 4 corners of grid.
	height_map = np.zeros((grid_size, grid_size), dtype=float)
	height_map[0, 0] = fn_rnjesus(G_MAX_RND)
	height_map[0, grid_size - 1] = fn_rnjesus(G_MAX_RND)
	height_map[grid_size - 1, 0] = fn_rnjesus(G_MAX_RND)
	height_map[grid_size - 1, grid_size - 1] = fn_rnjesus(G_MAX_RND)
	return height_map

# Starts here.
G_SIZE = 5  # Recommend 3 up to 10 for 2d and 3 - 5 for 3d
G_MAX_RND = 1.0  # Min & Max rnd value.
# Grid size must be (2^G_SIZE)+1 however index starts @0 so below is convenient
G_MAX_INDEX = 2**G_SIZE
Final_height_map = fn_compute_values(fn_seed_grid(G_MAX_INDEX+1))
fn_mesh_plot_3d(Final_height_map)
# fn_heat_plot_2d(Final_height_map)
