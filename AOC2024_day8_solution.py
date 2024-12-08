import numpy as np
from itertools import combinations
day = 8

# get the input
antennas = np.loadtxt(f'AOC2024_day{day}_input.txt', dtype='str')

antennas_ex = np.loadtxt(f'example_day8.txt', dtype='str')

# get all unique antenas to loop through
unique_antennas = [set(item) for item in antennas]
unique_antennas = list(set().union(*unique_antennas))

# example
unique_ex = list(set().union(*[set(item) for item in antennas_ex]))
unique_ex.remove('.')

max_rowindex_ex = len(antennas_ex)-1
max_colindex_ex = len(antennas_ex[0])-1

# remove the dot because that is not an antenna
unique_antennas.remove('.')

# get max row and column index
max_rowindex = len(antennas)-1
max_colindex = len(antennas[0])-1

# define a function that finds the indices where unique antennas are located
# return a list of dictionaries, each dictionary contains the indices where a certain antenna is located
def find_antenna_mapping(antennas, unique_antennas):

    indices_antenna = []

    for antenna in unique_antennas:
        antenna_dict = {antenna: {}}

        for index_row, row in enumerate(antennas):
            for index, value in enumerate(row):
                if value == antenna:
                    antenna_dict[antenna][index_row] = index

        indices_antenna.append(antenna_dict)
    
    return indices_antenna

# define a function that tries to place an antinode in line with two antennas 
def place_antinode(indices_antenna, max_rowindex, max_colindex):

    antinodes_all = []
    
    for dict in indices_antenna:
        for antenna, coordinates in dict.items():
            pairs = list(combinations(coordinates.items(), 2))

            antinodes = []

            for (row1, col1), (row2, col2) in pairs:
                row_distance = abs(row1-row2)
                col_distance = abs(col1-col2)

                if row1 < row2: 
                    direction_y = 'topdown'
                    first_node_row = row1-row_distance
                    second_node_row = row2+row_distance
                elif row1 > row2:
                    direction_y = 'bottomup'
                    first_node_row = row1+row_distance
                    second_node_row = row2-row_distance
                else: 
                    direction_y = 'horizontal'
                    first_node_row = row1
                    second_node_row = row2
                    

                if col1 < col2 and direction_y == 'bottom_up' or col1 < col2 and direction_y == 'topdown' or col1< col2 and direction_y=='horizontal':
                    first_node_col = col1-col_distance
                    second_node_col = col2+col_distance
                elif col1 > col2 and direction_y == 'bottomup' or col1 > col2 and direction_y == 'topdown' or col1 > col2 and direction_y == "horizontal":
                    first_node_col = col1+col_distance
                    second_node_col = col2-col_distance
                else:
                    first_node_col = col1
                    second_node_col = col2
                
                if first_node_row > max_rowindex or first_node_col > max_colindex or first_node_row < 0 or first_node_col < 0:
                    antinode_1 = ()
                else: 
                    antinode_1 = (first_node_row, first_node_col)
                if second_node_row > max_rowindex or second_node_col > max_colindex or second_node_row < 0 or second_node_col < 0:
                    antinode_2 = ()
                else:
                    antinode_2 = (second_node_row, second_node_col)
                

                antinodes.append([antinode_1, antinode_2])

        
            antinodes_all.append({antenna: antinodes})

    return antinodes_all

mapping_antennas = find_antenna_mapping(antennas, unique_antennas)
antinodes = place_antinode(mapping_antennas, max_rowindex, max_colindex)


# probeersel = find_antenna_mapping(antennas_ex, unique_ex)
# example_nodes = place_antinode(probeersel, max_rowindex=max_rowindex_ex, max_colindex=max_colindex_ex)

unique_antinodes = set()

for dict in antinodes:
    for antenna, antinodes in dict.items():
        for antinode_group in antinodes:
            for antinode in antinode_group:
                if antinode:  # Ignore empty tuples
                    unique_antinodes.add(antinode)

unique_pair_count = len(unique_antinodes)

# PART 2

def place_all_antinodes(indices_antenna, max_rowindex, max_colindex):

    antinodes_all = []
    
    for dict in indices_antenna:
        for antenna, coordinates in dict.items():
            pairs = list(combinations(coordinates.items(), 2))

            antinodes = []

            for (row1, col1), (row2, col2) in pairs:
                row_distance = abs(row1-row2)
                col_distance = abs(col1-col2)

                if col1 < col2: 
                    direction_x = 'left'
                elif col1 > col2:
                    direction_x = 'right'
                else:
                    direction_x = 'left'

                antinodes.append((row1, col1))
                # forwards checker
                in_bound = True
                count = 1
                
                while in_bound is True:

                    if direction_x == 'left':
                        antinode = (row1+(count*row_distance), col1+(count*col_distance))
                    if direction_x == 'right':
                        antinode = (row1+(count*row_distance), col1-(count*col_distance))

                    count += 1
                    
                    if antinode[0] > max_rowindex or antinode[1] > max_colindex or antinode[1] < 0: 
                        in_bound = False
                    else:
                        antinodes.append(antinode)


                # backwards checker 
                in_bound = True
                count = 1
                
                while in_bound is True:

                    if direction_x == 'left':
                        antinode = (row1-(count*row_distance), col1-(count*col_distance))
                    if direction_x == 'right':
                        antinode = (row1-(count*row_distance), col1+(count*col_distance))

                    count += 1
                    
                    if antinode[0] < 0 or antinode[1] > max_colindex or antinode[1] < 0: 
                        in_bound = False
                    else:
                        antinodes.append(antinode)

        
            antinodes_all.append({antenna: antinodes})

    return antinodes_all

probeersel = find_antenna_mapping(antennas_ex, unique_ex)
example_nodes = place_all_antinodes(probeersel, max_rowindex=max_rowindex_ex, max_colindex=max_colindex_ex)

unique_antinodes_ex = set()

for dict in example_nodes:
    for antenna, antinodes in dict.items():
        for antinode in antinodes:
            if antinode:  # Ignore empty tuples
                unique_antinodes_ex.add(antinode)

unique_pair_count_ex = len(unique_antinodes_ex)

antinodes = place_all_antinodes(mapping_antennas, max_rowindex, max_colindex)
unique_antinodes = set()

for dict in antinodes:
    for antenna, antinodes_map in dict.items():
        for antinode in antinodes_map:
            if antinode:  # Ignore empty tuples
                unique_antinodes.add(antinode)

unique_pair_count = len(unique_antinodes)