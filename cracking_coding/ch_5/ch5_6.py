def bit_swap_required(a: int, b: int) -> int:
    count = 0
    c = a ^ b
    while c:
        count += 1
        c = c & (c - 1)
    return count


a = 0b11101  # 29
b = 0b01111  # 15
bit_swap_required(a, b)
