from algorithm import start
import random

def calculate_time(num):
    if num == 0:
        return 0

    # using (2^N - 1) as the exponent range limiter
    # the function randrange goes from x to (y - 1)
    # so the limiter becomes (2^N - 1 + 1) = 2^N
    stop = 2**num
    return random.randrange(0, stop, 1)


start(calculate_time)
