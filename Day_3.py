from Day_0 import *
from collections import defaultdict

INPUT = 347991
N, S, E, W = 1j, -1j, 1, -1
NE, SE, SW, NW = (N + E), (S + E), (S + W), (N + W)

def distance(point): return abs(point.real) + abs(point.imag)

square, pos, found = 2, (1 + 0j), False

grid = defaultdict(int)
grid[(0 + 0j)], grid[(1 + 0j)] = 1, 1

def log(): 
    if square == INPUT: print(f"Part 1: {int(distance(pos))}"); exit(0) # 480

def neighbours_sum(): return sum(grid[pos + i] for i in [N, S, E, W, NE, SE, SW, NW])

def spread():
    global found
    grid[pos] = neighbours_sum()
    if grid[pos] > INPUT and not found: print(f"Part 2: {grid[pos]}"); found = True # 349975

for i in range(2, BIG, 2): # start at side length 3
    for _ in range(i - 1): pos += N; square += 1; spread(); log()
    for _ in range(i):     pos += W; square += 1; spread(); log()
    for _ in range(i):     pos += S; square += 1; spread(); log()
    for _ in range(i + 1): pos += E; square += 1; spread(); log()
