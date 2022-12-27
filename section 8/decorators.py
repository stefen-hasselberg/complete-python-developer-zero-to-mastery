# Decorator
# Why we need it
# performance decorator to measure how fast our code is
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        time1 = time()  # get start time
        result = fn(*args, **kwargs)
        time2 = time()  # get end time
        print(f'took {time2 - time1} s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i * 5


long_time()
