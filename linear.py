import random
from algorithm import start


def calculate_time(num):
    if num == 0:
        return 0
    return random.randrange(0, num + 1, 1)


start(calculate_time)
