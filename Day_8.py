from Day_0 import get_day_input
from collections import defaultdict

d, history = defaultdict(lambda: 0), []
instructions = [ i.split(' ') for i in get_day_input(8).replace("inc", "+=").replace("dec", "-=").split('\n')[:-1] ]

for xp in instructions:
    exec(" ".join(["if", f"d['{xp[4]}']", xp[5], xp[6], ':', f"d['{xp[0]}']", xp[1], xp[2]]))
    history.append(max(d.values()))

print(f"Day 8-1: {max(d.values())}") # 6343
print(f"Day 8-2: {max(history)}") # 7184
