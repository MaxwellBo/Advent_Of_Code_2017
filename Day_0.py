def get_day_input(number: int):
    file = open(f'inputs/day_{number}.txt', 'r')
    text = file.read()
    file.close()
    return text

def get_day_input_lines(number: int):
    return get_day_input(number).split('\n')

inf = float('inf')
BIG = 10 ** 999
