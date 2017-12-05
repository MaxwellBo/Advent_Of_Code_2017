def getDayInput(number):
    file = open('inputs.txt', 'r')
    text = file.read()
    file.close()
    return text

inf = float('inf')
BIG = 10 ** 999
