def draw_line(screen: bytearray, width: int, x1: int, x2: int, y: int) -> None:
    left_byte = (y * width + x1) // 8
    rigth_byte = (y * width + x2) // 8
    left_mask = 0xFF >> x1 % 8
    right_mask = (0xFF >> x2 % 8 + 1) ^ 0xFF
    if left_byte == rigth_byte:
        screen[left_byte] |= left_mask & right_mask
    else:
        screen[left_byte] |= left_mask
        for i in range(left_byte + 1, rigth_byte):
            screen[i] = 0xFF
        screen[rigth_byte] |= right_mask


screen = bytearray(2)
draw_line(screen, width=16, x1=0, x2=15, y=0)

assert screen == bytearray([0b11111111, 0b11111111])
