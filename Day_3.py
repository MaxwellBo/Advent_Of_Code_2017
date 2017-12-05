from Day_0 import *

INPUT = 347991

Point = complex
N, S, E, W = 1j, -1j, 1, -1

def distance(point): return abs(point.real) + abs(point.imag)

square = 2
pos = 1

def log():
    if (square == INPUT): print(f"Day 1: {distance(pos)}"); return True else: return False

for i in range(2, BIG, 2): # start at side length 3
    for _ in range(i - 1): pos += N; square += 1; log()
    for _ in range(i): pos += W; square += 1; log()
    for _ in range(i): pos += S; square += 1; log()
    for _ in range(i + 1): pos += E; square += 1; log()

    print(square, pos)

