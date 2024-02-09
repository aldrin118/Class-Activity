import time

def memoize(func):

    cache = {}
    def wrapper(n):
        print(cache)

        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return wrapper


@memoize
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("first call")
factorial(5)
print("second call")
factorial(5)
