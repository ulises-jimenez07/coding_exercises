def min_product(a, b):
    bigger = b if a < b else a
    smaller = a if a < b else b
    return min_product_helper(smaller, bigger)


def min_product_helper(smaller, bigger):
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger
    s = smaller >> 1
    half_prod = min_product_helper(s, bigger)
    if smaller % 2 == 0:
        return half_prod + half_prod
    return half_prod + half_prod + bigger


if __name__ == "__main__":
    test_cases = [(5, 6), (28, 89), (1234, 245334)]
    for a, b in test_cases:
        res = min_product(a, b)
        print(f"min_product({a},{b})={res}, expected {a*b}")
