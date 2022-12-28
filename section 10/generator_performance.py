from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        time1 = time()
        result = fn(*args, **kwargs)
        time2 = time()
        print(f"it took {time2 - time1}s to run")
        return result
    return wrapper


@performance
def long_time():
    print(1)
    for i in range(10000000):
        i * 5


long_time()


@performance
def long_time2():
    print(2)
    for i in list(range(10000000)):
        i * 5


long_time2()
