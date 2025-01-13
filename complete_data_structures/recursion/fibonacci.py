def fibonacci(n):
    assert n >= 0 and int(n) == n, "N must be integer only"
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))
