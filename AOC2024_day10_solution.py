from collections import deque
day = 10

example_input = [[8,9,0,1,0,1,2,3],
                 [7,8,1,2,1,8,7,4],
                 [8,7,4,3,0,9,6,5],
                 [9,6,5,4,9,8,7,4],
                 [4,5,6,7,8,9,0,3],
                 [3,2,0,1,9,0,1,2],
                 [0,1,3,2,9,8,0,1],
                 [1,0,4,5,6,7,3,2]]

# load input puzzle 1
input = open(f'AOC2024_day{day}_input.txt','r')
lines=input.readlines()

data = []
for line in lines:
    data.append(line.split())

mapping = []
for line in data:
    mapping.append(list(map(int, str(line[0]))))

# define valid moves:
# x - 1 (left), x+1 (right), y-1 (down), y+1 (up)
rows, cols = len(mapping), len(mapping[0])
directions = [(-1,0), (1,0), (0,-1), (0,1)]

trails = []

# find all 0's
zeroes = [(r,c) for r in range(rows) for c in range(cols)if mapping[r][c] ==0]

for zero in zeroes:
    path_so_far = [(zero, [zero])]
    visited = set([zero])
    
    while path_so_far:
        (x,y), trail = path_so_far.pop(0)
        
        # check if 9 reached
        if mapping[x][y] == 9:
            trails.append(trail)
            continue
        
        # find neighbours
        for dx, dy in directions:
            nx, ny = x + dx, y+dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx,ny) not in visited:
                if mapping[nx][ny] - mapping[x][y] == 1:
                    visited.add((nx,ny))
                    path_so_far.append(((nx,ny), trail + [(nx,ny)]))


nr_trailheads = len(set([item[0] for item in trails]))


for item in trails:
    print(len(item))

score = 0
for item in set([item[0] for item in trails]):
    score+=[item[0] for item in trails].count(item)
    
# part 2
# define valid moves:
# x - 1 (left), x+1 (right), y-1 (down), y+1 (up)
rows, cols = len(mapping), len(mapping[0])
directions = [(-1,0), (1,0), (0,-1), (0,1)]

trails = []

# find all 0's
zeroes = [(r,c) for r in range(rows) for c in range(cols)if mapping[r][c] ==0]

for zero in zeroes:
    path_so_far = [(zero, [zero])]
        
    while path_so_far:
        (x,y), trail = path_so_far.pop(0)
        
        # check if 9 reached
        if mapping[x][y] == 9:
            trails.append(trail)
            continue
        
        # find neighbours
        for dx, dy in directions:
            nx, ny = x + dx, y+dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx,ny):
                if mapping[nx][ny] - mapping[x][y] == 1:
                    path_so_far.append(((nx,ny), trail + [(nx,ny)]))


nr_trailheads = len(set([item[0] for item in trails]))


for item in trails:
    print(len(item))

score = 0
for item in set([item[0] for item in trails]):
    score+=[item[0] for item in trails].count(item)
    

