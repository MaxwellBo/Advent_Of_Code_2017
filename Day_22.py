
from Day_0 import *
from collections import defaultdict

CLEAN, WEAKENED, INFECTED, FLAGGED, DIRECTIONS = '.', 'W', '#', 'F', [N, E, S, W]

def load_grid():
    grid = defaultdict(lambda: '.')

    for (y, row) in enumerate(get_day_input(22).strip().split('\n')):
        for (x, col) in enumerate(row):
            grid[(x - (len(row) // 2) + -1j * (y - (len(row) // 2))) ] = col 

    return grid 

def part_1():
    facing, pos, infected, grid = 0, (0 + 0j), 0, load_grid()

    for i in range(10000):
        if grid[pos] == CLEAN:
            facing -= 1 # turn left
            grid[pos] = INFECTED; infected += 1
        else:
            facing += 1 # turn right
            grid[pos] = CLEAN

        pos += DIRECTIONS[facing % len(DIRECTIONS)]

    print(f'Day 22-1: {infected}') # 5399

def part_2():
    facing, pos, infected, grid = 0, (0 + 0j), 0, load_grid()

    for i in range(10000000):
        if grid[pos] == CLEAN:
            facing -= 1 # turn left
            grid[pos] = WEAKENED
        elif grid[pos] == WEAKENED:
            # continue straight
            grid[pos] = INFECTED; infected += 1
        elif grid[pos] == INFECTED:
            facing += 1 # turn right
            grid[pos] = FLAGGED
        elif grid[pos] == FLAGGED:
            facing += len(DIRECTIONS) // 2 # about-face
            grid[pos] = CLEAN

        pos += DIRECTIONS[facing % len(DIRECTIONS)]

    print(f'Day 22-2: {infected}') # 2511776

part_1()
part_2()