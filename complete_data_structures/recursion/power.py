def power(base, exp):
    assert int(exp) == exp, "The exponent must be integer"
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / base * power(base, exp + 1)
    return base * power(base, exp - 1)


print(power(4, 4))
