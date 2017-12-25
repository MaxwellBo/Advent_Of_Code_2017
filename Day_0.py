import cmath
import math

def get_day_input(number: int):
    file = open(f'inputs/day_{number}.txt', 'r')
    text = file.read()
    file.close()
    return text

def get_day_input_lines(number: int):
    return get_day_input(number).split('\n')

def for_each(f, xs):
    return list(map(f, xs))

inf = float('inf')
BIG = 10 ** 999
N, S, E, W = 1j, -1j, 1, -1
NE, SE, SW, NW = (N + E), (S + E), (S + W), (N + W)