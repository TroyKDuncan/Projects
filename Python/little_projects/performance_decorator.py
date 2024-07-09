from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'Time elapsed for {fn}: {round(t2 - t1, 2)} ms')
        return result
    return wrapper


@performance
def long_function():
    for i in range(100000000):
        i*5


long_function()


@performance
def hard_math(*args):
    total = 1
    for num in args:
        total *= num
    return total


print(hard_math(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
      16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30))
