import numpy as np
day = 6

# read in example input
example_input = open(f'example_day{day}.txt','r')
#input = open(f'example_day5.txt', 'r')
example_lines=example_input.readlines()

# get the lists of numbers
example = []
for line in example_lines:
    example.append(line.split())

