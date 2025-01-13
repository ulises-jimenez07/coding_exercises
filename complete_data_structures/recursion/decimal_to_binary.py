def decimal_to_binary(n):
    if n in [1, 0]:
        return n
    return 10 * (n % 2) + decimal_to_binary(n // 2)


print(decimal_to_binary(6))
