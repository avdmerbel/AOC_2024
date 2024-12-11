from functools import lru_cache
from collections import Counter

day = 11

rules = ["engraved with 0, replace by 1",
         "engraved with even number of digits, left half in one stone, right half the other no leading zeroes",
         "none of the above: old number multiplied by 2024"]

def change_stone(stone):
    
    if stone == 0: 
        stone = [1]
    elif len(str(stone))%2 == 0: 
        engraving_length_half = int(len(str(stone))/2)
        stone = [int(str(stone)[0:engraving_length_half]), 
                 int(str(stone)[engraving_length_half:len(str(stone))])
                 ]
    else:
        stone = [stone*2024]
        
    return stone

puzzle_input = [2, 72, 8949, 0, 981038, 86311, 246, 7636740]

example_input = [125, 17]

new_arrangement = [2, 72, 8949, 0, 981038, 86311, 246, 7636740]
blinks = 1

while blinks <= 25:
    
    blinks += 1 
    
    for index, stone in enumerate(new_arrangement):
        new_arrangement[index]= change_stone(stone)
    
    new_arrangement = sum(new_arrangement, [])

# part 2
# obviously this is going to go WRONG if I do it the same way
# make dictionary of each stone that passes by

# first we have to get our data into a dictionary

stones = dict(Counter(puzzle_input))

#@lru_cache(maxsize=128)
def change_stone(arrangement):
    
    new_stones = {}
    
    for stone, count in arrangement.items():
        
        if stone == 0: 
            
            if 1 in new_stones:
                new_stones[1] += count
            else:
                new_stones[1] = count
            
        elif len(str(stone))%2 == 0: 
            engraving_length_half = int(len(str(stone))/2)
            
            first_half = int(str(stone)[0:engraving_length_half])
            
            if first_half in new_stones:
                new_stones[first_half] += count
            else:
                new_stones[first_half] = count
                    
            second_half = int(str(stone)[engraving_length_half:len(str(stone))])
            
            if second_half in new_stones:
                new_stones[second_half] += count
            else:
                new_stones[second_half] = count
            
        else:
            new_numb = stone*2024
            
            if new_numb in new_stones:
                new_stones[new_numb] += count
            else:
                new_stones[new_numb] = count
        
    return new_stones
import time
begin = time.time()
for blink in range(75):
    stones = change_stone(stones)
end = time.time()    
