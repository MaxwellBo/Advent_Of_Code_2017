import numpy as np
from Day_0 import get_day_input

mutations = [ lambda x: x
            , lambda x: np.rot90(x, 1) 
            , lambda x: np.rot90(x, 2) 
            , lambda x: np.rot90(x, 3) 
            , lambda x: np.fliplr(x)
            , lambda x: np.fliplr(np.rot90(x, 1))
            , lambda x: np.fliplr(np.rot90(x, 2))
            , lambda x: np.fliplr(np.rot90(x, 3))
            ]

def parse(xs):
    return np.array([[ col for col in row ] for row in xs.split('/') ])

def enhance(a):
    for f in mutations:
        if f(a).tostring() in enhancements: 
            return enhancements[f(a).tostring()]


enhancements = {}

for enhancement in get_day_input(21).strip().split('\n'):
    frm, _, to = enhancement.split()
    enhancements[parse(frm).tostring()] = parse(to)

arr = parse(".#./..#/###")

for i in range(18):
    divided = []
    axis = arr.shape[0]

    if axis % 2 == 0:
        divided = [ np.hsplit(i, axis / 2) for i in np.vsplit(arr, axis / 2) ]
    else:
        divided = [ np.hsplit(i, axis / 3) for i in np.vsplit(arr, axis / 3) ]

    arr = np.vstack([ np.hstack( [ enhance(j) for j in i ] ) for i in divided ])

    if i == 4: print(f"Day 21-1: {np.count_nonzero(arr == '#')}") # 142
    if i == 17: print(f"Day 21-2: {np.count_nonzero(arr == '#')}") # 1879071


