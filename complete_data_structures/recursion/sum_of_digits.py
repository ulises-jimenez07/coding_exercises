def sum_digits(n):
    assert n >= 0 and int(n) == n, "N has to be positive integer only"
    if n < 10:
        return n
    remainder = n % 10
    return remainder + sum_digits(n // 10)


print(sum_digits(110812))
