# Given a real number between 0-1
# print the binary representation.
# if the number cannot be represend at most 32 characters => error
def bin_to_string(num):
    if num >= 1 or num <= 0:
        return "ERROR"

    bit_str = "."

    while num > 0:
        # multiply by 2 and check if 2n is greater than equal or to 1
        if len(bit_str) > 32:
            return bit_str
        two = num * 2
        if two >= 1:
            bit_str += "1"
            num = two - 1
        else:
            bit_str += "0"
            num = two
    return bit_str


for number in [0.625, 0, 0.1, 0.101, 0.2, 0.5, 1, 2]:
    print(bin_to_string(number))
