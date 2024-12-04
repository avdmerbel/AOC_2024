import numpy as np
import re

day = 4

# get the input
data_array = np.loadtxt(f'AOC2024_day{day}_input.txt', dtype='str')

example_array = ["MMMSXXMASM",
                 "MSAMXMSMSA",
                 "AMXSXMAAMM",
                 "MSAMASMSMX",
                 "XMASAMXAMM",
                 "XXAMMXXAMA",
                 "SMSMSASXSS",
                 "SAXAMASAAA",
                 "MAMMMXMMMM",
                 "MXMXAXMASX"]

# find everything horizontally both ways
# easy: search pattern XMAS and SAMX
# find everything vertically both ways
# harder: index on one element and corresponding index on the next 
# find everything diagonally both ways