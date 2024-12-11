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
    
example = sum(example, [])

for row, item in enumerate(example):
    for column, element in enumerate(item):
        if element != "^":
            continue
        elif element =="^":
            start_position = (row, column)

obstacle_coordinates = []

for row, item in enumerate(example):
    for column, element in enumerate(item):
        if element != "#":
            continue
        elif element =="#":
            obstacle_coordinates.append((row, column))
  

out_of_bounds = False
direction = "up"
visited_coordinates = [start_position]
next_position = start_position
while out_of_bounds = False:
    
    if direction == "up":
        next_position = (next_position[0]-1, next_position[1])
    # move up until obstacle
    # if obstacle (#) change direction to right move right until obstacle
    # if obstacle (#) change direction to down move down until obstacle
    # if obstacle (#) change direction to left move left until obstacle
    # if obstacle (#) change direction to up move up until obstacle
    # each step; save coordinates 
    # if next coordinate is out of bounds: out_of_bounds = True

