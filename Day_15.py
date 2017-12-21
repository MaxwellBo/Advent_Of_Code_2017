A_START, B_START = 699, 124
A_FACTOR, B_FACTOR = 16807, 48271
A_MULTIPLE, B_MULTIPLE = 4, 8 
DIVISOR = 2147483647
count = 0

def gen(start, factor, multiple=None):
    nxt = start

    while True:
        if not multiple or nxt % multiple == 0:
            yield nxt

        nxt = (nxt * factor) % DIVISOR

a, am = gen(A_START, A_FACTOR), gen(A_START, A_FACTOR, A_MULTIPLE)
b, bm = gen(B_START, B_FACTOR), gen(B_START, B_FACTOR, B_MULTIPLE)

for i in range(40000000):
    if next(a) & 65535 == next(b) & 65535: count += 1

print("Part 15-1: {count}".format(count=count)) # 600

count = 0 

for i in range(5000000):
    if next(am) & 65535 == next(bm) & 65535: count += 1

print("Part 12-2: {count}".format(count=count)) # 313
