def gcd(a, b):
    assert int(a) == a and int(b) == b, "Values must be integer"

    def _gcd(a, b):
        if b == 0:
            return a
        return _gcd(b, a % b)

    return _gcd(a, b)


print(gcd(48, 1.8))
