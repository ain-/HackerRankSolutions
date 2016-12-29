cube = lambda x: x**3


def fibonacci(n):
    fib = list(range(n))
    if n < 2:
        return fib
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib

n = int(input())
#Python 3 can't print out a map directly, need to wrap it in a list
print(list(map(cube, fibonacci(n))))
