def get_day_input(number: int):
    file = open(f'inputs/day_{number}.txt', 'r')
    text = file.read()
    file.close()
    return text

inf = float('inf')
BIG = 10 ** 999
